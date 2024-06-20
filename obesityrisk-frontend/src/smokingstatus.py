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

# Obesity Level by Smoking Status
import matplotlib.pyplot as plt
obesityDF.groupby(['NObeyesdad','SMOKE']).size().unstack().plot(kind='bar',stacked=True)
plt.xlabel('Obesity Level')
plt.ylabel('Count')
_ = plt.title('Obesity Level by Smoking Status')