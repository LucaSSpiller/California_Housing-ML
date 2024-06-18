# Projeto de Machine Learning: Previsão de Preços de Casas na Califórnia
## Descrição

<p>Este projeto utiliza o dataset de California Housing para prever os preços das casas com base em várias características. O projeto cobre desde o carregamento e exploração dos dados até o treinamento, avaliação, salvamento e utilização de modelos de Machine Learning.</p>

### Dependências

- Python 3
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

### Instalação das Dependências

Para instalar as dependências necessárias, você pode usar o pip:

```
pip install pandas scikit-learn matplotlib seaborn joblib
```

# Passo a Passo do Projeto
## 1. Carregar e Explorar os Dados

 <p>Objetivo: Carregar o dataset e explorar suas características principais para entender melhor os dados com os quais estamos lidando.</p>

### Explicação:
- Carregar os dados: Uso da função fetch_california_housing da biblioteca sklearn.datasets para obter o dataset.
- DataFrame: Convertendo os dados carregados para um DataFrame do Pandas para facilitar a manipulação.
- Explorar os dados: Visualizar as primeiras linhas, verificar informações gerais e obter estatísticas descritivas dos dados.
- A visualização da correlação entre características e a distribuição dos dados ajuda a entender como as variáveis estão relacionadas.

## 2. Pré-processar os Dados

<p>Objetivo: Padronizar as características e dividir os dados em conjuntos de treinamento e teste.</p>

### Explicação:

- Verificar valores faltantes: Verificar se há valores faltantes nas colunas.
- Separar características e alvo: Dividir os dados em X (características) e y (alvo, ou seja, preço das casas).
- Padronizar as características: Uso do StandardScaler para padronizar as características, garantindo que todas estejam na mesma escala.
- Dividir os dados: Utilizar train_test_split para dividir os dados em conjuntos de treinamento e teste.
- Isso permite avaliar a performance do modelo em dados que ele não viu durante o treinamento.

## 3. Treinar e Avaliar Modelos

<p>Objetivo: Treinar e avaliar vários modelos de regressão.</p>

### Explicação:

- RandomForestRegressor) para prever os preços das casas.
- Treinamento: Ajustar cada modelo aos dados de treinamento (fit).
- Avaliação: Avaliar cada modelo nos dados de teste usando métricas como Mean Squared Error (MSE) e R2 Score. Visualizar a relação entre os valores reais e previstos, bem como a distribuição dos resíduos (diferença entre valores reais e previstos).

## 4. Salvar e Carregar o Modelo

<p>Objetivo: Salvar o modelo treinado para que ele possa ser reutilizado sem precisar treiná-lo novamente.</p>

### Explicação:

- Salvar o modelo: Utilizar joblib para salvar o modelo treinado em um arquivo. Isso permite carregar o modelo posteriormente sem precisar re-treiná-lo.
- Carregar o modelo: Utilizar joblib para carregar o modelo salvo de um arquivo. Avaliar o modelo carregado para garantir que ele foi salvo e carregado corretamente.

## 5. Fazer Previsões com Novos Dados

<p>Objetivo: Utilizar o modelo carregado para fazer previsões em novos dados.</p>

### Explicação:

- Transformar novos dados: Padronizar os novos dados usando o mesmo scaler utilizado no preprocessamento.
- Fazer previsões: Utilizar o modelo carregado para fazer previsões nos novos dados padronizados.

## 6. Implementação do Modelo como um Serviço Web

<p>Objetivo: Implementar o modelo de Machine Learning como um serviço web utilizando Flask.</p>

### Passo a Passo da Implementação

1. Instalar o Flask:
```
pip install flask
```
2. Criar o Arquivo app.py;
3. Criar o Arquivo HTML index.html na pasta templates;
4. Executar o Serviço Web:
```
python web/app.py
```
Isso iniciará o servidor local do Flask. Entre em http://localhost:5000/ para acessar a interface do usuário e fazer previsões de preços de casas.

## Conclusão

<p>Com este manual, é possível ver como desenvolver um pipeline de Machine Learning para prever preços de casas. Ele abrange desde a exploração e preprocessamento dos dados até o treinamento, avaliação, salvamento e utilização de modelos. </p>
