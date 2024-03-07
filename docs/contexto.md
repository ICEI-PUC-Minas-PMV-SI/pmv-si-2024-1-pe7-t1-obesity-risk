# Introdução

**BERNARDO - PREENCHEREI ESSA PARTE AO FINAL**: *Texto descritivo introdutório apresentando a visão geral do projeto a ser desenvolvido considerando o contexto em que ele se insere, os objetivos gerais, a justificativa e o público-alvo do projeto.*

## Problema

A obesidade é um problema de saúde pública de grande importância no Brasil, afetando mais de um quinto da população adulta. Segundo dados da última pesquisa Vigitel, realizada em 2022, 20,3% dos brasileiros com 18 anos ou mais estão obesos. Isso significa que mais de 40 milhões de pessoas estão acima do peso ideal, o que aumenta significativamente o risco de desenvolver doenças crônicas como diabetes, hipertensão e doenças cardíacas. Entre os principais fatores de risco estão a má alimentação, a falta de atividade física e o sedentarismo.

O dataset que utilizaremos em nossa pesquisa contém estimativas dos níveis de obesidade em pessoas dos países do México, Peru e Colômbia, com idades entre 14 e 61 anos, considerando seus hábitos alimentares, tabagismo e condição física.

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

A escolha deste projeto se justifica pela crescente prevalência da obesidade globalmente, impactando significativamente a saúde pública. A obesidade está associada a várias doenças crônicas, como diabetes tipo 2, doenças cardiovasculares e certos tipos de câncer, representando um fardo significativo para os sistemas de saúde. Além disso, entender os fatores de risco e como eles interagem para influenciar os níveis de obesidade pode ajudar no desenvolvimento de estratégias preventivas e intervenções mais eficazes.

A análise detalhada deste dataset, que inclui dados de hábitos alimentares, condição física e dados demográficos de indivíduos de países diferentes, oferece uma oportunidade única de investigar as possíveis causas da obesidade em contextos culturais e geográficos específicos. Isso pode isso pode gerar insights importantes sobre como abordagens personalizadas para prevenção e tratamento podem ser mais eficazes em diferentes populações.

## Público-Alvo

Descreva quem serão as pessoas que poderão se beneficiar com a sua investigação indicando os diferentes perfis. O objetivo aqui não é definir quem serão os clientes ou quais serão os papéis dos usuários na aplicação. A ideia é, dentro do possível, conhecer um pouco mais sobre o perfil dos usuários: conhecimentos prévios, relação com a tecnologia, relações hierárquicas, etc.

Adicione informações sobre o público-alvo por meio de uma descrição textual, diagramas de personas e mapa de stakeholders.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)

## Estado da arte
  A prevalência de obesidade na população jovem é um desafio crescente para a saúde pública global. Com impactos físicos, emocionais e sociais significativos, é crucial compreender suas razões e métodos de intervenção. Nesta situação, esta análise do estado atual examina os principais fatores de risco, ações e políticas de saúde pública relacionadas à obesidade entre adolescentes.
  
1- Os fatores de risco envolvidos na obesidade no adolescente: uma revisão integrativa

 1-1 Contexto:
O texto apresenta um resumo de um estudo sobre os fatores de risco para o desenvolvimento da obesidade na adolescência, realizado por meio de uma revisão integrativa da literatura. A pesquisa teve como objetivo identificar e compreender os fatores que contribuem para o aumento da obesidade entre adolescentes, analisando aspectos biológicos, sociais, psicológicos e nutricionais. O estudo também teve como objetivo analisar propostas de intervenção e estratégias de prevenção da obesidade nessa faixa etária.

 1-2 Detalhes do Dataset:
Os 25 artigos selecionados foram selecionados a partir das bases de dados da Biblioteca Virtual em Saúde (BVS) e do EBSCOhost. Os textos abordaram diversos temas ligados à obesidade na adolescência, como fatores de risco, consequências para a saúde, impacto social e econômico, além de propostas de intervenção e prevenção.

 1-3 Medidas e resultados:
As métricas usadas no estudo incluíram a análise dos fatores de risco para obesidade na adolescência, como hábitos alimentares, níveis de atividade física, influência genética, condições socioeconômicas e culturais, dentre outros. Os resultados evidenciaram uma variedade de elementos interligados que contribuem para o aumento da obesidade nessa faixa etária.
Os resultados destacados são:
Identificação de fatores biológicos, sociais, psicológicos e nutricionais que contribuem para o excesso de peso na adolescência.
Falta de consenso sobre os riscos e benefícios relacionados à obesidade, dificultando recomendações baseadas em evidências.
Medidas para a mudança dos hábitos alimentares, controle de peso e aumento da atividade física.
Reconhecer a escola como um ambiente propício para a promoção da saúde e prevenção da obesidade.
Precisamos lidar com as táticas de marketing da indústria alimentícia que promovem alimentos processados ricos em gordura e açúcar.
Os resultados reforçam a relevância de abordagens integradas e multidisciplinares para lidar com o problema da obesidade na adolescência, envolvendo famílias, escolas, profissionais de saúde e políticas públicas de saúde.

