import pandas as pd
from sklearn.datasets import fetch_california_housing 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
def carregar_dados():
    california = fetch_california_housing()
    data = pd.DataFrame(california.data, columns=california.feature_names)
    data['MedHouseVal'] = california.target
    return data


# Explorar os dados
def explorar_dados(data):
    print("Primeiras linhas do DataFrame:")
    print(data.head())

    print("\nInformações sobre o DataFrame:")
    print(data.info())

    print("Estatísticas descritivas sobre o DataFrame:")
    print(data.describe())


    # Correlação entre as características e o preço 
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Heatmap de Correlação')
    plt.show()


    # Distribuições das características e do preço
    plt.figure(figsize=(12, 8))
    for i, column in enumerate(data.columns, 1):
        plt.subplot(3, 3, i)
        sns.histplot(data[column], kde=True)
        plt.title(column)
    plt.tight_layout()
    plt.show()



def preprocessar_dados(data):
    # Verificar se há avalores faltantes
    print("Valores faltantes em cada coluna")
    print(data.isnull().sum())

    # Separar características e alvo
    X = data.drop('MedHouseVal', axis=1)
    y = data['MedHouseVal']

    # Padronizar características
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Dividir dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    print(f"Shape de X_train: {X_train.shape}")
    print(f"Shape de X_test: {X_test.shape}")
    print(f"Shape de y_train: {y_train.shape}")
    print(f"Shape de y_test: {y_test.shape}")

    return X_train, X_test, y_train, y_test

# Carregar e explorar dados
data = carregar_dados()
explorar_dados(data)

# Pré-Processar dados
X_train, X_test, y_train, y_test = preprocessar_dados(data)