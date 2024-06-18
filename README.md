# Projeto de Machine Learning: Previsão de Preços de Casas na Califórnia
## Descrição

<p>Este projeto utiliza o dataset de California Housing para prever os preços das casas com base em várias características. O projeto cobre desde o carregamento e exploração dos dados até o treinamento, avaliação, salvamento e utilização de modelos de Machine Learning.</p>

### Dependências

  <p>. Python 3.x</p>
  <p>. Pandas</p>
  <p>. Scikit-learn</p>
  <p>. Matplotlib</p>
  <p>. Seaborn</p>
  <p>. Joblib</p>

### Instalação das Dependências

Para instalar as dependências necessárias, você pode usar o pip:

```
pip install pandas scikit-learn matplotlib seaborn joblib
```

# Passo a Passo do Projeto
## 1. Carregar e Explorar os Dados

 <p>Objetivo: Carregar o dataset e explorar suas características principais para entender melhor os dados com os quais estamos lidando.</p>

### Explicação:

  <p>Carregar os dados: Uso da função fetch_california_housing da biblioteca sklearn.datasets para obter o dataset.</p>
  <p>DataFrame: Convertendo os dados carregados para um DataFrame do Pandas para facilitar a manipulação.</p>
  <p>Explorar os dados: Visualizar as primeiras linhas, verificar informações gerais e obter estatísticas descritivas dos dados.</p>
  <p>A visualização da correlação entre características e a distribuição dos dados ajuda a entender como as variáveis estão relacionadas.</p>

## 2. Pré-processar os Dados

<p>Objetivo: Padronizar as características e dividir os dados em conjuntos de treinamento e teste.</p>

### Explicação:

  <p>Verificar valores faltantes: Verificar se há valores faltantes nas colunas.</p>
  <p>Separar características e alvo: Dividir os dados em X (características) e y (alvo, ou seja, preço das casas).</p>
  <p>Padronizar as características: Uso do StandardScaler para padronizar as características, garantindo que todas estejam na mesma escala.</p>
  <p>Dividir os dados: Utilizar train_test_split para dividir os dados em conjuntos de treinamento e teste.</p>
  <p>Isso permite avaliar a performance do modelo em dados que ele não viu durante o treinamento.</p>

## 3. Treinar e Avaliar Modelos

<p>Objetivo: Treinar e avaliar vários modelos de regressão.</p>

### Explicação:

  <p>Modelos: Uso de diferentes modelos de regressão (LinearRegression, Ridge, Lasso, DecisionTreeRegressor, RandomForestRegressor) para prever os preços das casas.</p>
  <p>Treinamento: Ajustar cada modelo aos dados de treinamento (fit).</p>
  <p>Avaliação: Avaliar cada modelo nos dados de teste usando métricas como Mean Squared Error (MSE) e R2 Score. Visualizar a relação entre os valores reais e previstos, bem como a distribuição dos resíduos (diferença entre valores reais e previstos).</p>

## 4. Salvar e Carregar o Modelo

<p>Objetivo: Salvar o modelo treinado para que ele possa ser reutilizado sem precisar treiná-lo novamente.</p>

### Explicação:

  <p>Salvar o modelo: Utilizar joblib para salvar o modelo treinado em um arquivo. Isso permite carregar o modelo posteriormente sem precisar re-treiná-lo.</p> 
  <p>Carregar o modelo: Utilizar joblib para carregar o modelo salvo de um arquivo. Avaliar o modelo carregado para garantir que ele foi salvo e carregado corretamente.</p>

## 5. Fazer Previsões com Novos Dados

<p>Objetivo: Utilizar o modelo carregado para fazer previsões em novos dados.</p>

### Explicação:

  <p>Transformar novos dados: Padronizar os novos dados usando o mesmo scaler utilizado no preprocessamento.</p>
  <p>Fazer previsões: Utilizar o modelo carregado para fazer previsões nos novos dados padronizados.</p>

## Conclusão

<p>Com este manual, é possível ver como desenvolver um pipeline de Machine Learning para prever preços de casas. Ele abrange desde a exploração e preprocessamento dos dados até o treinamento, avaliação, salvamento e utilização de modelos. </p>
