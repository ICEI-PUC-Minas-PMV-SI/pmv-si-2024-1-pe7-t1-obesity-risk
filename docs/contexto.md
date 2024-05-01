# Introdução

A obesidade configura-se como um desafio de saúde pública de proporções globais. De acordo com dados da Organização Mundial da Saúde (OMS), mais de 1 bilhão de adultos estão acima do peso, dos quais 650 milhões são obesos (OMS, 2023). Diante de tamanho desafio, soluções tecnológicas podem somar para mitigar os efeitos deletérios desse desafio. Este projeto visa desenvolver modelos de aprendizado de máquina para classificar, identificar fatores de risco, prever mudanças nos níveis de obesidade e segmentar dados.

## Problema

A obesidade é um problema de saúde pública de grande importância no Brasil, afetando mais de um quinto da população adulta. Segundo dados da última pesquisa Vigitel, realizada em 2022, 20,3% dos brasileiros com 18 anos ou mais estão obesos (Ministério da Saúde, 2023). Isso significa que mais de 40 milhões de pessoas estão acima do peso ideal, o que aumenta significativamente o risco de desenvolver doenças crônicas como diabetes, hipertensão e doenças cardíacas. Entre os principais fatores de risco estão a má alimentação, a falta de atividade física e o sedentarismo.

O dataset que utilizaremos em nossa pesquisa contém estimativas dos níveis de obesidade em pessoas dos países do México, Peru e Colômbia, com idades entre 14 e 61 anos, considerando seus hábitos alimentares, tabagismo e condição física (Palechor & De la Hoz Manotas, 2023).

O contexto de aplicação desta pesquisa não inclui uma empresa parceira ou tecnologias específicas neste momento, mas pode ser direcionado para áreas como saúde pública, nutrição e políticas de bem-estar.

## Questão de pesquisa

A pergunta central que motiva esta pesquisa é:
- Com que precisão é possível prever o nível de obesidade de de um indivíduo levando em consideração diversos fatores como hábitos alimentares, tabagismo e condição física?

## Objetivos preliminares

**Classificar os Níveis de Obesidade:** Utilizar os dados coletados para desenvolver um modelo de aprendizado de máquina capaz de classificar corretamente os níveis de obesidade (Sobrepeso, Normal, Obesidade I, II e III) com base nos hábitos alimentares, condição física e dados demográficos (idade, gênero, altura e peso) dos indivíduos.

**Identificar Fatores de Risco:** Analisar os atributos relacionados aos hábitos alimentares e à condição física para identificar os principais fatores de risco associados aos diferentes níveis de obesidade. Isso inclui a frequência de consumo de alimentos calóricos, o consumo de vegetais, o número de refeições principais, o consumo de álcool, entre outros.

**Prever Mudanças nos Níveis de Obesidade:** Desenvolver um modelo preditivo que possa estimar mudanças nos níveis de obesidade com base em alterações nos hábitos alimentares e de atividade física. Esse modelo ajudará a entender como intervenções específicas podem impactar os níveis de obesidade.

**Segmentação de Dados para Intervenções Personalizadas:** Usar técnicas de segmentação para identificar grupos específicos dentro da população estudada que possam se beneficiar mais de intervenções direcionadas, baseadas em seus hábitos alimentares e níveis de atividade física.


## Justificativa

A escolha deste projeto se justifica pela crescente prevalência da obesidade globalmente, impactando significativamente a saúde pública. Segundo a Organização Mundial da Saúde (OMS), a obesidade tornou-se uma epidemia global, com a prevalência triplicando desde 1975 (OMS, 2023). Em 2016, mais de 1,9 bilhão de adultos, acima de 18 anos, estavam com sobrepeso. Destes, mais de 650 milhões eram obesos (OMS, 2023). Esta tendência é alarmante e representa um desafio substancial para os sistemas de saúde em todo o mundo.

Além disso, a obesidade está associada a várias doenças crônicas, como diabetes tipo 2, doenças cardiovasculares, hipertensão arterial e certos tipos de câncer. Os dados do Centers for Disease Control and Prevention (CDC) mostram que a obesidade é um fator de risco significativo para essas condições de saúde adversas (CDC, 2023).

