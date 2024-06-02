# Pergunta orientada a dados

Qual modelo de aprendizado de máquina oferece a melhor performance na previsão, considerando métricas como acurácia, precisão, recall e F1-score?

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

# Outras bases de dados úteis
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

## 2. **Regressão Logística**
A regressão logística é um algoritmo de aprendizagem supervisionada usado para modelar a probabilidade de uma variável dependente categórica. Isto é particularmente útil quando a variável alvo é binária, mas também pode ser estendido a problemas de classificação multiclasse. O objetivo é encontrar a melhor combinação de variáveis ​​independentes para prever a probabilidade de ocorrência de um evento específico.

**Estrutura da Regressão Logística:**

- Variável Dependente (y): A variável categórica que queremos prever.
- Variáveis Independentes (X): As variáveis usadas para fazer a previsão.
- Coeficientes (β): Pesos atribuídos a cada variável independente que determinam a contribuição de cada uma para a probabilidade de um evento.

**Princípios de Funcionamento**
1. ![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/assets/40677663/dae3372d-1196-4e1b-bf08-0ccd6c4f9854)
2. Ajuste de Coeficientes: O ajuste dos coeficientes é feito através da maximização da função de verossimilhança, que mede o quão bem o modelo se ajusta aos dados observados.
3. Predição: Após o ajuste do modelo, as previsões para novas amostras são feitas calculando a probabilidade do evento de interesse e classificando-as com base em um limiar definido (geralmente 0.5).

**Vantagens:**
1. Interpretação probabilística: A regressão logística fornece as probabilidades associadas à ocorrência de um evento e permite a interpretação direta dos resultados.
2. Flexibilidade: Pode trabalhar com problemas binários e multiclasses.
3. Eficiência: Funciona bem quando existe uma relação linear entre a variável independente e a função logit da variável dependente.

**Limitações**

1. Relacionamento linear na função logit: Uma relação linear é assumida entre  a função logit das variáveis ​​independentes e dependentes.
2. Multicolinearidade: Altas correlações entre variáveis ​​independentes podem distorcer os resultados.
3. Sensibilidade a valores discrepantes: valores discrepantes podem afetar significativamente o modelo e os coeficientes.
   
**Justificativa da Escolha**

A regressão logística foi escolhida devido à sua capacidade de modelar probabilidades e lidar com variáveis ​​​​categóricas, tornando-a ideal para problemas de classificação, como a previsão de níveis de obesidade. A sua simplicidade, eficácia e interpretabilidade permitem-nos compreender o impacto de cada variável independente na variável dependente, fornecendo assim informação valiosa sobre intervenções e estratégias de saúde.  O uso da regressão logística é particularmente adequado para resolver este problema porque queremos prever categorias de obesidade com base em vários fatores e compreender a probabilidade de cada pessoa se enquadrar em uma determinada categoria.

## 3. **Random Forest**
O Random Forest é um algoritmo de aprendizado de máquina amplamente utilizado devido à sua robustez e eficácia em diversas aplicações. Este algoritmo, que pertence à família dos métodos de ensemble, combina múltiplos modelos de aprendizado para melhorar a precisão das previsões e reduzir a possibilidade de overfitting. 
O princípio básico do Random Forest é a construção de várias árvores de decisão durante o processo de treinamento. Cada uma dessas árvores é treinada em diferentes subconjuntos dos dados de treinamento, criados através de um método conhecido como bootstrap, onde os dados são amostrados com reposição. Esse processo garante que cada árvore seja treinada em uma amostra ligeiramente diferente, introduzindo variabilidade no modelo. Além disso, para cada nó de cada árvore, é selecionado um subconjunto aleatório de características (features). Esta seleção aleatória de características garante que cada árvore seja construída com base em diferentes atributos, aumentando a diversidade entre as árvores e reduzindo a correlação entre elas. Ao fazer previsões, o Random Forest combina as previsões de todas as árvores: para problemas de classificação, a decisão final é baseada na votação majoritária (a classe mais votada); para problemas de regressão, a previsão final é a média das previsões de todas as árvores.

