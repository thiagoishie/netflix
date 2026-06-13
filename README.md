# Netflix Data Analysis

Projeto de análise exploratória do catálogo da Netflix utilizando Python e Pandas, com foco em boas práticas de organização, pipeline de dados e geração de insights.

---

## Objetivos

* Realizar a extração, limpeza e transformação dos dados;
* Aplicar boas práticas de organização de projetos de dados;
* Desenvolver análises exploratórias sobre o catálogo da Netflix;
* Gerar insights relacionados a filmes e séries disponíveis na plataforma;
* Construir um pipeline simples de ETL para separação entre dados brutos e processados.

---

## Estrutura do Projeto

```text
netflix-analysis/
│
├── data/
│   ├── raw/
│   │   └── netflix_titles.csv
│   │
│   └── processed/
│       ├── netflix.csv
│       ├── netflix_directors.csv
│       └── netflix_cast.csv
│
├── notebooks/
│   ├── etl.ipynb
│   └── data_analysis.ipynb
│
├── src/
│   ├── extract.py
│   ├── cleaning.py
│   ├── feature_engineering.py
│   └── load.py
│
├── README.md
│
└── requirements.txt
```

---

## Fluxo do Pipeline

```text
Raw Data
    ↓
Extract
    ↓
Cleaning
    ↓
Feature Engineering
    ↓
Load
    ↓
Processed Data
    ↓
Exploratory Data Analysis
```

---

## Responsabilidade de cada módulo

| Módulo                   | Responsabilidade                                            |
| ------------------------ | ----------------------------------------------------------- |
| `extract.py`             | Leitura dos dados brutos (`data/raw`)                       |
| `cleaning.py`            | Limpeza, tratamento de valores ausentes e padronização      |
| `feature_engineering.py` | Criação de novas features e métricas                        |
| `load.py`                | Orquestração do pipeline e geração dos datasets processados |
| `etl.ipynb`              | Execução do processo de ETL para atualização dos dados      |
| `data_analysis.ipynb`    | Análise exploratória e visualização dos dados               |

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Jupyter Notebook
* Visual Studio Code

---

## Dataset

O conjunto de dados utilizado contém informações sobre filmes e séries disponíveis na Netflix, incluindo classificação indicativa, duração, país de origem, elenco e data de inclusão no catálogo.

---

## Principais etapas realizadas

* Remoção de colunas sem relevância analítica;
* Tratamento de valores ausentes;
* Correção de inconsistências na coluna `rating`;
* Conversão de tipos de dados;
* Padronização da coluna `duration`;
* Criação de novas variáveis por meio de feature engineering;
* Geração de datasets processados para análise.

---

## Datasets Processados

### `netflix.csv`

Tabela principal contendo os títulos da Netflix enriquecidos com as features criadas durante o pipeline.

**Granularidade:** 1 linha = 1 título.

---

### `netflix_directors.csv`

Tabela relacional entre títulos e diretores.

**Granularidade:** 1 linha = 1 diretor por título.

Exemplo:

| title   | director   |
| ------- | ---------- |
| Movie A | Director 1 |
| Movie A | Director 2 |
| Movie B | Director 3 |

---

### `netflix_cast.csv`

Tabela relacional entre títulos e membros do elenco.

**Granularidade:** 1 linha = 1 ator/atriz por título.

Exemplo:

| title   | cast    |
| ------- | ------- |
| Movie A | Actor 1 |
| Movie A | Actor 2 |
| Movie B | Actor 3 |

---

## Colunas do Dataset Original

| Coluna       | Descrição                                 |
| ------------ | ----------------------------------------- |
| show_id      | Identificador único da obra               |
| type         | Tipo do conteúdo (Movie ou TV Show)       |
| title        | Nome do filme ou série                    |
| director     | Diretor(es) associados ao título          |
| cast         | Principais atores e atrizes               |
| country      | País(es) de produção                      |
| date_added   | Data de inclusão no catálogo              |
| release_year | Ano de lançamento                         |
| rating       | Classificação indicativa                  |
| duration     | Duração do conteúdo                       |
| listed_in    | Gêneros originais fornecidos pelo dataset |
| description  | Sinopse da obra                           |

---

## Feature Engineering

### Rating Group

| Grupo   | Ratings                  |
| ------- | ------------------------ |
| Kids    | TV-Y, TV-Y7, TV-Y7-FV, G |
| Family  | TV-G, PG                 |
| Teen    | TV-PG, TV-14, PG-13      |
| Adult   | TV-MA, R, NC-17          |
| Unknown | NR, UR                   |

---

### Release Decade

Agrupamento do ano de lançamento em décadas.

**Exemplo:**

| release_year | release_decade |
| ------------ | -------------- |
| 1994         | 1990           |
| 2001         | 2000           |
| 2019         | 2010           |

---

### Duration Category

#### Movies

| Categoria          | Critério              |
| ------------------ | --------------------- |
| Short Film         | até 40 minutos        |
| Medium-length Film | entre 41 e 70 minutos |
| Feature Film       | acima de 70 minutos   |

#### TV Shows

| Categoria           | Critério             |
| ------------------- | -------------------- |
| Limited Series      | 1 temporada          |
| Short Series        | 2 a 3 temporadas     |
| Long-running Series | 4 ou mais temporadas |

---

### Additional Features

| Feature          | Descrição                                         |
| ---------------- | ------------------------------------------------- |
| `main_country`   | Principal país associado ao título                |
| `continent`      | Continente do país principal                      |
| `language`       | Idioma inferido a partir do país principal        |
| `year_added`     | Ano em que o título foi adicionado à Netflix      |
| `delay_added`    | Diferença entre lançamento e inclusão no catálogo |
| `genre`          | Gênero padronizado                                |
| `n_countries`    | Quantidade de países associados ao título         |
| `n_genres`       | Quantidade de gêneros originais                   |
| `n_cast_members` | Número de membros do elenco                       |
| `n_directors`    | Número de diretores associados                    |

---

## Perguntas de Negócio

Algumas questões que podem ser exploradas com os dados processados:

* Como o catálogo da Netflix evoluiu ao longo das décadas?
* Quais são os gêneros mais frequentes?
* Filmes ou séries predominam na plataforma?
* Qual o perfil etário predominante do catálogo?
* Quais países possuem maior representatividade?
* Quem são os diretores mais presentes no catálogo?
* Quais atores aparecem com maior frequência?
* Existem diferenças entre filmes e séries em relação à duração?

---

## Próximos Passos

* Desenvolver visualizações interativas;
* Construir dashboards em Power BI ou Streamlit;
* Adicionar testes unitários para as funções do pipeline;
* Automatizar a execução do ETL;
* Expandir as análises relacionais utilizando as tabelas auxiliares de diretores e elenco.
