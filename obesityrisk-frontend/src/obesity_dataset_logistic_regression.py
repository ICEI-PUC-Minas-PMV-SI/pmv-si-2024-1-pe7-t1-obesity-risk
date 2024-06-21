# -*- coding: utf-8 -*-
"""obesity_dataset_logistic_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DvUuQdycGZDV1hZsnloYZBSwIfX5vHbm
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

# Carregar os dados
data = pd.read_csv('ObesityDataSet.csv')

# Tratar valores ausentes
imputer = SimpleImputer(strategy='most_frequent')
data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Codificar variáveis categóricas
label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['family_history_with_overweight'] = label_encoder.fit_transform(data['family_history_with_overweight'])
data['FAVC'] = label_encoder.fit_transform(data['FAVC'])
data['CAEC'] = label_encoder.fit_transform(data['CAEC'])
data['SMOKE'] = label_encoder.fit_transform(data['SMOKE'])
data['SCC'] = label_encoder.fit_transform(data['SCC'])
data['CALC'] = label_encoder.fit_transform(data['CALC'])
data['MTRANS'] = label_encoder.fit_transform(data['MTRANS'])

# One-hot encoding para variáveis categóricas com mais de duas categorias
data = pd.get_dummies(data, columns=['MTRANS'])

# Codificar a variável alvo (NObeyesdad)
label_encoder = LabelEncoder()
data['NObeyesdad'] = label_encoder.fit_transform(data['NObeyesdad'])

# Dividir os dados em variáveis independentes (X) e dependente (y)
X = data.drop('NObeyesdad', axis=1)
y = data['NObeyesdad']

# Padronizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Primeira divisão: 70% treinamento, 30% restante
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Segunda divisão: 50% do restante para validação, 50% para teste
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Balanceamento de classes usando SMOTE
smote = SMOTE()
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Inicializar o modelo de regressão logística
model = LogisticRegression(max_iter=500)

# Treinar o modelo nos dados de treinamento
model.fit(X_train_resampled, y_train_resampled)

# Fazer previsões nos dados de VALIDAÇÃO
y_pred_val = model.predict(X_val)

# Avaliar o modelo nos dados de VALIDAÇÃO
accuracy_val = accuracy_score(y_val, y_pred_val)
print("Validação - Accuracy:", accuracy_val)
print("\nValidação - Classification Report:")
print(classification_report(y_val, y_pred_val))

# Fazer previsões nos dados de TESTE
y_pred = model.predict(X_test)

# Avaliar o modelo nos dados de TESTE
accuracy = accuracy_score(y_test, y_pred)
print("Teste - Accuracy:", accuracy)
print("\nTeste - Classification Report:")
print(classification_report(y_test, y_pred))