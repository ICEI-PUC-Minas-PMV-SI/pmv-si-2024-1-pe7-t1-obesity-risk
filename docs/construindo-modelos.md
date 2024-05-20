# Pergunta orientada a dados

Neste estudo, analisamos dados de dieta e estilo de vida para compreender os padrões associados à obesidade. Nosso objetivo é identificar os fatores que contribuem para esses problemas de saúde e desenvolver estratégias de prevenção. Execute análises detalhadas, incluindo processamento de dados, transformação e engenharia de recursos.

 - Refinamento de dados: esta etapa examina os dados em busca de problemas como valores ausentes e valores discrepantes. O script diz que nenhum valor ausente foi encontrado, o que significa que o conjunto de dados está completo. No entanto, foram encontradas diferenças para diversas variáveis, incluindo número de refeições por semana, idade, frequência de consumo de vegetais, ingestão diária de água e frequência de atividade física. Para lidar com essas exceções, decidimos tornar os dados consistentes arredondando os valores não inteiros para o número inteiro mais próximo. 
 - Transformação de dados: aqui, as transformações são feitas em variáveis ​​brutas para torná-las adequadas para análise. Por exemplo, as variáveis ​​Gênero e história_família_com_sobrepeso foram convertidas para valores binários (0 para não, 1 para sim) para facilitar a análise estatística.
 - Análise técnica: esta etapa consiste na criação de novas variáveis ​​a partir das anteriores. O artigo afirma que o índice de massa corporal (IMC) é calculado com base no peso e na altura de uma pessoa. Além disso, foram criadas variáveis ​​binárias para outras características como hábito de fumar, frequência de consumo de vegetais, etc. Essas novas variáveis ​​podem fornecer mais informações sobre seus dados e ajudá-lo a criar modelos preditivos mais precisos.
 - Conjunto de dados: Por fim, os dados são divididos em conjuntos de treinamento, validação e teste. Esta etapa é importante para avaliar o desempenho do seu modelo de análise e garantir que ele possa ser estendido para novos dados que não foram utilizados para treinamento. Para garantir uma distribuição justa dos dados, escolhemos 70% para treinamento e 15% para validação e teste. Essas etapas são importantes para preparar os dados para análise e garantir a confiabilidade dos resultados. Também ajuda a esclarecer a definição e a diversidade das questões de investigação e fornece informações valiosas sobre padrões e tendências em dados relacionados com a saúde e a obesidade.

# Tipos de dados do dataset

| Variável | Tipo | Faixa de Valores |
|---|---|---|
| Gênero (Gender) | Categórica nominal | Masculino (Male), Feminino (Female) |
| Idade (Age) | Quantitativa discreta | 17 a 61 |
| Altura (Height) | Quantitativa contínua  | 1.45 a 1.98 |
| Peso (Weight) | Quantitativa contínua  | 39 a 173 |
| Histórico familiar de sobrepeso (family_history_with_overweight) | Categórica nominal  | Sim (Yes), Não (No) |
| Consumo de alimentos com alta caloria entre as refeições (FAVC) | Categórica nominal  | Sim (Yes), Não (No) |
| Frequência de consumo de vegetais (FCVC) | Quantitativa discreta | 1 a 3 |
| Número de Refeições Principais (NCP) | Quantitativa discreta | 1 a 4 |
| Consumo de alimentos entre as refeições (CAEC)) | Categórica ordinal | Não (No), Às vezes (Sometimes), Frequentemente (Frequently), Sempre (Always) |
| Tabagismo (Smoke) | Categórica nominal | Sim (Yes), No (Não) |
| Consumo de água diário (CH2O) | Quantitativa discreta  | 1 a 3 |
| Monitoramento do consumo de calorias (SCC) | Categórica nominal | Sim (Yes), No (Não) |
| Frequência de atividade física (FAF) | Quantitativa discreta  | 0 a 3 |
| Tempo usando dispositivos tecnológicos (TUE) | Quantitativa discreta  | 0 a 2 |
| Consumo de álcool (CALC)) | Categórica ordinal | Não (No), Às vezes (Sometimes), Frequentemente (Frequently), Sempre (Always) |
| Meio de transporte utilizado (MTRANS) | Categórica nominal | Transporte público (Public_Transportation), Carro (Automobile), Andando (Walking), Moto (Motorbike), Bicicleta (Bike) |
| Nível de obesidade (NObeyesdad)) | Categórica ordinal | Peso insuficiente (Insufficient_Weight), Normal (Normal_Weight), Sobrepeso grau I (Overweight_Level_I), Sobrepeso grau II (Overweight_Level_II), Obesidade grau I (Obesity_Type_I), Obesidade grau II (Obesity_Type_II), Obesidade grau III (Obesity_Type_III) |

# Outras bases de dados úteis (Em progresso)
A integração de uma base de dados com outros datasets é uma estratégia que pode proporcionar uma série de vantagens. Isso inclui aprimoramento da precisão dos modelos de previsão, expansão da diversidade de dados, entre outros benefícios.

Em nossa busca por conjuntos de dados adicionais que poderiam enriquecer nossa pesquisa, encontramos o dataset ‘Diabetes Health Indicators Dataset’. Este conjunto de dados apresenta uma variedade de informações que, se correlacionadas com nossa base de dados atual, poderiam contribuir significativamente para a solução do problema identificado.

