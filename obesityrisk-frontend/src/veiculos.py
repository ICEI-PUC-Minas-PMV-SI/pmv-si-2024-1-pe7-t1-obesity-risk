# Importação das bibliotecas
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Conexão com o Google Drive
from google.colab import drive
drive.mount('/content/drive/')

# Definição da variável para leitura do dataframe
df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/ObesityDataSet.xlsx')

# Média de calorias consumidas por veículos utilizados
df.groupby('MTRANS')['CH2O'].mean().plot(kind='bar')