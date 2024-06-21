# -*- coding: utf-8 -*-
"""Random_Forest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qvmX27J90dXlCOJytA2S5aAOiALYNfHM
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve




# CONEXÃO COM GOOGLE DRIVE
from google.colab import drive
drive.mount('/content/drive/')

# DEFININDO A VARIAVEL QUE IRÁ LER O DATAFRAME
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ObesityDataSet.csv')

# Tratar valores ausentes
imputer = SimpleImputer(strategy='most_frequent')
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)


# Converter valores de string em valores numéricos usando LabelEncoder
label_encoder = LabelEncoder()
df_encoded = df.apply(label_encoder.fit_transform)


# Definir as variáveis preditoras (features)
X = df_encoded.drop("NObeyesdad", axis=1)  # Remove a coluna "grau de obesidade"

# Definir a variável alvo (target)
y = df_encoded["NObeyesdad"]


# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo Random Forest
rf_model = RandomForestClassifier(max_depth=10, n_estimators=100, random_state=42, criterion='gini')
rf_model.fit(X_train, y_train)

# Treinar o modelo com os dados de treinamento
rf_model.fit(X_train, y_train)

# Fazer previsões com os dados de teste
y_pred = rf_model.predict(X_test)

# Calcular a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia do modelo Random Forest:", accuracy)

# Imprimir a importância das características
feature_importances = rf_model.feature_importances_
print("\nImportância das características:")
for feature, importance in zip(X.columns, feature_importances):
    print(f"{feature}: {importance:.4f}")

# Imprimir a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nMatriz de Confusão:")
print(conf_matrix)

# Relatório de classificação
print('\nRelatório de classificação no conjunto de teste:')
print(classification_report(y_test, y_pred))


# Treinar e avaliar o modelo usando validação cruzada
scores = cross_val_score(rf_model, X, y, cv=5)  # 5-fold cross-validation
print(f"Acurácias nas diferentes dobras: {scores}")
print(f"Acurácia média: {np.mean(scores)}")


# Visualizar a matriz de confusão
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=label_encoder.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Matriz de Confusão")
plt.figure(figsize=(200,100))
plt.show()


max_depths = range(1, 21)  # Avaliando profundidades de 1 a 20

mean_scores = []

for max_depth in max_depths:
    rf = RandomForestClassifier(max_depth=max_depth, random_state=42)
    scores = cross_val_score(rf, X, y, cv=5)  # Usando 5-fold cross-validation
    mean_scores.append(np.mean(scores))

# Imprimir os resultados
for depth, score in zip(max_depths, mean_scores):
    print(f"Max Depth: {depth}, Acurácia Validação Cruzada: {score:.4f}")

plt.figure(figsize=(10, 6))
plt.plot(max_depths, mean_scores, marker='o')
plt.xlabel('Max Depth')
plt.ylabel('Acurácia Validação Cruzada')
plt.title('Random Forest Performance vs Max Depth')
plt.grid(True)
plt.show()


# Obter curvas de aprendizado
train_sizes, train_scores, test_scores = learning_curve(rf, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10))

# Calcular médias e desvios padrão
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

# Plotar curvas de aprendizado
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores_mean, 'o-', color='r', label='Pontuação treinamento')
plt.plot(train_sizes, test_scores_mean, 'o-', color='g', label='Pontuação validação cruzada')
plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color='r')
plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color='g')
plt.xlabel('Exemplos de treinamento')
plt.ylabel('Pontuação')
plt.legend(loc='best')
plt.title('Curva de Aprendizado (Random Forest)')
plt.grid(True)
plt.show()


# Definir diferentes tamanhos de conjuntos de teste
test_sizes = [0.1, 0.3, 0.5]

# Treinar e avaliar o modelo para diferentes tamanhos de conjuntos de teste
for test_size in test_sizes:
    # Dividir os dados em conjunto de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Criar e treinar o modelo Random Forest
    rf_model = RandomForestClassifier(max_depth=10, n_estimators=100, random_state=42, criterion='gini')
    rf_model.fit(X_train, y_train)

    # Fazer previsões com os dados de teste
    y_pred = rf_model.predict(X_test)

    # Calcular a acurácia do modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Acurácia do modelo Random Forest com conjunto de teste de {test_size * 100}%: {accuracy:.4f}")

    # Relatório de classificação
    print('\nRelatório de classificação no conjunto de teste:')
    print(classification_report(y_test, y_pred))

    # Imprimir a matriz de confusão
    conf_matrix = confusion_matrix(y_test, y_pred)
    print("\nMatriz de Confusão:")
    print(conf_matrix)





#col_name = "NObeyesdad"  # Substitua 'nome_da_coluna' pelo nome da coluna desejada

# Criar um vetor vazio
#vetor = []
#vetorx = []

# Adicionar os elementos do conjunto de dados ao vetor
#for value in df_encoded[col_name]:
#   vetor.append(value)

#for val in df[col_name]:
#    vetorx.append(val)

# Associar os elementos dos dois vetores em pares de tuplas
#pares_associados = zip(vetor, vetorx)

# Imprimir os pares associados
#for par in pares_associados:
#    print(par)