As vantagens do Random Forest são diversas. Primeiramente, ele é eficaz na redução do overfitting, um problema comum em árvores de decisão individuais. Devido ao processo de bootstrap e à seleção aleatória de características, as árvores são menos correlacionadas entre si, o que resulta em um modelo mais generalizável. Além disso, o Random Forest é robusto a outliers e dados ruidosos. Enquanto árvores individuais podem ser sensíveis a essas irregularidades, a combinação de muitas árvores reduz seu impacto.
Outro ponto forte do Random Forest é sua versatilidade. Ele pode ser utilizado tanto para problemas de classificação quanto de regressão e funciona bem com grandes conjuntos de dados e um alto número de características. A capacidade do Random Forest de calcular a importância das características permite aos usuários entender quais variáveis são mais influentes nas previsões do modelo. Além disso, comparado a outros algoritmos, o Random Forest requer menos ajuste de hiperparâmetros para alcançar um bom desempenho, tornando-o mais acessível para usuários com diferentes níveis de experiência em aprendizado de máquina.

Uma das principais do Random Forest desvantagens é a complexidade e o tempo de treinamento, que podem ser elevados, especialmente quando há um grande número de árvores e/ou características. Esse aspecto pode ser um impedimento em aplicações que exigem treinamento rápido. Além disso, as previsões podem ser lentas devido ao grande número de árvores, o que pode ser problemático em situações que demandam respostas em tempo real.
Outro desafio é a interpretabilidade do modelo. Embora o Random Forest forneça a importância das características, o modelo final é considerado uma "caixa preta". As árvores individuais são interpretáveis, mas a combinação de muitas árvores torna a interpretação do modelo final mais complexa. Além disso, o Random Forest pode consumir uma quantidade significativa de memória, especialmente quando aplicado a grandes conjuntos de dados, o que pode limitar seu uso em ambientes com recursos computacionais restritos.

# Avaliação dos modelos criados

## Métricas utilizadas

## 1. **Árvore de Decisão**
Para avaliar o desempenho do modelo, utilizamos as seguintes métricas:

- **Acurácia**: A acurácia mede a proporção de classificações corretas em relação ao total de amostras. É uma métrica importante para ter uma visão geral do desempenho do modelo, mas pode ser enganosa em casos de desequilíbrio de classes.

- **Precisão**: A precisão mede a proporção de verdadeiros positivos (amostras corretamente classificadas como pertencentes a uma classe) em relação ao total de amostras classificadas como pertencentes a essa classe. É uma métrica útil quando o custo de falsos positivos é alto, como em diagnósticos médicos, onde um falso positivo pode levar a tratamentos desnecessários.

- **Recall**: O recall mede a proporção de verdadeiros positivos em relação ao total de amostras que realmente pertencem à classe. É uma métrica importante quando o custo de falsos negativos é alto, como em detecção de fraudes, onde um falso negativo pode significar uma fraude não detectada.

- **F1-Score**: O F1-score é a média harmônica entre precisão e recall, fornecendo um equilíbrio entre as duas métricas. É útil quando se deseja uma métrica única que combine a capacidade do modelo de identificar corretamente os positivos (precisão) e de encontrar todos os positivos (recall).

Sendo assim, o **F1-score** se mostrou uma métrica mais adequada para avaliar o desempenho desse modelo, pois leva em consideração tanto a precisão quanto o recall, buscando um equilíbrio entre a capacidade do modelo de identificar corretamente os diferentes níveis de obesidade e de encontrar todos os casos de cada nível.

## 2. **Regressão Logística **
As duas principais métricas de avaliação de desempenho são utilizadas para medir a eficácia do modelo de Regressão Logística: Accuracy Score e Classification Report.
1. Accuracy Score: é uma métrica de avaliação que indica a proporção de previsões corretas feitas pelo modelo em relação ao número total de previsões.
2. Classification Report: fornece uma análise detalhada do desempenho do modelo de classificação, incluindo diversas métricas para cada categoria:
    - Precision para cada classe: A taxa de verdadeiros positivos entre as previsões feitas para cada classe.
    - Recall para cada classe: A taxa de verdadeiros positivos entre as instâncias reais de cada classe.
    - F1-Score para cada classe: A média harmônica entre precision e recall, que combina ambas as métricas em uma única medida.
    - Support: O número de ocorrências de cada classe no conjunto de dados de teste.

Nos testes realizados de classificação de nível de obesidade, F1-score é a métrica mais adequada. O F1-score fornece uma única métrica que considera tanto a precision quanto o recall, oferecendo um bom equilíbrio entre evitar falsos positivos e falsos negativos.

## 3. **Random Forest**
Foram utilizadas aqui as mesmas métricas empregadas para o modelo Árvore de Decisão, além das métricas a seguir:

