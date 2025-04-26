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

print(base_dados.describe())
print(base_dados["total_conta"].max())
plt.boxplot(base_dados["total_conta"])
plt.show()