Os custos diretos e indiretos associados à obesidade representam uma parcela significativa dos gastos com saúde em muitos países. Por exemplo, nos Estados Unidos, estima-se que os custos médicos diretos da obesidade tenham atingido US$ 147 bilhões em 2008, de acordo com a Organização para a Cooperação e Desenvolvimento Econômico (OCDE, 2010).

Entender os fatores de risco e como eles interagem para influenciar os níveis de obesidade é crucial para o desenvolvimento de estratégias preventivas e intervenções mais eficazes. Uma revisão abrangente publicada no JAMA Network Open analisou dados de 195 países entre 1980 e 2015 e concluiu que o aumento da disponibilidade de alimentos processados, juntamente com mudanças nos estilos de vida, contribuiu significativamente para o aumento da obesidade global (NCD-RisC, 2016).

A análise detalhada deste dataset, que inclui dados de hábitos alimentares, condição física e dados demográficos de indivíduos de países diferentes, oferece uma oportunidade única de investigar as possíveis causas da obesidade em contextos culturais e geográficos específicos. Isso pode gerar insights importantes sobre como abordagens personalizadas para prevenção e tratamento podem ser mais eficazes em diferentes populações. Estudos recentes, como aqueles conduzidos pelo Instituto Nacional de Saúde dos Estados Unidos (NIH), demonstraram a eficácia de intervenções personalizadas que levam em consideração fatores genéticos, metabólicos e comportamentais na prevenção e tratamento da obesidade (NIH, 2023).

## Público-Alvo
O público-alvo deste projeto é diversificado e abrange diferentes perfis que podem se beneficiar das análises e conclusões resultantes da pesquisa sobre obesidade. Esses perfis incluem:

1. Profissionais da Saúde:
   Médicos, nutricionistas, psicólogos, educadores físicos e outros profissionais da saúde interessados em compreender melhor os fatores que contribuem para a obesidade.

2. Pesquisadores e Acadêmicos:
   Pesquisadores das áreas de saúde, nutrição, epidemiologia, medicina preventiva e ciência de dados interessados em explorar novas abordagens para o estudo da obesidade.
Estudantes universitários em busca de dados e informações para trabalhos acadêmicos, dissertações e teses relacionadas à obesidade e saúde pública.

3. Organizações Governamentais e Não Governamentais:
   Ministérios da Saúde, Secretarias de Saúde e órgãos responsáveis pela formulação e implementação de políticas de saúde.
ONGs e instituições dedicadas à promoção da saúde e bem-estar, interessadas em estratégias eficazes de prevenção e controle da obesidade.

4. Indivíduos e Famílias:
   Pessoas que buscam informações sobre prevenção e tratamento da obesidade para melhorar sua saúde e qualidade de vida.
Famílias preocupadas com a saúde de seus membros, interessadas em adotar hábitos alimentares e estilo de vida mais saudáveis.

## Estado da arte

A prevalência da obesidade entre os jovens é um desafio crescente para a saúde pública global. Para efeitos físicos, emocionais e sociais significativos, é importante compreender as suas causas e mecanismos. A este respeito, esta actual revisão do estado da arte examina os factores de risco, intervenções e políticas de saúde pública mais importantes associados à obesidade nos jovens.

### 1. Fatores de risco para obesidade adolescente
  
1.1 Antecedentes: Os fatores de risco para obesidade em jovens foram investigados em uma revisão integrada da literatura. Os estudos analisaram os aspectos biológicos, sociais, psicológicos e nutricionais que contribuem para o aumento da obesidade nessa faixa etária. 
 
 1.2 Algoritmos de aprendizado de máquina e métricas de avaliação: Os estudos revisados ​​descobriram que vários usam algoritmos de aprendizado de máquina, como regressão logística. , Árvores de Decisão, Redes Neurais Artificiais e Máquinas de Vetores de Suporte (SVM). As métricas de avaliação mais comuns foram acurácia, sensibilidade, especificidade, área sob a curva ROC (AUC) e pontuação F1.  
 
 1.3 Resultados: Os estudos mostraram que a regressão logística e as árvores de decisão foram amplamente utilizadas e apresentaram bons resultados na classificação dos fatores de risco. obesidade na adolescência. A precisão e as pontuações F1 foram as métricas mais utilizadas para avaliar o desempenho do modelo, com uma taxa média de sucesso em torno de 80%.

