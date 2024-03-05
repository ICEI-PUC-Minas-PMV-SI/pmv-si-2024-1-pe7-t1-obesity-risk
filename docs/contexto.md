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

Nesta seção, deverão ser descritas outras abordagens identificadas na literatura que foram utilizadas para resolver problemas similares ao problema em questão. Para isso, faça uma pesquisa detalhada e identifique, no mínimo, 3 trabalhos que tenham utilizado dados em contexto similares e então, detalhe: detalhe e contextualize o problema, descreva o _dataset_ utilizado, detalhe quais abordagens/algoritmos foram utilizados (e seus parâmetros), identifique as métricas de avaliação empregadas e fale sobre os resultados obtidos. 

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

# Descrição do _dataset_ selecionado

O conjunto de dados disponível para análise oferece estimativas de níveis de obesidade em indivíduos do México, Peru e Colômbia, focalizando seus hábitos alimentares como fator determinante. Composto por 2111 registros, esse dataset representa reúne informações suficientes para pesquisadores e profissionais da saúde interessados na compreensão e abordagem da obesidade nessas regiões.

Para acessar os dados, os interessados podem utilizar o link: (https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster/data). 

O dataset é composto por 17 atributos que fornecem informações que possibilitam análises detalhadas. A classe variável "Nível de Obesidade" é o ponto focal, permitindo a aplicação de técnicas de classificação, agrupamento ou regressão. As categorias dessa variável incluem Peso Insuficiente, Peso Normal, Sobrepeso Nível I, Sobrepeso Nível II, Obesidade Tipo I, Obesidade Tipo II e Obesidade Tipo III, proporcionando uma segmentação clara dos registros com base nos diferentes estágios de obesidade.

Os atributos apresentados no dataset abrangem uma gama variada de informações, sendo elas:
  - Gênero (masculino ou feminino)
  - Idade
  - Altura
  - Peso
  - Histórico familiar de obesidade (sim ou não)
  - Frequência de consumo de alimentos altamente calóricos (falso ou verdadeiro)
  - Número de refeições principais
  - Consumo de alimentos entre as refeições 
  - Tabagismo (falso ou verdadeiro)
  - Consumo de água por dia
  - Monitoramento do consumo de calorias (sim ou não)
  - Frequência de atividade física
  - Tempo de uso de dispositivos tecnológicos
  - Consumo de álcool
  - Tipo de transporte utilizado
  - Tipo de Obesidade

Apesar da riqueza de informações, é importante notar algumas limitações nos dados, como a ausência de unidades de medida em certos atributos e a falta de clareza sobre a metodologia de medição em alguns casos . Para maximizar a utilidade do dataset, pode-se considerar a necessidade de padronização ou obtenção de informações adicionais.

# Canvas analítico

Nesta seção, você deverá estruturar o seu Canvas Analítico. O Canvas Analítico tem o papel de registrar a organização das ideias e apresentar o modelo de negócio.

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Referências

BRASIL. Ministério da Saúde. Vigitel 2022: Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico. Brasília: Ministério da Saúde, 2023.

Palechor, F. M., & de la Hoz Manotas, A. (2023). Obesity or CVD risk (Classify/Regressor/Cluster) [Conjunto de dados]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/7009925



Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
