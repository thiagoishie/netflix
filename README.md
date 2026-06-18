# Netflix Data Analysis

Projeto de Ciência de Dados aplicado ao catálogo da Netflix, desenvolvido com foco em **engenharia de dados, análise exploratória, estatística, aprendizado de máquina e análise de redes sociais**.

O projeto utiliza um pipeline modular de ETL para transformar dados brutos em datasets analíticos capazes de sustentar investigações progressivamente mais sofisticadas.

---

## 📌 Objetivos do Projeto

- Construir um pipeline completo de ETL utilizando Python;
- Aplicar boas práticas de organização de projetos de dados;
- Realizar análises exploratórias para compreender a composição do catálogo da Netflix;
- Desenvolver features analíticas para suportar estudos mais avançados;
- Investigar padrões temporais relacionados à expansão do catálogo;
- Validar hipóteses estatísticas relevantes;
- Aplicar técnicas de Machine Learning não supervisionado;
- Explorar relações entre atores e diretores utilizando Social Network Analysis (SNA).

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- SciPy
- Scikit-Learn
- Plotly
- NetworkX
- Jupyter Notebook
- Git e GitHub

---

## 📂 Estrutura do Projeto

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
│   ├── ETL_EDA.ipynb
│   ├── Hypothesis_Test.ipynb
│   └── TimeSeries.ipynb
│
├── src/
│   ├── extract.py
│   ├── cleaning.py
│   ├── feature_engineering.py
│   └── load.py
│
├── README.md
└── requirements.txt
```

---

## 🔄 Fluxo do Projeto

```text
Dados Brutos
      ↓
Extract
      ↓
Cleaning
      ↓
Feature Engineering
      ↓
Load
      ↓
Dados Processados
      ↓
Análise Exploratória (EDA)
      ↓
Testes de Hipótese
      ↓
Séries Temporais
      ↓
Machine Learning (Clusterização)
      ↓