- **Support**: O número de instâncias verdadeiras de cada classe no conjunto de teste.
- **Macro Avg (Média Macro)**: A média macro calcula a média das métricas sem considerar o suporte (número de instâncias em cada classe). Isso significa que cada classe contribui igualmente para a média final, independentemente do número de instâncias.
- **Weighted Avg (Média Ponderada)**: A média ponderada calcula a média das métricas considerando o suporte, ou seja, cada classe contribui para a média final proporcionalmente ao seu número de instâncias.

As métricas em questão foram calculadas a partir de uma **Matriz de Confusão**, também conhecida como tabela de contingência, e que permite a visualização do desempenho de um modelo de classificação, comparando as previsões do modelo com os valores reais dos dados.

## Discussão dos resultados obtidos

## 1. **Árvore de Decisão**

**Desempenho Geral**: O modelo de Árvore de Decisão com ```max_depth = 10``` apresentou um desempenho notável na previsão do nível de obesidade com uma acurácia de 89,91% nos dados de validação e 92,11% nos dados de teste, superando os resultados anteriores obtidos com ```max_depth = 5``` (validação 79,18% e teste 85,17%). Observando a matriz de confusão, observamos que a árvore com ```max_depth = 10``` teve um melhor desempenho que a árvore com ```max_depth = 5``` para diferenciar "Overweight_Level_I" de "Overweight_Level_II".

**Desempenho por Classe**:
- **Classes com excelente desempenho**: Todas as classes, exceto "Overweight_Level_I", apresentaram valores de F1-score acima de 0,80 em ambos os conjuntos de dados. Isso demonstra que o modelo é altamente eficaz na identificação de indivíduos em todas as categorias de obesidade, com um bom equilíbrio entre precisão e recall.

- **Classe com bom desempenho**: A classe "Overweight_Level_I" também apresentou um bom desempenho, com F1-score de 0.85 na validação e 0.79 no teste. Embora seja ligeiramente inferior às outras classes, o modelo ainda consegue identificar a maioria dos indivíduos nessa categoria com boa precisão.

**Implicações para a Questão de Pesquisa**: Os resultados obtidos com a Árvore de Decisão com ```max_depth = 10``` reforçam a ideia de que é possível prever o nível de obesidade de um indivíduo com alta precisão, considerando os fatores presentes no dataset. Iniciamos os testes com um ```max_depth = 5``` e verificamos que o aumento na profundidade da árvore para ```max_depth = 10``` permitiu ao modelo capturar nuances nos dados que não eram evidentes com uma profundidade menor, melhorando significativamente a capacidade de generalização e a performance em todas as classes.

## 2. **Regressão Logística**
O modelo de regressão logística apresentou forte desempenho  na predição da obesidade, com 85% de acerto nos dados de validação e 83% nos dados dos testes. O uso de técnicas de pré-processamento como  imputação de valores faltantes, codificação de variáveis ​​categóricas e balanceamento de classes pelo SMOTE contribuíram significativamente para esses resultados. A precisão do modelo é consistente e mostra boa  generalização.

**Desempenho por Classe:**
1. Classes de alto desempenho: a maioria das classes apresenta valores de pontuação F1 acima de 0,80 em conjuntos de dados de validação e teste. Isso mostra que o modelo pode identificar efetivamente pessoas em diferentes categorias de obesidade, mantendo um bom equilíbrio entre precisão  e sensibilidade (recall).
2.  Classe com bom desempenho: algumas classes têm desempenho um pouco pior, com pontuações na F1 variando de 0,75 a 0,80. Contudo, o modelo foi capaz de identificar corretamente a maioria das pessoas nessas categorias, com precisão aceitável.

  **Implicações para a questão de pesquisa:**
   
   Os resultados obtidos com a regressão logística mostram que é possível prever o nível de obesidade do indivíduo com alta precisão utilizando os fatores presentes no conjunto de dados. Uma análise detalhada do relatório de classificação mostra que o modelo é capaz de distinguir eficazmente entre diferentes níveis de obesidade. A precisão de 85% dos dados de validação sugere que o modelo generaliza bem  e pode ser aplicado em ambientes práticos para  previsão de obesidade. O uso do SMOTE para equilibrar as classes garantiu  um forte desempenho do modelo, mesmo em classes sub-representadas. Este aspecto é essencial para a aplicabilidade prática do modelo, pois garante que todas as classes de obesidade sejam consideradas da mesma forma. Em resumo, a regressão logística, combinada com técnicas apropriadas de pré-processamento, foi eficaz na previsão do nível de obesidade, proporcionando assim uma ferramenta valiosa para intervenção precoce e estratégias de saúde pública.
