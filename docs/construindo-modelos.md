# Preparação dos dados

Nesta seção, descrevemos as técnicas utilizadas para o pré-processamento e tratamento dos dados do dataset.

### Limpeza dos dados

* **Valores ausentes**: não identificamos valores ausentes, não sendo necessário tratar, imputar ou remover valores.
* **Outliers**:
  * **Número de Refeições Principais (NCP)**: 826 entradas apresentam valores não inteiros como por exemplo 1.003566 e 2.739. Nesses casos, optamos por desconsiderar os valores após a vírgula, assumindo que na verdade se tratam de 1 ou 2 refeições, respectivamente.
  * **Idade**: 1375 valores apresentam valores não inteiros como por exemplo 16.093234 e 55.24625. Nesses casos, optamos por desconsiderar os valores após a vírgula, assumindo que na verdade se tratam de 16 e 55 anos, respectivamente.
  * **Frequência de consumo de vegetais (FCVC)**: 826 entradas apresentam valores não inteiros como por exemplo 2.739 e 1.005578. Nesses casos, optamos por desconsiderar os valores após a vírgula, assumindo que na verdade se tratam de 2 e 1 vez ao dia, respectivamente.
  * **Consumo de água diário (CH2O)**: 1290 entradas apresentam valores não inteiros, como por exemplo 1.000463 e 2.999495. Nesses casos, optamos por arredondar para o inteiro mais próximo, assumindo que na verdade se tratam de 1 e 3 vezes ao dia, respectivamente. Optamos por arredondar e não desconsiderar as casas após a vírgula devido à quantidade de entradas afetadas por essa "anomalia". O valor mínimo era 1 e o valor máximo 3. Considerando que uma pessoa não diria que ingere exatamente 2.999495 litros de água por dia, assumimos que se tratava da frequência de consumo e não da quantidade.
  * **Frequência de atividade física (FAF)**: 1208 entradas apresentam valores não inteiros, como por exemplo 0.000096 e 2.999918. Nesses casos, optamos por arredondar para o inteiro mais próximo, assumindo que na verdade se tratam de 1 e 3 vezes por semana, respectivamente.
  
### Transformação de Dados

* **Gender**: optamos por substituir _Female_ por 0 e _Male_ por 1, escolhemos essa ordem devido a Male corresponder a 51% dos casos.
* **family_history_with_overweight**: optamos por substituir _No_ por 0 e _Yes_ por 1.
* **FAVC**: optamos por substituir _No_ por 0 e _Yes_ por 1.
* **SMOKE**: optamos por substituir _No_ por 0 e _Yes_ por 1.
* **SCC**: optamos por substituir _No_ por 0 e _Yes_ por 1.
* **CAEC**: optamos por utilizar a técnica de _One-Hot Encoding_, criando os atributos binários onde 0 significa _False_ e 1 significa _True_. Serão os seguintes atributos criados: _Sometimes, Frequently, Always e No_.
* **CALC**: optamos por utilizar a técnica de _One-Hot Encoding_, criando os atributos binários onde 0 significa _False_ e 1 significa _True_. Serão os seguintes atributos criados: _Sometimes, Frequently, Always e No_.
* **MTRANS**: optamos por utilizar a técnica de _One-Hot Encoding_, criando os atributos binários onde 0 significa _False_ e 1 significa _True_. Serão os seguintes atributos criados: _Public Transportation, Automobile, Walking, Motorbike e Bike_.
* **NObeyesdad**: optamos por utilizar a técnica de _One-Hot Encoding_, criando os atributos binários onde 0 significa _False_ e 1 significa _True_. Serão os seguintes atributos criados: _Insufficient Weight, Normal Weight, Overweight Level I, Overweight Level II, Obesity Type I, Obesity Type II, Obesity Type III_.

### _Feature Engineering_: crie novos atributos que possam ser mais informativos para o modelo; selecione características relevantes e descarte as menos importantes.

### Tratamento de dados desbalanceados: se as classes de interesse forem desbalanceadas, considere técnicas como _oversampling_, _undersampling_ ou o uso de algoritmos que lidam naturalmente com desbalanceamento.

### Separação de dados: divida os dados em conjuntos de treinamento, validação e teste para avaliar o desempenho do modelo de maneira adequada.
  
### Manuseio de Dados Temporais: se lidar com dados temporais, considere a ordenação adequada e técnicas específicas para esse tipo de dado.
  
### Redução de Dimensionalidade: aplique técnicas como PCA (Análise de Componentes Principais) se a dimensionalidade dos dados for muito alta.

### Validação Cruzada: utilize validação cruzada para avaliar o desempenho do modelo de forma mais robusta.

### Monitoramento Contínuo: atualize e adapte o pré-processamento conforme necessário ao longo do tempo, especialmente se os dados ou as condições do problema mudarem.

# Descrição dos modelos

Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever os algoritmos de aprendizado de máquina selecionados para a construção dos modelos propostos. Inclua informações abrangentes sobre cada algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha de cada um dos algoritmos. 

Explore aspectos específicos, como o ajuste dos parâmetros livres de cada algoritmo. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas.

Como parte da comprovação de construção dos modelos, um vídeo de demonstração com todas as etapas de pré-processamento e de execução dos modelos deverá ser entregue. Este vídeo poderá ser do tipo _screencast_ e é imprescindível a narração contemplando a demonstração de todas as etapas realizadas.

# Avaliação dos modelos criados

## Métricas utilizadas

Nesta seção, as métricas utilizadas para avaliar os modelos desenvolvidos deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 
