<p align="center">
  <img src="image/netflix_logo.png" width="500">
</p>

<h1 align="center">
Netflix Content Analytics
</h1>

<p align="center">
Projeto de Data Science utilizando o catálogo da Netflix para análises exploratórias, testes de hipóteses, séries temporais e clustering.
</p>

# Netflix Data Analysis

Projeto de Ciência de Dados aplicado ao catálogo da Netflix, com foco em transformar dados brutos em uma base analítica para exploração, validação estatística e modelagem. O fluxo foi organizado em etapas de ETL e análises progressivas, com entregáveis em notebooks e scripts Python. 

## Visão geral

O pipeline do projeto segue esta lógica:

**dados brutos → ETL → base tratada → EDA → testes de hipótese → série temporal → clustering**

Os arquivos de ETL estão organizados em:
- `extract.py`
- `cleaning.py`
- `feature_engineering.py`
- `load.py` 

## ETL

A etapa de ETL faz a leitura, limpeza, padronização e enriquecimento do dataset.  
Ela gera a base principal `netflix.csv` e também duas tabelas relacionais:
- `netflix_directors.csv`
- `netflix_cast.csv` 

## EDA

A análise exploratória foi concentrada no notebook `01_ETL_EDA.ipynb` e responde, de forma objetiva, às seguintes perguntas:
- O catálogo é composto majoritariamente por filmes ou séries?
- Como o catálogo cresceu ao longo do tempo?
- Quais países contribuem mais para o catálogo?
- Quais gêneros predominam?
- O catálogo é formado principalmente por conteúdos recentes ou antigos? :contentReference[oaicite:3]{index=3}

## Próximas etapas

Os próximos projetos do roadmap são:
- teste de hipótese;
- série temporal;
- clustering. 

## Estrutura do repositório

- `01_ETL_EDA.ipynb`
- `02_Hypothesis_Test.ipynb`
- `03_TimeSeries.ipynb`
- `04_Cluestering.ipynb`
- `src/`
- `data/` 

## Objetivo final

Construir um portfólio end-to-end de Ciência de Dados, mostrando domínio de ETL, análise exploratória, estatística e machine learning não supervisionado. 