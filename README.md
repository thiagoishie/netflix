# Netflix Data Analysis

Projeto de Ciência de Dados aplicado ao catálogo da Netflix, desenvolvido com foco em **engenharia de dados, análise exploratória, estatística, aprendizado de máquina e análise de redes**.

O projeto utiliza um pipeline modular de ETL para transformar dados brutos em datasets analíticos capazes de sustentar investigações progressivamente mais sofisticadas.

---

## Objetivos

* Construir um pipeline completo de ETL utilizando Python;
* Aplicar boas práticas de organização de projetos de dados;
* Realizar análises exploratórias para compreender a composição do catálogo;
* Desenvolver features analíticas para suportar estudos mais avançados;
* Investigar padrões temporais relacionados à expansão do catálogo;
* Validar hipóteses estatísticas relevantes;
* Aplicar técnicas de Machine Learning não supervisionado;
* Explorar relações entre atores e diretores utilizando Social Network Analysis.

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
├── Future Projects
└── requirements.txt
```

---

## Fluxo do Projeto

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
Exploratory Data Analysis (EDA)
    ↓
Hypothesis Testing
    ↓
Time Series Analysis
    ↓
Machine Learning (Clustering)
    ↓
Social Network Analysis (SNA)
```

---

## Pipeline ETL

O pipeline foi desenvolvido de forma modular, permitindo reutilização de código e expansão futura do projeto.

### Responsabilidade de cada módulo

| Módulo                   | Responsabilidade                                       |
| ------------------------ | ------------------------------------------------------ |
| `extract.py`             | Leitura dos dados brutos                               |
| `cleaning.py`            | Limpeza e tratamento dos dados                         |
| `feature_engineering.py` | Criação de variáveis derivadas                         |
| `load.py`                | Orquestração do pipeline e geração dos datasets finais |
| `etl.ipynb`              | Execução e validação do processo de ETL                |
| `data_analysis.ipynb`    | Desenvolvimento das análises exploratórias             |

---

## Datasets Gerados

### `netflix.csv`

Dataset analítico principal enriquecido com as features desenvolvidas durante o ETL.

**Granularidade:** 1 linha = 1 título.

---

### `netflix_directors.csv`

Tabela relacional contendo a associação entre títulos e diretores.

**Granularidade:** 1 linha = 1 diretor por título.

---

### `netflix_cast.csv`

Tabela relacional contendo a associação entre títulos e atores.

**Granularidade:** 1 linha = 1 ator por título.

---

## Feature Engineering

Durante o processo de transformação foram desenvolvidas diversas variáveis analíticas.

### Perfil do conteúdo

* `rating_group`
* `duration_category`
* `genre`
* `release_decade`

---

### Informações geográficas

* `main_country`
* `continent`
* `language`
* `n_countries`

---

### Informações temporais

* `year_added`
* `delay_added`

---

### Complexidade do conteúdo

* `n_cast_members`
* `n_directors`
* `n_genres`

---

## Exploratory Data Analysis (EDA)

A análise exploratória representa o núcleo inicial do projeto e tem como objetivo compreender a composição e as características do catálogo da Netflix.

### Questões investigadas

* O catálogo é composto majoritariamente por filmes ou séries?
* Como o catálogo evoluiu ao longo do tempo?
* Quais países contribuem mais para o catálogo?
* Quais gêneros predominam?
* O catálogo é formado principalmente por conteúdos recentes ou antigos?
* Filmes e séries apresentam diferenças relevantes em duração?
* Qual é o perfil etário predominante do catálogo?
* Quem são os atores e diretores mais recorrentes?

### Técnicas utilizadas

* Estatísticas descritivas;
* Distribuições univariadas;
* Análises bivariadas;
* Visualizações interativas utilizando Plotly;
* Comparações entre grupos.

---

## Future Engineering

O projeto foi estruturado para evoluir gradualmente, incorporando técnicas cada vez mais sofisticadas de Ciência de Dados utilizando os datasets gerados pelo ETL.

---

### 1. Testes de Hipótese

**Objetivo:** validar estatisticamente padrões identificados durante a EDA.

Possíveis investigações:

* Filmes demoram mais para entrar na Netflix do que séries?
* Séries possuem elencos maiores?
* A estratégia de aquisição mudou após 2020?

Técnicas:

* Mann–Whitney U;
* Kruskal–Wallis;
* Testes t;
* Medidas de tamanho de efeito.

---

### 2. Séries Temporais

**Objetivo:** compreender a evolução do catálogo ao longo do tempo.

Possíveis investigações:

* Como o catálogo cresceu ao longo dos anos?
* Houve períodos de aceleração ou desaceleração?
* Existem padrões sazonais na adição de conteúdos?
* Filmes e séries apresentam comportamentos temporais distintos?

Técnicas:

* Médias móveis;
* Decomposição temporal;
* Análise de tendência;
* Análise de sazonalidade;
* Detecção de outliers.

---

### 3. Machine Learning — Clusterização

**Objetivo:** identificar perfis naturais de conteúdos presentes na Netflix.

Possíveis investigações:

* Existem grupos distintos de títulos?
* Quais características definem cada segmento do catálogo?

Técnicas:

* K-Means;
* PCA;
* Silhouette Score;
* Método do Cotovelo.

---

### 4. Social Network Analysis (SNA)

**Objetivo:** explorar as relações existentes entre profissionais presentes no catálogo.

Possíveis investigações:

* Quais atores ocupam posições estratégicas na rede?
* Existem comunidades bem definidas de colaboração?
* Quais diretores apresentam maior diversidade de parcerias?

Técnicas:

* NetworkX;
* Degree Centrality;
* Betweenness Centrality;
* Eigenvector Centrality;
* Community Detection.

---

### 5. Dashboards Interativos

**Objetivo:** transformar os resultados analíticos em ferramentas acessíveis para comunicação e apoio à tomada de decisão.

Possíveis implementações:

* Streamlit;
* Power BI;
* Plotly Dash.

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Plotly
* Jupyter Notebook
* Visual Studio Code

---

## Conjunto de Dados

O dataset utilizado contém informações sobre filmes e séries disponíveis na Netflix, incluindo:

* tipo do conteúdo;
* elenco;
* direção;
* país de origem;
* data de inclusão no catálogo;
* ano de lançamento;
* classificação indicativa;
* duração;
* gêneros;
* descrição.

---

## Narrativa Analítica do Projeto

```text
O que existe no catálogo?
            ↓
Análise Exploratória (EDA)
            ↓
As diferenças observadas são estatisticamente relevantes?
            ↓
Testes de Hipótese
            ↓
Como o catálogo evoluiu ao longo do tempo?
            ↓
Séries Temporais
            ↓
Existem perfis naturais de conteúdo?
            ↓
Machine Learning (Clusterização)
            ↓
Como os profissionais do catálogo se relacionam?
            ↓
Social Network Analysis
```

---

## Status do Projeto

### Concluído

* [x] Estruturação do projeto;
* [x] Pipeline completo de ETL;
* [x] Limpeza e padronização dos dados;
* [x] Desenvolvimento das features analíticas;
* [x] Geração dos datasets processados;
* [x] Início da Análise Exploratória de Dados (EDA).

### Planejado

* [ ] Conclusão da EDA;
* [ ] Testes de hipótese;
* [ ] Séries temporais;
* [ ] Clusterização;
* [ ] Social Network Analysis;
* [ ] Dashboards interativos.

---

## Licença

Este projeto foi desenvolvido para fins educacionais e de construção de portfólio em Ciência de Dados.
