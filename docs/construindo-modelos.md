# Pergunta orientada a dados

Quais fatores (hábitos alimentares, tabagismo, condição física, etc.) são mais relevantes para prever o nível de obesidade e qual modelo de aprendizado de máquina oferece a melhor performance na previsão, considerando métricas como acurácia, precisão, recall e F1-score?

A pergunta de pesquisa é mais ampla e abrangente, estabelecendo o tema geral da investigação. Ela não se limita aos dados em si, mas sim ao problema que se busca resolver. A pergunta orientada a dados, por outro lado, é mais específica e focada na análise dos dados. Ela busca identificar os padrões e relações presentes nos dados que podem ajudar a responder à pergunta de pesquisa.

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
| Consumo de álcool (CALC) | Categórica ordinal | Não (No), Às vezes (Sometimes), Frequentemente (Frequently), Sempre (Always) |
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
Para validação, optamos por criar o atributo IMC onde faremos manualmente o cálculo do Índice de Massa Corporal = Peso / (Altura x Altura) para verificar se o valor em _NObeyesdad_ classifica corretamente. Consideraremos os intervalos conforme os níveis determinados pela Organização Mundial de Saúde (OMS, 2022). Para os valores de "Overweight Level I e Overweight Level II", chamaremos de Sobrepeso, agregando os níveis 1 e 2.

### Separação de dados
Os dados foram divididos em conjuntos de treinamento (70%), validação (15%) e teste (15%) visando garantir um bom desempenho do modelo.

# Descrição dos modelos

## 1. **Árvore de Decisão**

A Árvore de Decisão é um algoritmo que classifica dados como um fluxograma, dividindo-os em grupos menores com base em perguntas sobre seus atributos. Essa estrutura em árvore facilita a interpretação do modelo, revelando quais características são mais importantes para determinar o nível de obesidade.

- **Nós**: Representam pontos de decisão, onde os dados são divididos com base em um atributo específico.
- **Ramos**: Conectam os nós e representam os possíveis resultados de uma decisão.
- **Folhas**: Representam as classes finais ou valores previstos, indicando o resultado da classificação ou regressão.

### Princípios de Funcionamento:

- **Divisão Recursiva**: A árvore de decisão começa com um nó raiz que contém todos os dados. O algoritmo seleciona o atributo que melhor divide os dados em subconjuntos mais homogêneos em relação à variável alvo. Essa divisão é feita com base em um critério de impureza, como o índice de Gini ou a entropia.
- **Crescimento da Árvore**: O processo de divisão é repetido recursivamente para cada subconjunto de dados, criando novos nós e ramos até que um critério de parada seja atingido. Os critérios de parada podem incluir:
    - Profundidade máxima da árvore (max_depth).
    - Número mínimo de amostras em um nó para permitir uma nova divisão.
    - Limite de impureza.
    - Quando todos os exemplos em um nó pertencem à mesma classe ou quando não há mais atributos para dividir.
- **Predição**: Uma vez que a árvore esteja construída, a classificação de uma nova amostra é feita percorrendo a árvore desde o nó raiz até uma folha, seguindo os ramos de acordo com os valores dos atributos da amostra. A classe ou valor previsto na folha final é a saída do modelo.

### Vantagens:

- Interpretabilidade: A estrutura em árvore facilita a visualização e compreensão do processo de decisão, permitindo identificar quais atributos são mais importantes para a classificação.
- Simplicidade: O algoritmo é relativamente simples de entender e implementar.
- Não requer normalização dos dados: A árvore de decisão não é afetada pela escala dos atributos.

### Limitações:

- Overfitting: Árvores de decisão podem facilmente sofrer de overfitting, especialmente quando a profundidade da árvore não é limitada.
- Instabilidade: Pequenas variações nos dados de treinamento podem levar a árvores de decisão muito diferentes.
- Viés para atributos com muitas categorias: Atributos com muitas categorias podem ter um peso maior na decisão, mesmo que não sejam tão relevantes.

### Justificativa da Escolha:

A árvore de decisão foi escolhida por sua simplicidade, interpretabilidade e capacidade de lidar com dados numéricos e categóricos, características importantes para o problema de classificação do nível de obesidade. Além disso, a árvore de decisão permite identificar os atributos mais relevantes para a previsão, o que pode fornecer insights valiosos sobre os fatores que contribuem para a obesidade.

No nosso modelo, limitamos a profundidade da árvore (max_depth=10) para evitar overfitting e usamos o índice de Gini como critério de divisão. O índice de Gini mede a impureza de um nó, ou seja, o quão misturadas estão as classes. O algoritmo busca a divisão que maximiza a redução da impureza, resultando em subconjuntos mais puros (com exemplos de classes mais semelhantes).

## 2. **Regressão Linear**
(Em construção)

# Avaliação dos modelos criados

## Métricas utilizadas

## 1. **Árvore de Decisão**
Para avaliar o desempenho do modelo, utilizamos as seguintes métricas:

- **Acurácia**: A acurácia mede a proporção de classificações corretas em relação ao total de amostras. É uma métrica importante para ter uma visão geral do desempenho do modelo, mas pode ser enganosa em casos de desequilíbrio de classes.

