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

# Frequência de consumo de alimentos entre as refeições
from matplotlib import pyplot as plt
import seaborn as sns
df.groupby('CAEC').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)