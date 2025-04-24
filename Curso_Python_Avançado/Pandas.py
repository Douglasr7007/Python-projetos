#Importando Pandas para a manipulação dos dados

import pandas as pd

#Ler o arquivo em CSV localmente ou remoto 

df = pd.read_csv("**************")

#Verificar o tipo do meu arquivo, nesse caso é, um DATAFRAME 

print(type(df))

#Verificar as 5 primeiras linhas do dataframe 

print(df.head())


#Verificar a 5 últimas linhas do dataframe 

print(df.tail())


#Verifica a quantidade de linhas e colunas 

print(df.shape)


#Verifica a colunas como um array 

print(df.columns)


#Verifica se tem duplicatas no dataframe, tráz um valor booleano como resposta 

print(df.duplicated())


#Fazer a soma de quantas duplicatas tem no dataframe 


print(df.duplicated().sum())


#INFO irá trazer informações genéricas sobre o dataframe. Trás o total de index/registros e colunas, total de 
#valores não nulos e tipo de dados. Faz as observações dos dtypes.

print(df.info())


#Verifica a existência de NAN ( Valores Nulos ) e faz a somatória dos dados

print(df.isna().sum())


#Describe tras os sumários dos dados, resumo estatístico do dataframe 

print(df.describe())

#Describe ALL trás o resumo estatístico de todos os dados do dataframe, incluindo as variáveis categoricas 

print(df.describe(include= all))

#Quantidade de valores unicos em cada coluna 

print(df.nunique())


#Verifica os valores unicos da coluna especifica

print(df["Qualquer coluna"].unique())


#Função COUNT_VALUES faz a contagem de um conjunto de dados especificados no meu dataframe 

print(df["Genêro"].value_counts())


#Criando uma nova coluna para se calcular a média através da coluna de provas dos meus alunos e,
#especificando o eixo


"  df.[mean] = df[provas].mean(axis = 1)  "
print(df.head())


