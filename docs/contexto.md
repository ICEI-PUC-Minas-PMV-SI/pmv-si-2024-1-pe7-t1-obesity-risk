# Introdução

A obesidade configura-se como um desafio de saúde pública de proporções globais. De acordo com dados da Organização Mundial da Saúde (OMS) de 2023, mais de 1 bilhão de adultos estão acima do peso, dos quais 650 milhões são obesos. Diante de tamanho desafio, soluções tecnológicas podem somar para mitigar os efeitos deletérios desse desafio. Este projeto visa desenvolver modelos de aprendizado de máquina para classificar, identificar fatores de risco, prever mudanças nos níveis de obesidade e segmentar dados visando intervenções personalizadas com base em hábitos alimentares, condição física e dados demográficos. O público-alvo inclui profissionais da saúde, pesquisadores, órgãos governamentais e indivíduos interessados em melhorar sua saúde e qualidade de vida.

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

A escolha deste projeto se justifica pela crescente prevalência da obesidade globalmente, impactando significativamente a saúde pública. Segundo a Organização Mundial da Saúde (OMS), a obesidade tornou-se uma epidemia global, com a prevalência triplicando desde 1975. Em 2016, mais de 1,9 bilhão de adultos, acima de 18 anos, estavam com sobrepeso. Destes, mais de 650 milhões eram obesos. Esta tendência é alarmante e representa um desafio substancial para os sistemas de saúde em todo o mundo. (Fonte: OMS - https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)

Além disso, a obesidade está associada a várias doenças crônicas, como diabetes tipo 2, doenças cardiovasculares, hipertensão arterial e certos tipos de câncer. Os dados do Centers for Disease Control and Prevention (CDC) mostram que a obesidade é um fator de risco significativo para essas condições de saúde adversas. (Fonte: CDC - https://www.cdc.gov/obesity/data/adult.html)

Os custos diretos e indiretos associados à obesidade representam uma parcela significativa dos gastos com saúde em muitos países. Por exemplo, nos Estados Unidos, estima-se que os custos médicos diretos da obesidade tenham atingido US$ 147 bilhões em 2008, de acordo com a Organização para a Cooperação e Desenvolvimento Econômico (OCDE). (Fonte: OCDE - https://www.oecd.org/health/health-systems/obesityandtheeconomicsofpreventionfitnotfat.htm)

Entender os fatores de risco e como eles interagem para influenciar os níveis de obesidade é crucial para o desenvolvimento de estratégias preventivas e intervenções mais eficazes. Uma revisão abrangente publicada no JAMA Network Open analisou dados de 195 países entre 1980 e 2015 e concluiu que o aumento da disponibilidade de alimentos processados, juntamente com mudanças nos estilos de vida, contribuiu significativamente para o aumento da obesidade global. (Fonte: JAMA Network Open - https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2729879)

A análise detalhada deste dataset, que inclui dados de hábitos alimentares, condição física e dados demográficos de indivíduos de países diferentes, oferece uma oportunidade única de investigar as possíveis causas da obesidade em contextos culturais e geográficos específicos. Isso pode gerar insights importantes sobre como abordagens personalizadas para prevenção e tratamento podem ser mais eficazes em diferentes populações. Estudos recentes, como aqueles conduzidos pelo Instituto Nacional de Saúde dos Estados Unidos (NIH), demonstraram a eficácia de intervenções personalizadas que levam em consideração fatores genéticos, metabólicos e comportamentais na prevenção e tratamento da obesidade. (Fonte: NIH - https://www.nih.gov/news-events/nih-research-matters/personalized-diets-may-improve-health-more-traditional-advice)

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

![Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-obesity-risk/assets/78939209/742c928c-2a28-4258-8936-e67f3922622f)

# Referências

ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS). Obesidade e sobrepeso. https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight (acessado em 8 de março de 2024).

BRASIL. Ministério da Saúde. Vigitel 2022: Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico. Brasília: Ministério da Saúde, 2023.

PALECHOR, F. M.; DE LA HOZ MANOTAS, A. Obesity or CVD risk (Classify/Regressor/Cluster) [Conjunto de dados]. Kaggle, 2023. Disponível em: https://doi.org/10.34740/KAGGLE/DSV/7009925. Acesso em: 8 mar. 2024.

NEVES, S. C. et al.. Os fatores de risco envolvidos na obesidade no adolescente: uma revisão integrativa. Ciência & Saúde Coletiva, v. 26, p. 4871–4884, out. 2021.

ALBUQUERQUE, F. L. S. et al. Obesidade abdominal como fator de risco para doenças cardiovasculares / Abdominal obesity as a risk factor for cardiovascular diseases. Brazilian Journal of Health Review, v. 3, n. 5, p. 14529-14536, 2020. DOI: 10.34119/bjhrv3n5-248.

STREB, A. R. et al. Simultaneidade de comportamentos de risco para a obesidade em adultos das capitais do Brasil [Simultaneity of risk behaviors for obesity in adults in the capitals of Brazil]. Ciência & Saúde Coletiva, Rio de Janeiro, v. 25, n. 8, p. 2999-3007, ago. 2020. DOI: 10.1590/1413-81232020258.27752018.
