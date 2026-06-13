# Projeto de Análise de Dados: Catálogo da Netflix

## Objetivo do Projeto

Realizar uma análise exploratória do catálogo da Netflix para identificar padrões relacionados ao tipo de conteúdo, classificações indicativas, gêneros, países de produção e evolução do catálogo ao longo do tempo.

---

## Etapas do Projeto

| Etapa | O que foi realizado |
|--------|---------------------|
| **Entendimento do negócio** | Definição das perguntas de análise sobre o catálogo da Netflix. |
| **Coleta dos dados** | Leitura do arquivo `netflix_titles.csv`. |
| **Entendimento dos dados** | Exploração inicial utilizando `head()`, `info()`, `describe()` e análise de valores ausentes. |
| **Limpeza e preparação** | Tratamento de valores nulos, conversão de tipos de dados e padronização das categorias de gêneros. |
| **Análise Exploratória (EDA)** | Investigação de ratings, gêneros, países de produção e evolução temporal do catálogo. |
| **Modelagem** | Não aplicável, pois o objetivo do projeto é descritivo e exploratório. |
| **Comunicação dos resultados** | Documentação dos insights obtidos por meio de notebooks e README do projeto. |
| **Implantação** | Desenvolvimento opcional de um dashboard interativo em Power BI para visualização dos resultados. |

---

## Perguntas de Negócio

- Qual é a proporção entre filmes e séries disponíveis na Netflix?
- Quais são os gêneros mais frequentes no catálogo?
- Como o número de títulos adicionados evoluiu ao longo dos anos?
- Quais países mais produzem conteúdos disponíveis na plataforma?
- Quais classificações indicativas (ratings) são mais comuns?
- Existem diferenças entre filmes e séries em relação às classificações etárias?

---

## Fluxo do Projeto

```
Perguntas de negócio
        ↓
Coleta dos dados
        ↓
Entendimento dos dados
        ↓
Limpeza e preparação
        ↓
Análise exploratória (EDA)
        ↓
Comunicação dos resultados
        ↓
Dashboard
```

---

## Ferramentas Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib

---

## Estrutura Sugerida do Projeto

```text
netflix-analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── data_analytics.ipynb
│
├── src/
│   ├── extract.py
│   ├── cleaning.py
│   └── feature_engineering.py
│
├── README.md
│
└── requirements.txt
```

---

## Principais Entregáveis

- Dataset limpo e tratado;
- Notebook contendo a análise exploratória;
- Gráficos e visualizações dos principais resultados;
- README documentando objetivos, metodologia e insights;

---

## Resultado Esperado

Ao final do projeto, espera-se obter uma visão abrangente sobre a composição e a evolução do catálogo da Netflix, transformando dados brutos em informações úteis para apoiar decisões e gerar insights de negócio.