## 3. **Random Forest**

O modelo apresenta um desempenho muito bom no conjunto de teste, com uma alta acurácia de 0.95, para ```max_depth = 10```.  A maioria das classes tem precisão, revocação e F1-Score elevadas, indicando que o modelo está bem ajustado e generaliza bem para novos dados. A única classe com desempenho ligeiramente inferior é a Classe 1, "Normal_Weight" , mas ainda assim, suas métricas são bastante aceitáveis. No geral, o modelo parece bem equilibrado e eficaz na classificação das instâncias.

![image 00](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/blob/main/docs/img/Random%20Forest.jpg)

A matriz de confusão fornecida é resultado da avaliação de um modelo de classificação para sete classes diferentes. 

Classe 0 (Insufficient_Weight): O modelo classificou corretamente 54 instâncias da classe 0. No entanto, errou duas instâncias da classe 1 como classe 0 (falsos negativos). 

Classe 1 (Normal_Weight): O modelo classificou corretamente 57 instâncias da classe 1. No entanto, errou uma instância da classe 0 como classe 1 (falso positivo), três instâncias da classe 5 como classe 1 (falsos negativos) e uma instância da classe 6 como classe 1 (falso negativo). 

Classe 2 (Obesity_Type_I): O modelo classificou corretamente 74 instâncias da classe 2. No entanto, errou duas instâncias da classe 3 como classe 2 (falsos negativos) e duas instâncias da classe 6 como classe 2 (falsos positivos). 

Classe 3 (Obesity_Type_II): O modelo classificou corretamente 57 instâncias da classe 3. No entanto, errou uma instância da classe 2 como classe 3 (falso negativo). 

Classe 4 (Obesity_Type_III): O modelo classificou corretamente 63 instâncias da classe 4 e não houve erros em outras classes. Não é necessário fazer correções para esta classe, pois o modelo obteve um desempenho perfeito.

Classe 5 (Overweight_Level_I): O modelo classificou corretamente 49 instâncias da classe 5. No entanto, errou seis instâncias da classe 1 como classe 5 (falsos positivos) e uma instância da classe 6 como classe 5 (falso negativo). 

Classe 6 (Overweight_Level_II): O modelo classificou corretamente 48 instâncias da classe 6 e não houve erros em outras classes. Não é necessário fazer correções para esta classe, pois o modelo obteve um desempenho perfeito.

**Teste das profundidades máximas**

Treinar um modelo Random Forest com várias profundidades máximas (max depth) é uma prática comum para encontrar o melhor ajuste para o conjunto de dados. Isso pode ser feito utilizando a técnica de validação cruzada para avaliar o desempenho do modelo em diferentes valores de profundidade máxima.
Através do gráfico abaixo, é possível perceber que, a partir da profundidade 10 adiante, a acurácia do modelo se estabiliza acima de 90%. Já os testes com profundidade inferior a 10 mostram uma queda acentuada na acurácia.

![image 01](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/blob/main/src/Max%20depth.jpg)

**Curva de Aprendizado**

A curva de aprendizado é uma ferramenta gráfica que ajuda a entender a performance de um modelo de aprendizado de máquina à medida que a quantidade de dados de treinamento aumenta. Ela pode fornecer dados importantes sobre se o modelo está sofrendo de overfitting ou underfitting e ajudar a identificar oportunidades para melhorar o desempenho do modelo. Em geral, se as curvas de treinamento e validação/teste convergem, isso é indicativo de uma performance aceitável, na qual o modelo está se generalizando bem. A curva de aprendizado mostrada abaixo demontra convergência entre as curvas.

![image 02](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/blob/main/src/Curva%20de%20Aprendizado.jpg)

**Resultados com amostras de teste variáveis**

Os resultados indicam a acurácia do modelo Random Forest em diferentes conjuntos de teste, onde o tamanho do conjunto de teste é variado. 

- Acurácia do modelo Random Forest com conjunto de teste de 10.0%: 0.9387

Isso indica que, quando 10% dos dados foram retidos como conjunto de teste, o modelo classificou corretamente cerca de 93.87% das amostras de teste.

- Acurácia do modelo Random Forest com conjunto de teste de 30.0%: 0.9322

Isso indica que, quando 30% dos dados foram retidos como conjunto de teste, o modelo classificou corretamente cerca de 93.22% das amostras de teste.

