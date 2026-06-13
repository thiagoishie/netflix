# Netflix Data Analysis

Projeto de análise exploratória do catálogo da Netflix utilizando Python e Pandas.

## Objetivos

* Realizar a extração e limpeza dos dados;
* Aplicar boas práticas de organização de projetos de dados;
* Desenvolver análises exploratórias sobre o catálogo da Netflix;
* Gerar insights relacionados a filmes e séries disponíveis na plataforma.

## Estrutura do projeto

```text
NETFLIX/
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   ├── etl.ipynb
│   └── data_analytics.ipynb
│
├── src/
│   ├── extract.py
│   └── cleaning.py
│
├── requirements.txt
└── README.md
```

## Principais etapas realizadas

* Remoção de colunas sem relevância analítica;
* Tratamento de valores ausentes;
* Correção de inconsistências na coluna `rating`;
* Conversão de tipos de dados;
* Padronização da coluna `duration`;
* Preparação dos dados para análise exploratória.

## Tecnologias utilizadas

* Python
* Pandas
* NumPy
* Jupyter Notebook
* Visual Studio Code

## Dataset

O conjunto de dados utilizado contém informações sobre filmes e séries disponíveis na Netflix, incluindo classificação indicativa, duração, país de origem, elenco e data de inclusão no catálogo.

## Próximos passos

* Desenvolver novas variáveis por meio de feature engineering;
* Realizar análises exploratórias e visualizações;
* Investigar padrões relacionados a gêneros, classificações indicativas e evolução do catálogo ao longo do tempo.
