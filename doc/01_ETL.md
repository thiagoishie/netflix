# Documentação Técnica — Pipeline ETL

## Visão Geral

O objetivo do pipeline ETL é transformar o dataset bruto da Netflix em uma base analítica estruturada para suportar análises exploratórias, testes estatísticos, séries temporais e algoritmos de Machine Learning.

O processo foi desenvolvido de forma modular, permitindo manutenção, reutilização de código e expansão futura.

---

# Fluxo do ETL

```text
Netflix Titles Dataset
          │
          ▼
    extract.py
          │
          ▼
    cleaning.py
          │
          ▼
feature_engineering.py
          │
          ▼
      load.py
          │
          ▼
Dados Processados
```

---

# Estrutura dos Arquivos

```text
src/
│
├── extract.py
├── cleaning.py
├── feature_engineering.py
└── load.py
```

---

# 1. Extract

Arquivo:

```python
extract.py
```

Responsável pela leitura dos dados brutos.

## Função

### read_csv()

```python
read_csv(path)
```

Lê o arquivo CSV original e retorna um DataFrame Pandas.

### Entrada

```text
data/raw/netflix_titles.csv
```

### Saída

```text
DataFrame bruto
```

---

# 2. Cleaning

Arquivo:

```python
cleaning.py
```

Responsável pela limpeza, padronização e correção de inconsistências do dataset.

---

## Função

### clean_netflix()

```python
clean_netflix(df)
```

---

## Etapas executadas

### Remoção de colunas irrelevantes

A coluna:

```text
show_id
```

foi removida por não possuir valor analítico.

---

### Tratamento de valores ausentes

#### Director

```python
Not Informed
```

#### Cast

```python
Not Informed
```

#### Country

```python
Unknown
```

---

### Conversão de datas

A coluna:

```text
date_added
```

é convertida para datetime.

---

### Correção de registros inconsistentes

Foram identificadas três linhas onde o valor de rating havia sido deslocado para a coluna duration.

Registros corrigidos:

```text
5541
5794
5813
```

---

### Tratamento de rating ausente

Valores ausentes foram substituídos por:

```text
UR
```

(Unrated)

---

### Conversão de tipos

As colunas:

```python
type
rating
```

são convertidas para categoria.

---

### Padronização da duração

Exemplos:

```text
90 min
```

↓

```text
90
```

```text
3 Seasons
```

↓

```text
3
```

---

# 3. Feature Engineering

Arquivo:

```python
feature_engineering.py
```

Esta etapa concentra a maior parte do valor analítico do projeto.

As variáveis criadas permitem análises demográficas, geográficas, temporais e de perfil do catálogo.

---

# Classificação Indicativa

## create_rating_group()

Agrupa ratings detalhados em categorias mais amplas.

### Exemplo

| Rating | Grupo |
|----------|----------|
| TV-Y | Kids |
| PG | Family |
| TV-14 | Teen |
| TV-MA | Adult |
| UR | Unknown |

### Variável criada

```python
rating_group
```

---

# Geografia

## create_main_country()

Extrai o primeiro país informado.

### Exemplo

```text
United States, India
```

↓

```text
United States
```

### Variável criada

```python
main_country
```

---

## create_continent()

Mapeia o país principal para um continente.

### Exemplo

| País | Continente |
|--------|--------|
| Brazil | South America |
| India | Asia |
| France | Europe |

### Variável criada

```python
continent
```

---

## create_language()

Infere o idioma principal com base no país principal.

### Exemplo

| País | Idioma |
|--------|--------|
| Brazil | Portuguese |
| United States | English |
| Japan | Japanese |

### Variável criada

```python
language
```

---

# Features Temporais

## create_date_features()

Cria variáveis relacionadas ao momento em que o conteúdo foi incorporado ao catálogo.

---

### year_added

Ano em que o conteúdo entrou na Netflix.

Exemplo:

```text
2019-06-01
```

↓

```text
2019
```

---

### delay_added

Tempo entre lançamento e entrada no catálogo.

Fórmula:

```python
year_added - release_year
```

Exemplo:

| Lançamento | Entrada |
|------------|----------|
| 2017 | 2020 |

↓

```text
3 anos
```

---

# Gênero Principal

## create_genre()

Agrupa dezenas de gêneros em categorias mais amplas.

### Exemplo

| Gênero Original | Categoria |
|-----------------|------------|
| TV Dramas | Drama |
| TV Comedies | Comedy |
| Docuseries | Documentary |

### Variável criada

```python
genre
```

---

# Década de Lançamento

## create_release_decade()

Transforma o ano em década.

### Exemplo

| Ano |
|------|
| 1994 |

↓

```text
1990
```

### Variável criada

```python
release_decade
```

---

# Categoria de Duração

## create_duration_category()

Classifica filmes e séries de acordo com seu tamanho.

---

### Filmes

| Duração | Categoria |
|----------|----------|
| ≤ 40 min | Short Film |
| 41–70 min | Medium-length Film |
| > 70 min | Feature Film |

---

### Séries

| Temporadas | Categoria |
|------------|------------|
| 1 | Limited Series |
| 2–3 | Short Series |
| ≥ 4 | Long-running Series |

### Variável criada

```python
duration_category
```

---

# Complexidade da Produção

## create_n_countries()

Quantidade de países envolvidos na produção.

### Exemplo

```text
United States, Canada
```

↓

```text
2
```

### Variável criada

```python
n_countries
```

---

## create_n_genres()

Quantidade de gêneros associados ao conteúdo.

### Variável criada

```python
n_genres
```

---

## create_n_cast_members()

Quantidade de atores informados.

### Variável criada

```python
n_cast_members
```

---

## create_n_directors()

Quantidade de diretores informados.

### Variável criada

```python
n_directors
```

---

# 4. Load

Arquivo:

```python
load.py
```

Responsável por orquestrar todo o pipeline.

---

# Fluxo executado

```text
read_csv()
      ↓
clean_netflix()
      ↓
create_rating_group()
      ↓
create_main_country()
      ↓
create_continent()
      ↓
create_language()
      ↓
create_date_features()
      ↓
create_genre()
      ↓
create_release_decade()
      ↓
create_duration_category()
      ↓
create_n_countries()
      ↓
create_n_genres()
      ↓
create_n_cast_members()
      ↓
create_n_directors()
      ↓
Dataset Final
```

---

# Datasets Gerados

## netflix.csv

Tabela principal para análise.

Granularidade:

```text
1 linha = 1 título
```

---

## netflix_directors.csv

Tabela relacional entre títulos e diretores.

Granularidade:

```text
1 linha = 1 diretor por título
```

---

## netflix_cast.csv

Tabela relacional entre títulos e atores.

Granularidade:

```text
1 linha = 1 ator por título
```

---

# Resultado Final

Após o ETL, o dataset deixa de ser apenas um catálogo de títulos e passa a conter informações estruturadas para:

- Análise Exploratória (EDA);
- Testes de Hipótese;
- Séries Temporais;
- Clusterização;
- Social Network Analysis (SNA);
- Construção de Dashboards.

O principal ganho do processo está na etapa de Feature Engineering, responsável por transformar atributos brutos em variáveis analíticas capazes de gerar insights de negócio e suportar modelos estatísticos e de Machine Learning.