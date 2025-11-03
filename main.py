#Importando as bibliotecas necessarias
import pandas as pd
import numpy as np

#Lendo o DataFrame e imprimindo as 5 primeiras linhas
df = pd.read_csv("conjunto_dados/dados.csv")
print(df.head())

#Dicionario mapeado conforme pede o enunciado
# Criando uma nova coluna aplicando o mapeamento
species_map = {"Iris-setosa": 1, "Iris-versicolor": 2, "Iris-virginica": 3}
df["species_num"] = df["species"].replace(species_map)

#Conferindo a nova coluna
print(df.head())

#Mostrando 50 amostras de cada classe
print(df["species_num"].value_counts().sort_index())

#Mostrando os tipos das colunas
print(df.dtypes)

#Aqui, vamos diver em treino e teste, conforme manda o enunciado