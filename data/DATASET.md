# Alzheimer’s Disease Dataset - Análise de Mineração de Dados

<p align="center">
  <img src="https://st4.depositphotos.com/1229718/20031/i/450/depositphotos_200319408-stock-photo-concept-memory-loss-dementia-disease.jpg" alt="Bem-vindo ao seu Ambiente de Desenvolvimento">
</p>

## Descrição do Dataset

Este dataset contém informações de saúde de 2.149 pacientes. Os dados abrangem:

- **Detalhes demográficos**
- **Fatores de estilo de vida**
- **Histórico médico**
- **Medições clínicas**
- **Avaliações cognitivas e funcionais**
- **Sintomas**
- **Diagnóstico da Doença de Alzheimer**

Esses dados são ideais para pesquisadores e cientistas de dados interessados em explorar fatores associados ao Alzheimer, desenvolver modelos preditivos e realizar análises estatísticas.

## Citação do Dataset
```bibtex
@misc{rabie_el_kharoua_2024,
title={Alzheimer's Disease Dataset},
url={https://www.kaggle.com/dsv/8668279},
DOI={10.34740/KAGGLE/DSV/8668279},
publisher={Kaggle},
author={Rabie El Kharoua},
year={2024}
```
## Fonte

O dataset utilizado neste projeto foi retirado de Kaggle, e está disponível para download [aqui](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset?resource=download). 

## Etapas Realizadas

✅ **a) Coletar todos os dados da base escolhida**  
A coleta foi realizada a partir do dataset disponível no Kaggle, conforme mencionado acima. Todos os dados foram baixados e preparados para análise.

✅ **b) Compreender os dados da base escolhida**  
Foi realizado um estudo detalhado sobre as variáveis presentes no dataset, incluindo o significado de cada coluna e o tipo de dados associado. Além disso, foram identificados padrões e informações relevantes para a análise.

✅ **c) Definir os objetivos a serem alcançados com a mineração dos dados da base escolhida**  
O principal objetivo deste trabalho foi aplicar técnicas de mineração de dados para prever o diagnóstico de Doença de Alzheimer a partir dos dados coletados. O intuito foi identificar quais fatores estão mais associados ao desenvolvimento da doença, além de construir modelos preditivos baseados em dados históricos.

✅ **d) Realizar pré-processamento nos dados**  
Foi realizado o pré-processamento nos dados, incluindo as seguintes etapas:
- Limpeza de dados ausentes ou inconsistentes.
- Normalização de variáveis numéricas.
- Conversão de variáveis categóricas em formatos numéricos para melhor desempenho dos modelos de machine learning.
- Divisão dos dados em conjuntos de treinamento e teste.

✅ **e) Aplicar três algoritmos de machine learning para realizar classificação dos dados com objetivos preditivos**  
Três algoritmos de machine learning foram aplicados para realizar a classificação dos dados:

1. **Árvore de Decisão** –  Utilizado para explorar a relação entre as variáveis e as previsões do diagnóstico. A árvore de decisão é interpretável e ajuda a entender como as variáveis influenciam a decisão.

2. **K Vizinhos Mais Próximos (KNN)** – Um modelo simples que classifica os dados com base na proximidade de pontos no espaço de características. O KNN é eficaz para dados com distribuições claras, mas pode ser sensível a ruídos.

3. **Máquinas de Vetores de Suporte (SVM)** –  Aplicadas para encontrar as melhores fronteiras de decisão no conjunto de dados. O SVM é muito eficaz em problemas de classificação binária e pode lidar bem com alta dimensionalidade.

✅ **f) Utilizar três métricas para avaliar o resultado dos três algoritmos e indicar qual foi o melhor**  
As métricas utilizadas para avaliar os resultados dos algoritmos foram:
1. **Acurácia** – Medida da proporção de previsões corretas.
2. **Precisão** – Avaliação de quão preciso é o modelo para identificar casos positivos (Alzheimer).
3. **Recall (Sensibilidade)** – Avaliação de quão bem o modelo identifica todos os casos positivos.
4. **F1 Score** -  Combinação de precisão e recall, sendo uma métrica balanceada que considera tanto falsos positivos quanto falsos negativos.

Após a aplicação dos três algoritmos e a análise das métricas, a **Árvore de Decisão** apresentou o melhor desempenho, com uma boa combinação de precisão e recall, tornando-se a melhor escolha para este problema específico.

## Conclusão

Com base nos resultados dos três algoritmos de machine learning, foi possível identificar que a Árvore de Decisão é o modelo mais adequado para a previsão do diagnóstico de Doença de Alzheimer neste dataset. Este estudo pode ser expandido para incluir outras técnicas e fontes de dados, proporcionando uma base sólida para futuras pesquisas sobre a doença.
