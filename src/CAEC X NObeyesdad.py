# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Un9Iy3ldG_p1MPDPv3_4cAm_5s9XNMg
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CONEXÃO COM GOOGLE DRIVE
from google.colab import drive
drive.mount('/content/drive/')

# DEFININDO A VARIAVEL QUE IRÁ LER O DATAFRAME
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ObesityDataSet.csv')

# COMPARAÇÃO ENTRE O CONSUMO DE COMIDA ENTRE REFEIÇÕES E OS NÍVEIS DE OBESIDADE
plt.rcParams["figure.figsize"] = [8.00, 4.00]

plt.rcParams["figure.autolayout"] = True

sns.countplot(data = df, x = "CAEC", hue = "NObeyesdad")
plt.show()