Informações como ‘Fruits - Consumo de Frutas Por Dia’ e ‘Diabetes_012 - Sem diabetes, pré-diabetes, diabetes’ são exemplos de dados que poderiam agregar valor à nossa pesquisa, proporcionando novas perspectivas e insights valiosos.

# Preparação dos dados

Nesta seção, descrevemos as técnicas utilizadas para o pré-processamento e tratamento dos dados do dataset.

### Limpeza dos dados

* **Valores ausentes**: não identificamos valores ausentes, não sendo necessário tratar, imputar ou remover valores.
* **Outliers**:
  * **Número de Refeições Principais (NCP)**: 826 entradas apresentam valores não inteiros como por exemplo 1.003566 e 2.739. Nesses casos, optamos por arredondar para o inteiro mais próximo.
  * **Idade**: 1375 valores apresentam valores não inteiros como por exemplo 16.093234 e 55.24625. Nesses casos, optamos por arredondar para o inteiro mais próximo.
  * **Frequência de consumo de vegetais (FCVC)**: 826 entradas apresentam valores não inteiros como por exemplo 2.739 e 1.005578. Nesses casos, optamos por arredondar para o inteiro mais próximo.
  * **Consumo de água diário (CH2O)**: 1290 entradas apresentam valores não inteiros, como por exemplo 1.000463 e 2.999495. Nesses casos, optamos por arredondar para o inteiro mais próximo, assumindo que na verdade se tratam de 1 e 3 vezes ao dia, respectivamente. O valor mínimo era 1 e o valor máximo 3. Considerando que uma pessoa não diria que ingere exatamente 2.999495 litros de água por dia, assumimos que se tratava da frequência de consumo e não da quantidade.
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

### _Feature Engineering_
Para validação, optamos por criar o atributo IMC onde faremos manualmente o cálculo do Índice de Massa Corporal = Peso / (Altura x Altura) para verificar se o valor em _NObeyesdad_ classifica corretamente. Consideraremos os intervalos conforme os níveis determinados pela Organização Mundial de Saúde (OMS, 2022). Para o valor de "Pre-obesity", chamaremos de sobrepeso e agregaremos os níveis 1 e 2.

### Separação de dados
Os dados foram divididos em conjuntos de treinamento (70%), validação (15%) e teste (15%) visando garantir um bom desempenho do modelo.

# Descrição dos modelos

REMOVER APÓS ADICIONAR OS MODELOS: 

<<< --------- Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever os algoritmos de aprendizado de máquina selecionados para a construção dos modelos propostos. Inclua informações abrangentes sobre cada algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha de cada um dos algoritmos. Explore aspectos específicos, como o ajuste dos parâmetros livres de cada algoritmo. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas. GRAVAR O VIDEO!!! Como parte da comprovação de construção dos modelos, um vídeo de demonstração com todas as etapas de pré-processamento e de execução dos modelos deverá ser entregue. Este vídeo poderá ser do tipo _screencast_ e é imprescindível a narração contemplando a demonstração de todas as etapas realizadas. 
----------- >>>

1. Árvore de Decisão

A Árvore de Decisão é um algoritmo que classifica dados como um fluxograma, dividindo-os em grupos menores com base em perguntas sobre seus atributos. Essa estrutura em árvore facilita a interpretação do modelo, revelando quais características são mais importantes para determinar o nível de obesidade.

No nosso modelo, limitamos a profundidade da árvore (max_depth=5) para evitar overfitting e usamos o índice de Gini como critério de divisão. O índice de Gini mede a impureza de um nó, ou seja, o quão misturadas estão as classes. O algoritmo busca a divisão que maximiza a redução da impureza, resultando em subconjuntos mais puros (com exemplos de classes mais semelhantes).

3. Regressão Linear
(Em construção)

# Avaliação dos modelos criados

## Métricas utilizadas

REMOVER APÓS ADICIONAR OS MODELOS: 

<<< ---------
Nesta seção, as métricas utilizadas para avaliar os modelos desenvolvidos deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 
------------ >>>

* Acurácia: Proporção de exemplos classificados corretamente.
* Relatório de Classificação: Inclui precisão, recall e F1-score para cada classe, além das médias macro e ponderada.

A acurácia fornece uma visão geral do desempenho do modelo, enquanto o relatório de classificação detalha o desempenho em cada classe, incluindo métricas como precisão (proporção de verdadeiros positivos entre os classificados como positivos), recall (proporção de verdadeiros positivos entre os positivos reais) e F1-score (média harmônica entre precisão e recall).

## Discussão dos resultados obtidos

REMOVER APÓS ADICIONAR OS MODELOS: 

<<<<< ----------
Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 
------------- >>>>

1. Árvore de Decisão

Nosso modelo de Árvore de Decisão alcançou uma acurácia de 78,5% na validação e 83,6% no teste. O desempenho foi bom na maioria das classes, exceto na classe 1 (obesidade tipo I), indicando a necessidade de melhorias na identificação desse grupo específico.

Os resultados demonstram que a Árvore de Decisão é eficaz na classificação do nível de obesidade, mas apresenta dificuldades na identificação da obesidade tipo I.

2. Regressão Linear
(Em construção)


# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 

# Referências Bibliográficas
ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS). A healthy lifestyle - WHO recommendations. [S.l.: s.n.], 2020. Disponível em: https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations. Acesso em: 12 abr. 2024.
