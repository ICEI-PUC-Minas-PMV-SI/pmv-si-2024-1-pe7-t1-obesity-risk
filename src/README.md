# Instruções de utilização

## Instalação do Site

A pré análise de dados foi gerado utilizando a linguagem Python e as bibliotecas:
* Pandas
* ProfileReport
* sweetviz

## Histórico de versões

### [1.0.0] - 18/03/2024
#### Adicionado
- Version 1.1.0

## PANDAS PROFILING
# instalando o PANDAS PROFILING
!pip install ydata-profiling

# importar bibliotecas necessárias
import pandas as pd
from ydata_profiling import ProfileReport

# pegas a quantidade de linhas e colunas que possuem no DF
obesityDF.shape

# criando o ProfileReport (case sensitive)
report = ProfileReport(obesityDF)

# criar a visualização do iFrame (para que os rsultados sejam exibidos dentro do Notebook)
report.to_notebook_iframe()

## SWEETVIZ
# instalando biblioteca SWEETVIZ
!pip install SWEETVIZ

# importando biblioteca necessárias
import pandas as pd
import sweetviz

# Mapeando o caminho do DF ObesityDataSet
obesityDF = pd.read_excel('/content/gdrive/MyDrive/SI/ObesityDataSet.xlsx')

# Carrega relatório
report_obesity = sweetviz.analyze(obesityDF)

# Carrega o relatório em HTML para visualização
report_obesity.show_html('report_obesity.html')
