import React, { useState } from 'react';
import axios from 'axios';
import {
  Container,
  TextField,
  MenuItem,
  FormControl,
  Button,
  Typography,
  Box,
  Grid,
  Paper
} from '@mui/material';

function App() {
  const [inputData, setInputData] = useState({
    Gender: '',
    Age: '',
    Height: '',
    Weight: '',
    family_history_with_overweight: '',
    FAVC: '',
    FCVC: '',
    NCP: '',
    CAEC: '',
    SMOKE: '',
    CH2O: '',
    SCC: '',
    FAF: '',
    TUE: '',
    CALC: '',
    MTRANS: ''
  });
  const [result, setResult] = useState(null);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    let formattedValue = value;

    if (name === 'Height') {
      formattedValue = value.replace(',', '.');
      const validValue = formattedValue.match(/^\d*\.?\d{0,2}$/);
      if (validValue) {
        formattedValue = validValue[0];
      } else {
        formattedValue = inputData.Height;
      }
    } else if (name === 'Weight') {
      formattedValue = value.replace(',', '.');
      const validValue = formattedValue.match(/^\d*\.?\d{0,1}$/);
      if (validValue) {
        formattedValue = validValue[0];
      } else {
        formattedValue = inputData.Weight;
      }
    } else if (name === 'Age') {
      formattedValue = value.replace(/\D/g, '');
    }

    setInputData({ ...inputData, [name]: formattedValue });
  };

  const handlePredict = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', { input_data: inputData });
      setResult(response.data);
    } catch (error) {
      console.error('Erro:', error);
    }
  };

  const labels = {
    Gender: 'Gênero',
    Age: 'Idade',
    Height: 'Altura',
    Weight: 'Peso',
    family_history_with_overweight: 'Histórico familiar de sobrepeso',
    FAVC: 'Consome alimentos ricos em calorias com frequência',
    FCVC: 'Frequência de consumo de vegetais',
    NCP: 'Número de Refeições Principais',
    CAEC: 'Consumo de alimentos entre as refeições',
    SMOKE: 'Tabagismo',
    CH2O: 'Consumo de água diário',
    SCC: 'Monitoramento do consumo de calorias',
    FAF: 'Frequência de atividade física',
    TUE: 'Tempo usando dispositivos tecnológicos',
    CALC: 'Consumo de álcool',
    MTRANS: 'Meio de transporte utilizado'
  };

  const options = {
    Gender: { Male: 'Masculino', Female: 'Feminino' },
    family_history_with_overweight: { Yes: 'Sim', No: 'Não' },
    FAVC: { Yes: 'Sim', No: 'Não' },
    CAEC: { No: 'Não', Sometimes: 'Às vezes', Frequently: 'Frequentemente', Always: 'Sempre' },
    SMOKE: { Yes: 'Sim', No: 'Não' },
    SCC: { Yes: 'Sim', No: 'Não' },
    CALC: { No: 'Não', Sometimes: 'Às vezes', Frequently: 'Frequentemente', Always: 'Sempre' },
    MTRANS: { Public_Transportation: 'Transporte público', Automobile: 'Carro', Walking: 'Andando', Motorbike: 'Moto', Bike: 'Bicicleta' },
    FCVC: [1, 2, 3],
    CH2O: [1, 2, 3],
    NCP: [1, 2, 3, 4],
    FAF: [0, 1, 2, 3],
    TUE: [0, 1, 2]
  };

  const modelTranslations = {
    DecisionTree: 'Árvore de Decisão',
    LogisticRegression: 'Regressão Logística',
    RandomForest: 'Random Forest'
  };

  const predictionTranslations = {
    'Insufficient Weight': 'Baixo peso',
    'Normal Weight': 'Peso normal',
    'Overweight Level I': 'Sobrepeso grau I',
    'Overweight Level II': 'Sobrepeso grau II',
    'Obesity Type I': 'Obesidade grau I',
    'Obesity Type II': 'Obesidade grau II',
    'Obesity Type III': 'Obesidade grau III'
  };

  return (
    <Container maxWidth="sm">
      <Box mt={4}>
        <Typography variant="h4" align="center" gutterBottom>
          Classificação de Nível de Obesidade
        </Typography>
      </Box>
      {Object.keys(inputData).map((key) => (
        <FormControl fullWidth margin="normal" key={key}>
          <TextField
            id={key}
            label={labels[key]}
            name={key}
            value={inputData[key]}
            onChange={handleInputChange}
            type={
              key === 'Age' ? 'number' :
              key === 'Height' || key === 'Weight' ? 'text' :
              'text'
            }
            inputProps={{
              step: key === 'Height' ? '0.01' : key === 'Weight' ? '0.1' : undefined,
            }}
            select={Boolean(options[key])}
          >
            {options[key] && (
              Array.isArray(options[key])
                ? options[key].map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))
                : Object.entries(options[key]).map(([value, label]) => (
                    <MenuItem key={value} value={value}>
                      {label}
                    </MenuItem>
                  ))
            )}
          </TextField>
        </FormControl>
      ))}
      <Box mt={2}>
        <Button variant="contained" color="primary" fullWidth onClick={handlePredict}>
          Classificar
        </Button>
      </Box>
      {result && (
        <>
          <Box mt={4}>
            <Typography variant="h5" align="center" gutterBottom>
              Resultados dos Modelos
            </Typography>
            <Grid container spacing={2}>
              {Object.keys(result).map((modelKey) => (
                modelKey !== 'technical_details' && (
                  <Grid item xs={12} sm={4} key={modelKey}>
                    <Paper elevation={3} style={{ padding: '16px', textAlign: 'center' }}>
                      <Typography variant="h6">Modelo: {modelTranslations[modelKey]}</Typography>
                      <Typography variant="body1">
                        Classe Prevista: {predictionTranslations[result[modelKey]]}
                      </Typography>
                    </Paper>
                  </Grid>
                )
              ))}
            </Grid>
          </Box>
          <Box mt={4}>
            <Typography variant="h5" align="center" gutterBottom>
              Análise Técnica
            </Typography>
            <Paper elevation={3} style={{ padding: '16px' }}>
              <Typography variant="body1">
                {JSON.stringify(result.technical_details, null, 2)}
              </Typography>
            </Paper>
          </Box>
        </>
      )}
    </Container>
  );
}

export default App;
