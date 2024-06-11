# Implantação da solução

## Introdução

Na etapa do projeto, o grande objetivo é garantir que o sistema possa processar grandes quantidades de dados em servidores ou serviços remotos. Para tal, a computação em nuvem se mostra eficiente.

## Critérios para Implantação

### 1. Avaliação de Provedores de Serviço em Nuvem

Os principais provedores de serviços em nuvem (AWS, Azure, Google Cloud) foram avaliados. Escolhemos a AWS pela sua ampla gama de serviços gerenciados, suporte a modelos de aprendizado de máquina e escalabilidade robusta. Nos dando a oportunidade de fazer o que é proposto de várias maneiras diferentes.

### 2. Configuração do Ambiente na AWS

#### Passos:

1. **Configuração do DataLake**:
    - O AWS Lake Formation será utilizado para configurar e gerenciar o DataLake, armazenando todos os dados brutos, transformados e modelos.
2. **Configuração de Redes e Armazenamento**:
    - Um VPC será criado para isolar o ambiente de rede.
    - Sub-redes públicas e privadas serão configuradas conforme necessário.
    - O Amazon S3 será utilizado para armazenamento dos dados e modelos.
3. **Configuração de Máquinas Virtuais (EC2)**:
    - Instâncias EC2 serão configuradas para treinamento e implantação do modelo.
    - Instâncias otimizadas para computação (por exemplo, `c5.large`) serão utilizadas.

### 3. Implantação do Modelo

#### Passos:

1. **Amazon S3**: Os dados de entrada e o modelo treinado serão armazenados. ( Exemplo de como os dados serão armazenados, nomes ilustrativos )
    ```bash
    aws s3 mb s3://obesity-dataset-bucket
    aws s3 cp ObesityDataSet.csv s3://obesity-dataset-bucket/
    aws s3 cp model.joblib s3://obesity-dataset-bucket/
    ```

2. **Amazon SageMaker**: O treinamento e a implantação do modelo serão realizados.
    - Uma instância de notebook no SageMaker será criada para treinar o modelo.
    - Após o treinamento, o modelo será implantado como um endpoint no SageMaker.

3. **AWS Lambda e API Gateway**:
    - Uma função Lambda será criada para invocar o endpoint do SageMaker.
    - O API Gateway será configurado para expor a função Lambda como uma API RESTful.

    ```python
    import boto3
    import json

    def lambda_handler(event, context):
        sagemaker = boto3.client('sagemaker-runtime')
        input_data = json.loads(event['body'])
        
        response = sagemaker.invoke_endpoint(
            EndpointName='nome-do-endpoint',
            Body=json.dumps(input_data),
            ContentType='application/json'
        )
        
        result = json.loads(response['Body'].read().decode())
        
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    ```

    ## Endpoint:
   - **URL**: `https://api-gateway-url/{stage}/predict`
   - **Método HTTP**: POST
   - **Header**: `Content-Type: application/json`
   - **Corpo da Requisição (JSON)**:
     ```json
     {
        "Gender": "Male",
        "Age": 30,
        "Height": 1.75,
        "Weight": 70.1,
        "family_history_with_overweight": "Yes",
        "FAVC": "Yes",
        "FCVC": 2,
        "NCP": 3,
        "CAEC": "Sometimes",
        "SMOKE": "No",
        "CH2O": 2,
        "SCC": "Yes",
        "FAF": 1,
        "TUE": 0,
        "CALC": "Sometimes",
        "MTRANS": "Public_Transportation"
     }
    - **Corpo da Resposta (JSON)**:
      ```json
      {
           "DecisionTree": "Normal_Weight",
           "LogisticRegression": "Overweight_Level_I",
           "RandomForest": "Normal_Weight",
           "technical_details": {
               "DecisionTree": {
                   "accuracy": 0.85,
                   "precision": 0.80,
                   "recall": 0.75,
                   "f1-score": 0.88
               },
               "LogisticRegression": {
                   
               },
               "RandomForest": {
                   
               }
      }

5. **Elastic Beanstalk**:
    - O AWS Elastic Beanstalk será usado para implantar e gerenciar a aplicação web que interage com a API.
    - O Beanstalk será configurado para garantir a escalabilidade automática e a alta disponibilidade.

### 4. Planejamento da Capacidade Operacional

#### Modelagem Matemática

A capacidade necessária será calculada com base no número esperado de requisições por segundo, o tempo médio de processamento de cada requisição e a capacidade das instâncias do SageMaker.

#### Simulação do Sistema Computacional

Ferramentas de simulação serão utilizadas para testar a capacidade do sistema sob diferentes cargas de trabalho e ajustar os parâmetros de escalabilidade conforme necessário.

### 5. Monitoramento e Ajuste

#### Passos:

1. **Amazon CloudWatch**: O monitoramento do desempenho do modelo será configurado.
    - Alarmes serão configurados para detectar anomalias ou problemas de desempenho.
    - Métricas como latência, taxa de erro e utilização de CPU/memória serão monitoradas.

2. **Ajuste de Capacidade**: A capacidade do endpoint do SageMaker e das instâncias do Elastic Beanstalk será ajustada com base nos dados de monitoramento.
    - A escalabilidade automática será configurada para ajustar o número de instâncias conforme necessário.

### 6. Testes

#### Testes de Funcionalidade

Solicitações ao endpoint via API Gateway serão enviadas para verificar se o modelo retorna a previsão correta.

```python
import requests

url = 'https://{api-id}.execute-api.{region}.amazonaws.com/{stage}/predict'
data = {
    # Dados de entrada para teste
}

response = requests.post(url, json=data)
print(response.json())
```

#### Testes de Desempenho

Ferramentas como Apache JMeter serão utilizadas para enviar um grande número de requisições ao endpoint e medir o desempenho.

### Documentação do Processo

1. **Configuração da AWS**: Documentar tudo assim que for realizada implementação.
2. **Manutenção e Monitoramento**: Além do monitoramento nativo do BeanStalk e DataLake, podemos monitorar através de métricas personalizadas do CloudWatch.