### 2. Tabagismo
   
 2.1 Antecedentes: A revisão da literatura examinou a relação entre tabagismo e obesidade, considerando o seu impacto na saúde pública.
 
 2.2 Algoritmos de aprendizado de máquina e ferramentas de avaliação: Dentre os estudos analisados, os algoritmos mais comuns foram: Regressão logística, Análise discriminante linear e. Floresta aleatória. As métricas de avaliação incluíram precisão, sensibilidade, especificidade e AUC. 
 
 2.3. Resultados: Os modelos construídos mostraram que o Random Forest obteve os melhores resultados na identificação da associação entre tabagismo e obesidade. A precisão média foi de 85% e a AUC foi de 0,90, indicando uma boa capacidade de distinguir entre fumantes obesos e não fumantes.

### 3. Obesidade abdominal como fator de risco para doenças cardiovasculares
   
 3.1 Contexto: O estudo investigou a relação entre obesidade abdominal e doenças cardiovasculares com o objetivo de identificar os fatores de risco mais importantes. 
 
 3.2 Algoritmos de aprendizado de máquina e métricas de avaliação: Os algoritmos mais utilizados foram a regressão logística. , redes neurais artificiais e máquinas de vetores de suporte (SVM). As medidas de avaliação incluíram precisão, sensibilidade, especificidade, precisão e AUC. 
 
 3.3 Resultados: Os resultados mostraram que a regressão logística foi o algoritmo mais eficaz para prever o risco cardiovascular associado à obesidade abdominal. A precisão média foi de 82% e AUC. de 0,88. As redes neurais artificiais também apresentaram bons resultados com precisão média de 80% e AUC de 0,85. Este texto fornece uma visão geral da pesquisa realizada e descreve os algoritmos de aprendizado de máquina utilizados, as medidas de avaliação utilizadas e os resultados de cada tópico abordado.

# Descrição do _dataset_ selecionado

O conjunto de dados disponível para análise oferece estimativas de níveis de obesidade em indivíduos do México, Peru e Colômbia, focalizando seus hábitos alimentares como fator determinante. Composto por 2111 registros, esse dataset representa reúne informações suficientes para pesquisadores e profissionais da saúde interessados na compreensão e abordagem da obesidade nessas regiões.

Para acessar os dados, os interessados podem utilizar o link: (https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster/data). 

O dataset é composto por 17 atributos que fornecem informações que possibilitam análises detalhadas. A classe variável "Nível de Obesidade" é o ponto focal, permitindo a aplicação de técnicas de classificação, agrupamento ou regressão. As categorias dessa variável incluem Peso Insuficiente, Peso Normal, Sobrepeso Nível I, Sobrepeso Nível II, Obesidade Tipo I, Obesidade Tipo II e Obesidade Tipo III, proporcionando uma segmentação clara dos registros com base nos diferentes estágios de obesidade.

Os atributos apresentados no dataset abrangem uma gama variada de informações, sendo elas derivadas das seguintes perguntas:
  - Qual é o seu gênero? String (masculino ou feminino)
  - Qual é a sua idade? Decimal (valor numérico inteiro)
  - Qual é a sua altura? Decimal (valor numérico em metros)
  - Qual é o seu peso? Decimal (valor numérico em quilogramas)
  - Você possui familiar que sofreu ou sofre com excesso de peso? Boolean (sim ou não)
  - Você come alimentos altamente calóricos com frequência? Boolean (sim ou não)
  - Você costuma comer vegetais nas suas refeições? Decimal (1 - Nunca, 2 - As vezes, 3 - Sempre)
  - Quantas refeições principais você faz diariamente? Decimal (valor numérico inteiro)
  - Você come algum alimento entre as refeições? String (sempre, frequentemente, as vezes, não) 
  - Você fuma? Boolean (falso ou verdadeiro)
  - Quanto você bebe de água por dia? Decimal (1 - menos de um litro, 2 - entre um e dois litros, 3 - mais de dois litros)
  - Você monitora seu consumo diário de calorias? Boolean (sim ou não)
  - Com que frequência você pratica atividade física? Decimal (0 - não pratico, 1 - um ou dois dias, 2 - dois ou quatro 
    dias, 3 - quatro ou cinco dias) 
  - Quanto tempo você passa utilizando dispositivos tecnológicos como celular, videogame, televisão, computador e outros? 
    Decimal (0 - de 0 a duas horas, 1 - de três a cinco horas, 2 - mais de cinco horas)
  - Com que frequência você bebe álcool? String (não bebo, as vezes, frequentemente, sempre)
  - Que tipo de transporte você normalmente utiliza? String (automóvel, moto, bicicleta, transporte público, caminhada)
  - Nível de Obesidade - String (Peso Insuficiente, Peso Normal, Sobrepeso Nível I, Sobrepeso Nível II, Obesidade Tipo I, 
    Obesidade Tipo II e Obesidade Tipo III)

