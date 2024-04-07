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

# FOI UTILIZADO O GRÁFICO DE DISPERSÃO PARA ANÁLISE DE REFERÊNCIA ENTRE NIVEIS DE PESO X TEMPO DE USO EM APARELHOS TECNOLOGICOS
# CONFORME PODEMOS OBSERVAR, PESSOAS DE OBESIDADE TIPO 1 POSSUEM O MAIOR INDICE DE TEMPO DE USO EM APARELHOS TECNOLOGICOS

import matplotlib.pyplot as plt

plt.scatter(df['TUE'], df['NObeyesdad'])
plt.xlabel('Time using technology devices')
plt.ylabel('NObeyesdad')
plt.title('Scatter Plot')
plt.show()