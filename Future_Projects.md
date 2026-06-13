# Roadmap Analítico do Projeto

## Ordem recomendada para o projeto

1. **Análise Exploratória (EDA)**
2. **Testes de Hipótese**
3. **Séries Temporais**
4. **Clusterização (Machine Learning não supervisionado)**
5. **Social Network Analysis (SNA)**

---

## Grau de dificuldade estimado

| Etapa                   | Dificuldade |
| ----------------------- | :---------: |
| EDA                     |   **3/10**  |
| Testes de hipótese      |   **5/10**  |
| Séries temporais        |   **6/10**  |
| Clusterização           |   **7/10**  |
| Social Network Analysis |   **8/10**  |

```text
EDA                     ███░░░░░░░   3/10
Testes de hipótese      █████░░░░░   5/10
Séries temporais        ██████░░░░   6/10
Clusterização           ███████░░░   7/10
SNA                     ████████░░   8/10
```

---

# Prompt 1 — Análise Exploratória (EDA)

## Objetivo

Responder às principais perguntas de negócio relacionadas ao catálogo da Netflix antes da aplicação de técnicas mais avançadas.

---

## Dados utilizados

* `netflix.csv`
* `netflix_cast.csv`
* `netflix_directors.csv`

---

## Etapas desejadas

### 1. Compreensão dos dados

* Apresente a dimensão dos datasets;
* Identifique o significado de cada variável;
* Verifique tipos de dados;
* Identifique valores ausentes e duplicados.

---

### 2. Limpeza e preparação

* Trate valores ausentes de forma apropriada;
* Converta colunas de datas para datetime;
* Crie variáveis derivadas relevantes:

  * `year_added`;
  * `month_added`;
  * `weekday_added`;
  * `delay_added`;
  * `duration_category`;
  * `rating_group`;
  * `n_cast_members`;
  * `n_directors`;
  * `n_genres`.

---

### 3. Análise univariada

Investigue a distribuição das principais variáveis:

* `type`;
* `release_year`;
* `year_added`;
* `delay_added`;
* `rating_group`;
* `duration_category`;
* `n_cast_members`;
* `n_directors`;
* `n_genres`;
* países mais frequentes;
* gêneros mais frequentes.

---

### 4. Análise bivariada

Explore relações entre variáveis relevantes.

Exemplos:

* Movie × TV Show versus `delay_added`;
* Movie × TV Show versus `duration`;
* `rating_group` versus `duration`;
* `release_year` versus `delay_added`;
* `n_cast_members` versus `type`;
* países versus tipo de conteúdo.

---

### 5. Análise multivariada

Investigue possíveis padrões envolvendo múltiplas variáveis.

Exemplos:

* composição do catálogo por país e tipo;
* evolução temporal por tipo de conteúdo;
* relação entre rating, duração e tipo de conteúdo.

---

### 6. Questões de negócio

Responder às seguintes perguntas:

* O catálogo é composto majoritariamente por filmes ou séries?
* Como o catálogo cresceu ao longo do tempo?
* Quais países contribuem mais para o catálogo?
* Quais gêneros predominam?
* Os filmes entram na Netflix mais rapidamente do que as séries?
* O catálogo é formado principalmente por conteúdos recentes ou antigos?
* Existem diferenças relevantes entre filmes e séries em relação à duração, classificação indicativa e tamanho do elenco?
* Existem padrões temporais na adição de conteúdos ao catálogo?

---

### 7. Comunicação dos resultados

* Produza visualizações claras utilizando Plotly;
* Destaque os principais insights encontrados;
* Discuta possíveis implicações estratégicas.

---

# Prompt 2 — Testes de Hipótese

## Objetivo

Validar estatisticamente padrões identificados durante a EDA.

---

## Diretrizes gerais

1. Defina H0 e H1;
2. Verifique pressupostos;
3. Escolha testes adequados;
4. Reporte estatísticas e valor-p;
5. Apresente tamanho do efeito;
6. Interprete os resultados em linguagem de negócio.