- **Precisão**: A precisão mede a proporção de verdadeiros positivos (amostras corretamente classificadas como pertencentes a uma classe) em relação ao total de amostras classificadas como pertencentes a essa classe. É uma métrica útil quando o custo de falsos positivos é alto, como em diagnósticos médicos, onde um falso positivo pode levar a tratamentos desnecessários.

- **Recall**: O recall mede a proporção de verdadeiros positivos em relação ao total de amostras que realmente pertencem à classe. É uma métrica importante quando o custo de falsos negativos é alto, como em detecção de fraudes, onde um falso negativo pode significar uma fraude não detectada.

- **F1-Score**: O F1-score é a média harmônica entre precisão e recall, fornecendo um equilíbrio entre as duas métricas. É útil quando se deseja uma métrica única que combine a capacidade do modelo de identificar corretamente os positivos (precisão) e de encontrar todos os positivos (recall).

Sendo assim, o **F1-score** se mostrou uma métrica mais adequada para avaliar o desempenho desse modelo, pois leva em consideração tanto a precisão quanto o recall, buscando um equilíbrio entre a capacidade do modelo de identificar corretamente os diferentes níveis de obesidade e de encontrar todos os casos de cada nível.


## 2. **Regressão Linear**
(em construção)

## Discussão dos resultados obtidos

## 1. **Árvore de Decisão**

**Desempenho Geral**: O modelo de Árvore de Decisão com ```max_depth = 10``` apresentou um desempenho notável na previsão do nível de obesidade com uma acurácia de 89,91% nos dados de validação e 92,11% nos dados de teste, superando os resultados anteriores obtidos com ```max_depth = 5``` (validação 79,18% e teste 85,17%).

**Desempenho por Classe**:
- **Classes com excelente desempenho**: Todas as classes, exceto "Overweight_Level_I", apresentaram valores de F1-score acima de 0,80 em ambos os conjuntos de dados. Isso demonstra que o modelo é altamente eficaz na identificação de indivíduos em todas as categorias de obesidade, com um bom equilíbrio entre precisão e recall.

- **Classe com bom desempenho**: A classe "Overweight_Level_I" também apresentou um bom desempenho, com F1-score de 0.85 na validação e 0.79 no teste. Embora seja ligeiramente inferior às outras classes, o modelo ainda consegue identificar a maioria dos indivíduos nessa categoria com boa precisão.

**Implicações para a Questão de Pesquisa**: Os resultados obtidos com a Árvore de Decisão com ```max_depth = 10``` reforçam a ideia de que é possível prever o nível de obesidade de um indivíduo com alta precisão, considerando os fatores presentes no dataset. Iniciamos os testes com um ```max_depth = 5``` e verificamos que o aumento na profundidade da árvore para ```max_depth = 10``` permitiu ao modelo capturar nuances nos dados que não eram evidentes com uma profundidade menor, melhorando significativamente a capacidade de generalização e a performance em todas as classes.

## 2. **Regressão Linear**
(Em construção)


# Pipeline de pesquisa e análise de dados

O Google Colab foi a plataforma escolhida para conduzir esta pesquisa e análise de dados. O Colab oferece um ambiente de notebook Jupyter hospedado na nuvem, proporcionando acesso gratuito a recursos computacionais, incluindo GPUs, e facilitando a colaboração em projetos de aprendizado de máquina.

As bibliotecas Python utilizadas neste projeto foram:

- ```pandas```: Para manipulação e análise de dados.
- ```scikit-learn```: Para modelagem de aprendizado de máquina (árvore de decisão, validação cruzada, métricas de avaliação).
- ```imblearn```: Para técnicas de balanceamento de classes (SMOTE).
- ```matplotlib```: Para visualização de dados (árvore de decisão).
- ```seaborn```: Para visualização de dados (matriz de confusão).

O pipeline de pesquisa e análise de dados seguiu as seguintes etapas:

1. **Coleta de dados**: O conjunto de dados "Obesity or CVD risk (Classify/Regressor/Cluster)" no formato ```csv``` foi obtido do Kaggle.
2. **Limpeza e pré-processamento**: Os dados foram limpos, outliers foram tratados e transformações foram aplicadas para preparar os dados para a modelagem.
3. **Engenharia de recursos**: Novos recursos foram criados (cálculo do IMC) para avaliar a capacidade preditiva dos modelos.
4. **Divisão dos dados**: Os dados foram divididos em conjuntos de treinamento, validação e teste.
5. **Modelagem**: Modelos de aprendizado de máquina (árvore de decisão, regressão linear) foram treinados e validados.
6. **Avaliação**: O desempenho dos modelos foi avaliado usando métricas como acurácia, precisão, recall e F1-score.
7. **Interpretação**: Os resultados foram interpretados para entender os pontos fortes e fracos dos modelos e identificar oportunidades de melhoria.

# Referências Bibliográficas
ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS). A healthy lifestyle - WHO recommendations. [S.l.: s.n.], 2020. Disponível em: https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations. Acesso em: 12 abr. 2024.