Social Network Analysis (SNA)
```

---

# ⚙️ Pipeline ETL

O pipeline foi desenvolvido de forma modular, permitindo reutilização de código e expansão futura do projeto.

## Responsabilidade de cada módulo

| Módulo | Responsabilidade |
|---------|------------------|
| `extract.py` | Leitura dos dados brutos |
| `cleaning.py` | Limpeza e tratamento dos dados |
| `feature_engineering.py` | Criação de variáveis derivadas |
| `load.py` | Orquestração do pipeline e geração dos datasets finais |

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

# 🧠 Engenharia de Features

Durante o processo de transformação foram desenvolvidas diversas variáveis analíticas.

## Perfil do conteúdo

- `rating_group`
- `duration_category`
- `genre`
- `release_decade`

## Informações geográficas

- `main_country`
- `continent`
- `language`
- `n_countries`

## Informações temporais

- `year_added`
- `delay_added`

## Complexidade do conteúdo

- `n_cast_members`
- `n_directors`
- `n_genres`

---

# 📊 Análise Exploratória de Dados (EDA)

A EDA representa a etapa inicial da investigação e tem como objetivo compreender a composição e as características do catálogo da Netflix.

## Questões investigadas

- O catálogo é composto majoritariamente por filmes ou séries?
- Como o catálogo cresceu ao longo do tempo?
- Quais países contribuem mais para o catálogo?
- Quais gêneros predominam?
- O catálogo é formado principalmente por conteúdos recentes ou antigos?
- Filmes e séries apresentam diferenças relevantes em duração?
- Qual é o perfil etário predominante do catálogo?
- Existem diferenças na composição do elenco entre filmes e séries?

## Técnicas utilizadas

- Estatísticas descritivas;
- Análises univariadas;
- Análises bivariadas;
- Visualizações utilizando Plotly;
- Comparações entre grupos.

---

# 🧪 Testes de Hipótese

## Objetivo

Validar estatisticamente padrões identificados durante a EDA.

## Hipóteses avaliadas

- Séries são adicionadas à Netflix mais rapidamente do que filmes?
- Filmes destinados a públicos diferentes apresentam durações distintas?
- Séries possuem elencos maiores do que filmes?
- A estratégia de aquisição da Netflix mudou após 2020?

## Técnicas utilizadas

- Mann–Whitney U;
- ANOVA;
- Kruskal–Wallis;
- Medidas de tamanho de efeito.

---

# 📈 Séries Temporais

## Objetivo

Compreender a evolução do catálogo ao longo do tempo.

## Questões investigadas

- O catálogo cresceu continuamente?
- Houve aceleração ou desaceleração no ritmo de expansão?
- Filmes e séries apresentam padrões temporais distintos?
- Existem períodos anômalos que merecem investigação?

## Técnicas utilizadas

- Agregações semanais;
- Médias móveis;
- Análise de tendência;
- Investigação de sazonalidade;
- Detecção de anomalias.

---

# 🤖 Machine Learning — Clusterização

## Objetivo

Identificar perfis naturais de conteúdos presentes na Netflix.

## Variáveis utilizadas

- `type`
- `main_country`
- `continent`
- `release_year`
- `delay_added`
- `rating_group`
- `duration_category`
- `n_directors`
- `n_cast_members`
- `n_genres`

## Técnicas utilizadas

- StandardScaler;
- One-Hot Encoding;
- Método do Cotovelo;
- Silhouette Score;
- K-Means;
- PCA.

---

# 🕸️ Social Network Analysis (SNA)

## Objetivo

Explorar relações entre profissionais presentes no catálogo.

## Rede principal

### Rede de co-participação entre atores

- **Nó:** ator;
- **Aresta:** dois atores participaram do mesmo título.

## Métricas avaliadas

- Degree Centrality;
- Betweenness Centrality;
- Eigenvector Centrality;
- Clustering Coefficient.

## Questões investigadas

- Quais atores ocupam posições estratégicas na rede?
- Existem comunidades bem definidas?
- Quais profissionais apresentam maior influência dentro do catálogo?

---

# 📌 Status do Projeto

## ✅ Concluído

### Pipeline ETL

- [x] Desenvolvimento do módulo de extração;
- [x] Limpeza e padronização dos dados;
- [x] Correção de inconsistências;
- [x] Geração dos datasets processados;
- [x] Construção das tabelas relacionais.

### Engenharia de Features

- [x] Variáveis de classificação indicativa;
- [x] Variáveis geográficas;
- [x] Variáveis temporais;
- [x] Variáveis de duração;
- [x] Métricas de complexidade.

### Documentação

- [x] Estruturação do repositório;
- [x] Documentação do pipeline;
- [x] Descrição dos datasets;
- [x] Definição do roadmap analítico.

### Análise

- [x] Desenvolvimento da EDA inicial;
- [x] Produção das primeiras visualizações;
- [x] Levantamento de hipóteses de negócio.

---

## 🚧 Em andamento

- [ ] Conclusão da EDA;
- [ ] Testes de hipótese;
- [ ] Séries temporais;
- [ ] Refinamento da comunicação dos resultados.

---

## 📋 Próximas etapas

- [ ] Clusterização dos conteúdos;
- [ ] Social Network Analysis;
- [ ] Rede bipartida ator–diretor;
- [ ] Dashboard interativo;
- [ ] Publicação da versão final do projeto.

---

# 📚 Conjunto de Dados

O dataset utilizado contém informações sobre filmes e séries disponíveis na Netflix, incluindo:

- tipo do conteúdo;
- elenco;
- direção;
- país de origem;
- data de inclusão no catálogo;
- ano de lançamento;
- classificação indicativa;
- duração;
- gêneros;
- descrição.

Fonte: Netflix Titles Dataset.

---

# 👨‍💻 Autor

**Thiago**

Analista de Dados Pleno no Itaú Unibanco, com formação em Economia pela UNIFESP e MBA em Data Science e Analytics pela ESALQ/USP.

Atualmente, desenvolve projetos end-to-end em Ciência de Dados com foco em estatística aplicada, aprendizado de máquina e geração de insights para tomada de decisão baseada em dados.

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais, construção de portfólio e demonstração de competências em Ciência de Dados.