2- Obesidade abdominal como fator de risco para doenças cardiovasculares

 2-1  Contexto
O contexto abordado nos textos diz respeito à relação entre obesidade abdominal e doenças cardiovasculares (DCV)
Diversas pesquisas destacam a obesidade abdominal como um fator de risco significativo para o surgimento de enfermidades cardiovasculares.
A obesidade abdominal é considerada uma epidemia global e um dos principais problemas de saúde da atualidade.
Há uma preocupação crescente com a chegada cada vez mais precoce de doenças cardiovasculares em jovens.

 2-2  Dataset 
O estudo se baseou em uma revisão de textos científicos em língua portuguesa, predominantemente nos últimos 10 anos (2010-2020) Foram empregadas as bases de dados LILACS, MEDLINE e SciELO para pesquisar artigos com os termos "Obesidade abdominal", "Doenças Cardiovasculares" e "Circunferência Abdominal". Essa abordagem permitiu uma avaliação atualizada e abrangente da conexão entre obesidade abdominal e enfermidades cardiovasculares.

 2-3  Medidas e resultados:
Os textos mencionam diversas pesquisas que utilizaram medidas como a circunferência abdominal e a prevalência de obesidade abdominal para avaliar o risco de contrair doenças cardiovasculares.
São citados os resultados de estudos realizados em diferentes regiões do Brasil, que mostram uma grande incidência de obesidade abdominal em diversas populações.
Os resultados também são mencionados, sugerindo que a obesidade abdominal em jovens e adolescentes é um fator de risco para o surgimento de enfermidades cardiovasculares na fase adulta.
Chegou-se à conclusão de que a obesidade abdominal é um fator de risco que pode ser modificado, enfatizando a relevância de incentivar a adoção de um estilo de vida mais saudável para prevenir o surgimento de enfermidades cardiovasculares.

3- Simultaneidade de comportamentos de risco para a obesidade em adultos das capitais do Brasil

 3-1 Contexto
O propósito do estudo é examinar a conexão entre a simultaneidade de comportamentos de risco e a obesidade em indivíduos com idades entre 18 e 59 anos em cidades brasileiras. Os comportamentos de risco incluem inatividade física, tempo prolongado sentado, consumo excessivo de doces e carnes vermelhas gordurosas ou frango com pele.

 3-2 Dataset 
O estudo é transversal e com base na população, contando com 35.448 indivíduos entrevistados por telefone. As variáveis autorrelatadas são obesidade, definida pelo índice de massa corporal (IMC ≥ 30 kg/m2), e os comportamentos de risco mencionados anteriormente. O calendário é composto pelos resultados dessas entrevistas e dados sociodemográficos dos participantes.

 3-3 Medidas e resultados:
As avaliações foram conduzidas por meio de regressões de Poisson e logística multinomial, levando em conta fatores sociodemográficos. Nos homens, o consumo de carnes gordurosas, o tempo desperdiçado sentado e a inatividade física, assim como a presença dos quatro comportamentos de risco, estão relacionados significativamente à obesidade. Nas mulheres, o consumo simultâneo de doces e carnes gordurosas também se associou ao final. Obesidade aumentou com o aumento do número de comportamentos de risco em ambos os sexos.

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

Nesta seção, você deverá estruturar o seu Canvas Analítico. O Canvas Analítico tem o papel de registrar a organização das ideias e apresentar o modelo de negócio.

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Referências

BRASIL. Ministério da Saúde. Vigitel 2022: Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico. Brasília: Ministério da Saúde, 2023.

Palechor, F. M., & de la Hoz Manotas, A. (2023). Obesity or CVD risk (Classify/Regressor/Cluster) [Conjunto de dados]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/7009925

Os fatores de risco envolvidos na obesidade no adolescente: uma revisão integrativa. https://www.scielo.br/j/csc/a/YJBwJkN9H7Z8GbBKX5j7m8C/#

Obesidade abdominal como fator de risco para doenças cardiovasculares. https://ojs.brazilianjournals.com.br/ojs/index.php/BJHR/article/view/18306/14782

Simultaneidade de comportamentos de risco para a obesidade em adultos das capitais do Brasil. https://www.scielosp.org/pdf/csc/v25n8/1413-8123-csc-25-08-2999.pdf

Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
