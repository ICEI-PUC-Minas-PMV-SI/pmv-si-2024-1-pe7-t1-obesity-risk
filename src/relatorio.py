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

# instalando biblioteca SWEETVIZ
!pip install SWEETVIZ

# importando biblioteca necessárias
import sweetviz

# Carrega relatório
report_obesity = sweetviz.analyze(df)

# Carrega o relatório em HTML para visualização
report_obesity.show_html('report_obesity.html')