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

# CRUZANDO O GRÁFICO DE LINHAS IDADE E PESO X CONSUMO DE COMIDA ENTRE REFEIÇÃO CONSEGUIMOS OBSERVAR QUE QUANTO MAIS ELEVADA É A IDADE DO INDIVIDUO MAIOR A TAXA
# DE CONSUMO DE COMIDA ENTRE REFEIÇÕES

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Weight']
  ys = series['Age']
  
  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = _df_14.sort_values('Weight', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('CAEC')):
  _plot_series(series, series_name, i)
  fig.legend(title='Consumption of food between meals', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Weight')
_ = plt.ylabel('Age')