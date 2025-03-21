import pandas as pd


#Lendo o dataset em json 
df_acidentes = pd.read_json("C:\\Users\\Dell\\OneDrive\\Desktop\\Data Set PRF\\acidentes2017-2023.json")

#Convertendo o rquivo para csv 
acidentes = "C:/Users/Dell/OneDrive/Desktop/Data Set PRF/acidentes2017-2023.csv"
df_acidentes.to_csv(acidentes, index=False, encoding="utf-8-sig", sep=",")

#Criando uma cópia do dataframe original
df_acidentes_copy = df_acidentes.copy()

df_acidentes_copy = df_acidentes_copy.drop(columns=["id_veiculo"])

#Convertendo tipos
df_acidentes_copy["data_inversa"] = pd.to_datetime(df_acidentes_copy["data_inversa"])
df_acidentes_copy["horario"] = pd.to_datetime(df_acidentes_copy["horario"], format="%H:%M:%S").dt.time
df_acidentes_copy["km"] = df_acidentes_copy["km"].str.replace(",", ".").astype(float)


#Criando tabela dimensão acidentes e passando um índice unico para cada linha
d_acidentes = df_acidentes_copy[["causa_acidente", "tipo_acidente", "classificacao_acidente"]].drop_duplicates().reset_index(drop=True)
d_acidentes["id_acidentes"] = d_acidentes.index + 1 

# Criando tabelas dimensões e fato, (removendo duplicatas e gerando IDs)

#Dimensão local
d_local = df_acidentes_copy[["uf", "br", "km", "municipio", "latitude", "longitude"]].drop_duplicates().reset_index(drop=True)
d_local["id_local"] = d_local.index + 1 

#Dimensão tempo 
d_tempo = df_acidentes_copy[["horario", "fase_dia", "data_inversa", "dia_semana", "condicao_metereologica"]].drop_duplicates().reset_index(drop=True)
d_tempo["id_tempo"] = d_tempo.index + 1

#Dimensão pista 
d_pista = df_acidentes_copy[["sentido_via", "tipo_pista", "tracado_via", "uso_solo"]].drop_duplicates().reset_index(drop=True)
d_pista["id_pista"] = d_pista.index + 1

#Dimensão condutor 
d_condutor = df_acidentes_copy[["tipo_envolvido", "estado_fisico", "idade", "sexo"]].drop_duplicates().reset_index(drop=True)
d_condutor["id_condutor"] = d_condutor.index + 1

#Dimensão veículo 
d_veiculo = df_acidentes_copy[["tipo_veiculo", "marca", "ano_fabricacao_veiculo", "marca_veiculo", "modelo_veiculo"]].drop_duplicates().reset_index(drop=True)
d_veiculo["id_veiculo"] = d_veiculo.index + 1 

# Fazendo merge para adicionar IDs no dataframe principal
df_acidentes_copy = df_acidentes_copy.merge(d_acidentes, on=["causa_acidente", "tipo_acidente", "classificacao_acidente"], how="left")
df_acidentes_copy = df_acidentes_copy.merge(d_local, on=["uf", "br", "km", "municipio", "latitude", "longitude"], how="left")
df_acidentes_copy = df_acidentes_copy.merge(d_tempo, on=["horario", "fase_dia", "data_inversa", "dia_semana", "condicao_metereologica"], how="left")
df_acidentes_copy = df_acidentes_copy.merge(d_pista, on=["sentido_via", "tipo_pista", "tracado_via", "uso_solo"], how="left")
df_acidentes_copy = df_acidentes_copy.merge(d_condutor, on=["tipo_envolvido", "estado_fisico", "idade", "sexo"], how="left")
df_acidentes_copy = df_acidentes_copy.merge(d_veiculo, on=["tipo_veiculo", "marca", "ano_fabricacao_veiculo", "marca_veiculo", "modelo_veiculo"], how="left")

#fato ferido 
f_feridos = df_acidentes_copy[["id_condutor","id_veiculo","id_pista","id_tempo","id_local","id_acidentes","ilesos", "feridos_leves", "feridos_graves", "mortos"]].reset_index(drop=True)
f_feridos["id_feridos"] = f_feridos.index + 1 

# Exportando tabelas para CSV
d_acidentes.to_csv("C:/Users/Dell/OneDrive/Desktop/Data Set PRF/d_acidentes.csv", index=False, encoding="utf-8-sig")
d_local.to_csv("C:/Users/Dell/OneDrive/Desktop/Data Set PRF/d_local.csv", index=False, encoding="utf-8-sig")
d_tempo.to_csv("C:/Users/Dell/OneDrive/Desktop/Data Set PRF/d_tempo.csv", index=False, encoding="utf-8-sig")
d_pista.to_csv("C:/Users/Dell/OneDrive/Desktop/Data Set PRF/d_pista.csv", index=False, encoding="utf-8-sig")
d_condutor.to_csv("C:/Users/Dell/OneDrive/Desktop/Data Set PRF/d_condutor.csv", index=False, encoding="utf-8-sig")
d_veiculo.to_csv("C:/Users/Dell/OneDrive/Desktop/Data Set PRF/d_veiculo.csv", index=False, encoding="utf-8-sig")
f_feridos.to_csv("C:/Users/Dell/OneDrive/Desktop/Data Set PRF/f_feridos.csv", index=False, encoding="utf-8-sig")

print("Exportação concluída com sucesso!")