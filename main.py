# Importação das bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Leitura do arquivo CSV
df = pd.read_csv("conjunto_dados/dados.csv")
print(df.head())

# Mapeamento das espécies (conforme enunciado)
species_map = {
    "Iris-setosa": 1,
    "Iris-versicolor": 2,
    "Iris-virginica": 3
}
df["species_num"] = df["species"].replace(species_map)

# Conferências
print("\nPrévia com a nova coluna 'species_num':")
print(df.head())

print("\nContagem por classe:")
print(df["species_num"].value_counts().sort_index())

print("\nTipos de dados:")
print(df.dtypes)

#Definindo o que sera entrada e o que sera saida
X = df[["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm"]]
Y = df["species_num"]

#Divisao de Treino e Teste
X_train, X_test, Y_train, Y_test = train_test_split(
    X,Y,
    test_size=0.2,
    shuffle=True,
    random_state=42,
    stratify=Y
)

#Verificando os tamanhos
print("\nShapes:")
print("X_train:", X_train.shape, "| y_train:", Y_train.shape)
print("X_test :", X_test.shape,  "| y_test :", Y_test.shape)

#Criando a instancia do modelo
modelo = KNeighborsClassifier(n_neighbors=5)

#Parte Responsável por treinar o modelo
modelo.fit(X_train, Y_train)

#Testando o modelo com 30 flores novas
y_pred = modelo.predict(X_test)

print(y_pred[:10])

print(Y_test[:10].values)

#Porcentagem de acertos no conjunto de teste
acertos = accuracy_score(Y_test, y_pred)
print(f"Porcentagem de acertos: {acertos:.3f}")

#Tabelas de acertos/erros por classe
confusao = confusion_matrix(Y_test, y_pred, labels=[1,2,3])
print("\nMatriz de confusão (linhas = verdade, colunas = predição):")
print(confusao)

#Relatorio de classificacao
nomes = ["setosa", "versicolor", "virginica"]
print("\nRelatorio de Classificacao")
print(classification_report(Y_test, y_pred, target_names=nomes, digits=3))


print("\n--- Classificação de nova amostra ---")
# Coleta dos dados do usuário
sepal_length_cm = float(input("Digite o comprimento da sépala (cm): "))
sepal_width_cm     = float(input("Digite a largura da sépala (cm): "))
petal_length_cm = float(input("Digite o comprimento da pétala (cm): "))
petal_width_cm     = float(input("Digite a largura da pétala (cm): "))


# Criando a amostra nova como DataFrame, com os mesmos nomes de coluna de X
amostra_nova = pd.DataFrame( 
    [[sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm]], 
    columns=X.columns
) 

# Realizando a predição
predicao = modelo.predict(amostra_nova)[0]

# Mapeando o número para o nome da espécie
mapa_especies = {1: "Iris-setosa", 2: "Iris-versicolor", 3: "Iris-virginica"}

print(f"\nO modelo classificou a flor como: {mapa_especies[predicao]}")
