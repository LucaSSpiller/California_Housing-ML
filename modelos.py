# modelos.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from preprocessamento import carregar_dados, preprocessar_dados
import joblib

def avaliar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2, y_pred

def treinar_modelos(X_train, y_train, X_test, y_test):
    # Definir os modelos
    modelos = {
        'Regressão Linear': LinearRegression(),
        'Ridge': Ridge(),
        'Lasso': Lasso(),
        'Árvore de Decisão': DecisionTreeRegressor(),
        'Random Forest': RandomForestRegressor()
    }
    
    # Treinar e avaliar modelos
    resultados = {}
    for nome, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        mse, r2, y_pred = avaliar_modelo(modelo, X_test, y_test)
        resultados[nome] = {'MSE': mse, 'R2': r2}
        
        # Gráfico de dispersão dos valores reais vs previstos para cada modelo
        plt.figure(figsize=(8, 6))
        plt.scatter(y_test, y_pred, alpha=0.3)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
        plt.xlabel('Valores Reais')
        plt.ylabel('Valores Previstos')
        plt.title(f'Valores Reais vs Previstos ({nome})')
        plt.show()
        
        # Distribuição dos resíduos para cada modelo
        residuos = y_test - y_pred
        plt.figure(figsize=(8, 6))
        sns.histplot(residuos, kde=True)
        plt.xlabel('Resíduos')
        plt.title(f'Distribuição dos Resíduos ({nome})')
        plt.show()
    
    return pd.DataFrame(resultados).T

def salvar_modelo(modelo, nome_arquivo):
    joblib.dump(modelo, nome_arquivo)
    print(f"Modelo salvo como {nome_arquivo}")

def carregar_modelo(nome_arquivo):
    modelo = joblib.load(nome_arquivo)
    print(f"Modelo carregado de {nome_arquivo}")
    return modelo

def fazer_previsao(modelo, novos_dados):
    novos_dados_scaled = scaler.transform(novos_dados)
    previsoes = modelo.predict(novos_dados_scaled)
    return previsoes

# Carregar e pré-processar os dados
data = carregar_dados()
X_train, X_test, y_train, y_test = preprocessar_dados(data)

# Ajuste do scaler para futuros dados
scaler = StandardScaler().fit(X_train)

# Treinar e avaliar os modelos
resultados = treinar_modelos(X_train, y_train, X_test, y_test)
print(resultados)

# Salvar o melhor modelo
melhor_modelo_nome = 'Random Forest'
melhor_modelo = RandomForestRegressor()
melhor_modelo.fit(X_train, y_train)
salvar_modelo(melhor_modelo, f'{melhor_modelo_nome}.joblib')

# Carregar o modelo salvo
modelo_carregado = carregar_modelo(f'{melhor_modelo_nome}.joblib')

# Avaliar o modelo carregado
mse, r2, y_pred_carregado = avaliar_modelo(modelo_carregado, X_test, y_test)
print(f"Avaliação do modelo carregado ({melhor_modelo_nome}): MSE={mse:.2f}, R2={r2:.2f}")

# Exemplo de novos dados (substitua pelos seus dados)
novos_dados = np.array([[8.3252, 41, 6.984127, 1.023809, 322, 2.555556, -122.213675, 37.757647]])
previsao = fazer_previsao(modelo_carregado, novos_dados)
print(f"Previsão para novos dados: {previsao}")