- Acurácia do modelo Random Forest com conjunto de teste de 50.0%: 0.9347

Isso indica que, quando 50% dos dados foram retidos como conjunto de teste, o modelo classificou corretamente cerca de 93.47% das amostras de teste.

Esses resultados sugerem que a acurácia do modelo é consistente em diferentes tamanhos de conjunto de teste, o que é um bom sinal de que o modelo está generalizando bem para diferentes amostras de teste. No entanto, é importante lembrar que a acurácia por si só pode não ser suficiente para avaliar completamente a performance de um modelo. Desse modo, outras métricas foram consideradas, conforme imagem abaixo, e mais uma vez a consistência do modelo foi demonstrada.

Portanto, a partir dos testes realizados, é possível concluir que o modelo de classificação Random Forest funciona bem com o dataset utilizado.

![image 03](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/blob/main/src/Varia%C3%A7%C3%A3o%20de%20testes.jpg)

### Pipeline de Pesquisa e Análise de Dados

O Google Colab foi a plataforma escolhida para conduzir esta pesquisa e análise de dados. O Colab oferece um ambiente de notebook Jupyter hospedado na nuvem, proporcionando acesso gratuito a recursos computacionais, incluindo GPUs, e facilitando a colaboração em projetos de aprendizado de máquina.

As bibliotecas Python utilizadas neste projeto foram:

- **pandas**: Para manipulação e análise de dados.
- **scikit-learn**: Para modelagem de aprendizado de máquina (árvore de decisão, validação cruzada, métricas de avaliação).
- **imblearn**: Para técnicas de balanceamento de classes (SMOTE).
- **matplotlib**: Para visualização de dados (árvore de decisão).
- **seaborn**: Para visualização de dados (matriz de confusão).
- **sklearn**: Para algoritmos adicionais de aprendizado de máquina e funções utilitárias.
- **scikit-lib**: Para métodos avançados de modelagem e análise.

O pipeline de pesquisa e análise de dados seguiu as seguintes etapas:

1. **Coleta de dados**: O conjunto de dados "Obesity or CVD risk (Classify/Regressor/Cluster)" no formato csv foi obtido do Kaggle.
2. **Limpeza e pré-processamento**: Os dados foram limpos, outliers foram tratados e transformações foram aplicadas para preparar os dados para a modelagem.
3. **Engenharia de recursos**: Novos recursos foram criados (cálculo do IMC) para avaliar a capacidade preditiva dos modelos.
4. **Divisão dos dados**: Os dados foram divididos em conjuntos de treinamento, validação e teste.
5. **Modelagem**: Modelos de aprendizado de máquina (árvore de decisão, regressão linear) foram treinados e validados.
6. **Avaliação**: O desempenho dos modelos foi avaliado usando métricas como acurácia, precisão, recall e F1-score.
7. **Interpretação**: Os resultados foram interpretados para entender os pontos fortes e fracos dos modelos e identificar oportunidades de melhoria.

### Pipeline de Execução Visual

![image 04](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/blob/main/src/pipeline.png)

### Descrição das Etapas

- **Coleta de dados**: Importar os dados do Kaggle e carregar no Google Colab.
- **Limpeza e pré-processamento**: Remover valores ausentes, tratar outliers e aplicar transformações necessárias.
- **Engenharia de recursos**: Criar novos atributos como o IMC e preparar os dados para a modelagem.
- **Divisão dos dados**: Separar os dados em conjuntos de treinamento, validação e teste.
- **Modelagem**: Treinar modelos de aprendizado de máquina utilizando as bibliotecas scikit-learn e sklearn.
- **Avaliação**: Avaliar o desempenho dos modelos utilizando métricas como acurácia, precisão, recall e F1-score.
- **Interpretação**: Analisar os resultados para identificar pontos fortes e fracos dos modelos e propor melhorias.

# Códigos
- Árvore de Decisão: https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/blob/b6fb6cc676026948cee326b888d306e31315fbd4/src/obesity_dataset_decision_tree_classifier_max_depth_10.py
- Random Forest: https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/blob/main/src/random_forest.py

# Vídeos demonstrando os algoritmos
- Árvore de Decisão: https://youtu.be/js_gml6jU7g
- Random Forest: https://www.youtube.com/watch?v=80l1Im9ZdfI

# Referências Bibliográficas
ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS). A healthy lifestyle - WHO recommendations. [S.l.: s.n.], 2020. Disponível em: https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations. Acesso em: 12 abr. 2024.
