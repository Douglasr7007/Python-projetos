import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


base_dados = sns.load_dataset("tips")

base_dados.rename(columns={
    "total_bill" : "total_conta",
    "tip" : "gorjeta",
    "sex" : "sexo",
    "smoker" : "fumante",
    "time" : "hora",
    "size" : "pessoas"
},inplace=True)

#Verificando a amplitude do meu conjunto de dados
print(base_dados["total_conta"].max() - base_dados["total_conta"].min())

print(base_dados.describe())

#Verificando a aplitude interquatilica 
print(base_dados["total_conta"].describe()[6:7].values - base_dados["total_conta"].describe()[4:5].values)

# + De uma maneira de pegar os quartis 

#Verificando a aplintude semi-interquatílica
q3 = base_dados["total_conta"].quantile(0.75)
q1 = base_dados["total_conta"].quantile(0.25)
d_i = (q3 - q1)/2
print(d_i)


#Verificando a distancia (variancia) que os dados estão da média
print(base_dados["total_conta"].var())


#Verificando o desvio padrão dos meus dados 
print(base_dados["total_conta"].std())