---

## Hipótese 1

### Pergunta

A Netflix adiciona séries mais rapidamente do que filmes?

### Variáveis

* `delay_added`
* `type`

### Grupos

* Movie
* TV Show

### Teste sugerido

* Mann–Whitney U.

---

## Hipótese 2

### Pergunta

Filmes destinados a públicos diferentes apresentam durações distintas?

### Variáveis

* `duration`
* `rating_group`

### Teste sugerido

* ANOVA;
* Kruskal–Wallis.

---

## Hipótese 3

### Pergunta

Séries possuem elencos maiores do que filmes?

### Variáveis

* `n_cast_members`
* `type`

### Teste sugerido

* Mann–Whitney U.

---

## Hipótese 4

### Pergunta

A estratégia de aquisição mudou após 2020?

### Variáveis

* `delay_added`
* período (antes/depois de 2020).

### Teste sugerido

* Mann–Whitney U.

---

## Para cada hipótese

* Apresente boxplots;
* Apresente distribuições;
* Justifique a escolha do teste;
* Reporte tamanho do efeito;
* Interprete os resultados para gestores.

---

# Prompt 3 — Séries Temporais

## Objetivo

Compreender a evolução do catálogo ao longo do tempo.

---

## Dados utilizados

Utilize `date_added` como referência temporal.

Analise filmes e séries separadamente.

---

## Etapas desejadas

1. Construa séries temporais semanais;
2. Analise tendências;
3. Investigue sazonalidade;
4. Calcule médias móveis;
5. Identifique semanas anômalas;
6. Compare filmes e séries;
7. Discuta mudanças estratégicas;
8. Produza gráficos interativos com Plotly.

---

## Questões de negócio

* O catálogo cresceu continuamente?
* Houve aceleração ou desaceleração?
* Filmes e séries apresentam padrões temporais distintos?
* Existem eventos extremos que merecem investigação?

---

# Prompt 4 — Machine Learning (Clusterização)

## Objetivo

Identificar perfis naturais de conteúdos presentes na Netflix.

---

## Variáveis sugeridas

* `type`
* `main_country`
* `continent`
* `release_year`
* `delay_added`
* `rating_group`
* `duration_category`
* `n_directors`
* `n_cast_members`
* `n_genres`

---

## Etapas desejadas

1. Faça o pré-processamento adequado;
2. Utilize StandardScaler;
3. Utilize One-Hot Encoding;
4. Determine o número ótimo de clusters;
5. Ajuste um modelo K-Means;
6. Descreva detalhadamente os clusters;
7. Interprete os resultados do ponto de vista de negócio;
8. Produza visualizações utilizando PCA ou t-SNE.

---

## Questões de negócio

* Existem perfis distintos de conteúdos?
* Quais características definem cada grupo?
* Existem clusters dominados por filmes ou séries?

---

# Prompt 5 — Social Network Analysis (SNA)

## Objetivo

Explorar relações entre profissionais presentes no catálogo.

---

## Dados utilizados

* `netflix_cast.csv`
* `netflix_directors.csv`

---

## Rede principal

### Rede de co-participação entre atores

#### Definições

* **Nó:** ator;
* **Aresta:** dois atores participaram do mesmo título.

---

## Etapas desejadas

1. Construa a rede utilizando NetworkX;

2. Restrinja a análise aos atores mais frequentes;

3. Calcule métricas clássicas:

   * Degree Centrality;
   * Betweenness Centrality;
   * Eigenvector Centrality;
   * Clustering Coefficient.

4. Detecte comunidades;

5. Identifique os atores mais influentes;

6. Produza visualizações da rede;

7. Discuta os resultados.

---

## Rede opcional

### Rede bipartida ator–diretor

#### Definições

* Nós: atores e diretores;
* Arestas: colaboração em um mesmo título.

---

## Questões de negócio

* Quais atores ocupam posições estratégicas?
* Existem comunidades bem definidas?
* Quais diretores apresentam maior diversidade de parcerias?
