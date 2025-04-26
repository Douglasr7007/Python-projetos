import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

base_dados = sns.load_dataset("tips")

base_dados.rename(columns={
    "total_bill" : "total_conta",
    "tip" : "gorjeta",
    "sex" : "sexo",
    "smoker" : "fumante",
    "time" : "hora",
    "size" : "pessoas"
},inplace=True)

print(base_dados.head())

sns.barplot(data=base_dados,y="sexo", x="total_conta", hue="fumante")
plt.show()