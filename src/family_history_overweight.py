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

# REALIZADO EM GRÁFICO DE COLUNAS EMPILHADAS A RELAÇÃO ENTRE HISTORICO FAMILIAR X GENERO
# PODEMOS OBSERVAR QUE O HISTORICO FAMILIAR DE DO SEXO MASCULINO POSSUI MAIOR INDICE DE SOBREPESO DO QUE O HISTORICO FAMILIAR DO SEXO FEMININO

df.groupby('Gender')['family_history_with_overweight'].value_counts().unstack().plot(kind='bar', stacked=True)