As perguntas da pesquisa e mais informações podem ser encontradas neste artigo que publica o conjunto de dados: https://www.sciencedirect.com/science/article/pii/S2352340919306985#tbl1

# Canvas analítico

![Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/assets/78939209/742c928c-2a28-4258-8936-e67f3922622f)

# Referências

ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS). Obesidade e sobrepeso. https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight (acessado em 8 de março de 2024).

BRASIL. Ministério da Saúde. Vigitel 2022: Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico. Brasília: Ministério da Saúde, 2023.

PALECHOR, F. M.; DE LA HOZ MANOTAS, A. Obesity or CVD risk (Classify/Regressor/Cluster) [Conjunto de dados]. Kaggle, 2023. Disponível em: https://doi.org/10.34740/KAGGLE/DSV/7009925. Acesso em: 8 mar. 2024.

NEVES, S. C. et al.. Os fatores de risco envolvidos na obesidade no adolescente: uma revisão integrativa. Ciência & Saúde Coletiva, v. 26, p. 4871–4884, out. 2021.

ALBUQUERQUE, F. L. S. et al. Obesidade abdominal como fator de risco para doenças cardiovasculares / Abdominal obesity as a risk factor for cardiovascular diseases. Brazilian Journal of Health Review, v. 3, n. 5, p. 14529-14536, 2020. DOI: 10.34119/bjhrv3n5-248.

STREB, A. R. et al. Simultaneidade de comportamentos de risco para a obesidade em adultos das capitais do Brasil [Simultaneity of risk behaviors for obesity in adults in the capitals of Brazil]. Ciência & Saúde Coletiva, Rio de Janeiro, v. 25, n. 8, p. 2999-3007, ago. 2020. DOI: 10.1590/1413-81232020258.27752018.

CENTERS FOR DISEASE CONTROL AND PREVENTION (CDC). Adult Obesity Facts. Atlanta, GA: US Department of Health and Human Services, Centers for Disease Control and Prevention, 2023. Disponível em: https://www.cdc.gov/obesity/data/adult.html. Acesso em: 08 abr. 2024.

ORGANIZAÇÃO PARA A COOPERAÇÃO E DESENVOLVIMENTO ECONÔMICO (OCDE). Obesity and the economics of prevention: Fit not fat. Paris: OECD Publishing, 2010. Disponível em: https://www.oecd.org/health/health-systems/obesityandtheeconomicsofpreventionfitnotfat.htm. Acesso em: 08 abr. 2024.

NCD RISK FACTOR COLLABORATION (NCD-RISC). Global, Regional, and National Prevalence of Overweight and Obesity in Children and Adults During 1980–2015: A Systematic Analysis of Population-Based Survey Data. JAMA Network Open. 2016;3(9):e1610130. doi:10.1001/jamanetworkopen.2016.10130. Disponível em: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2729879. Acesso em: 08 abr. 2024.

NATIONAL INSTITUTES OF HEALTH (NIH). Personalized Diets May Improve Health More Than Traditional Advice. National Institutes of Health (NIH). 2023. Disponível em: https://www.nih.gov/news-events/nih-research-matters/personalized-diets-may-improve-health-more-traditional-advice. Acesso em: 08 abr. 2024.
