# IMPORTANDO BIBLIOTECAS
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CONEXÃO COM GOOGLE DRIVE
from google.colab import drive
drive.mount('/content/drive/')

# DEFININDO A VARIAVEL QUE IRÁ LER O DATAFRAME
df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/ObesityDataSet.xlsx')


# Obesity vs High-Calorie Food Consumption
import matplotlib.pyplot as plt
obesityDF.groupby('CAEC')['NObeyesdad'].value_counts().unstack().plot(kind='bar')
plt.xlabel('CAEC')
plt.ylabel('Count')
_ = plt.title('Obesity vs High-Calorie Food Consumption')