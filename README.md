<h1 align="center">🌸 Classificação das Flores *Iris*</h1>

<p align="center">
  <em>Um projeto prático de aprendizado de máquina — AG2 / 2025</em><br>
  <strong>Treinando um modelo para reconhecer espécies de flores a partir de suas medidas.</strong>
</p>

---

## 🧠 Objetivo

O projeto tem como meta desenvolver e avaliar um modelo de **classificação supervisionada** capaz de identificar corretamente as três espécies de flores do gênero *Iris*:

🌷 *Iris setosa*  
🌿 *Iris versicolor*  
💜 *Iris virginica*

---

## 👨‍💻 Autores

- **Lucca Marcondes Madeira** — GES - 420  
- **Pedro Tiso Vinhas Mesquita** — GEC - 1932

---

## 📊 Conjunto de Dados

O conjunto de dados utilizado é o clássico **Iris Dataset**, com **150 amostras** — amplamente usado em estudos e testes de algoritmos de classificação.

Cada flor é descrita por quatro atributos numéricos:

| Atributo | Descrição | Unidade |
|-----------|------------|----------|
| `sepal_length_cm` | Comprimento da sépala | cm |
| `sepal_width_cm`  | Largura da sépala     | cm |
| `petal_length_cm` | Comprimento da pétala | cm |
| `petal_width_cm`  | Largura da pétala     | cm |

> 🔗 Dados obtidos no [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)

---

## ⚙️ Tecnologias Utilizadas

- 🐍 **Python 3**
- 📚 **Pandas** — manipulação e análise de dados  
- 🤖 **Scikit-learn** — modelagem, treino e métricas  

---

## 🚀 Etapas do Projeto

1. **Leitura e preparação dos dados**  
   → Importação do CSV e mapeamento das espécies em valores numéricos  

2. **Divisão em treino e teste**  
   → 80% treino, 20% teste — com *stratify* para equilíbrio das classes  

3. **Treinamento do modelo**  
   → Algoritmo utilizado: `KNeighborsClassifier (k=5)`  

4. **Avaliação e métricas**  
   → Acurácia, matriz de confusão e relatório de classificação  

---

## 📈 Resultados

O modelo apresentou **desempenho perfeito** no conjunto de teste, confirmando a eficiência do kNN para este tipo de classificação.

| Métrica | Resultado |
|----------|------------|
| **Acurácia** | 1.00 (100%) |
| **Classes mais confundidas** | Nenhuma — todas as amostras foram classificadas corretamente |

> 🟢 O modelo foi avaliado com métricas de precisão, recall e F1-score para cada classe.

---

## 💾 Como Executar

```bash
# 1️⃣ Clonar o repositório
git clone https://github.com/PedroTiso/Ag02
cd Ag02

# 2️⃣ Instalar as dependências
pip install -r requirements.txt

# 3️⃣ Executar o script principal
python main.py