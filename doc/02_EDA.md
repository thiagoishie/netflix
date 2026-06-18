````markdown id="c7rw0w"
# Notebook 02 — Testes de Hipótese

# Objetivo

Após compreender a estrutura do catálogo por meio da Análise Exploratória de Dados (EDA), a próxima etapa consiste em verificar se os padrões observados são estatisticamente significativos.

Enquanto a EDA identifica possíveis comportamentos nos dados, os testes de hipótese permitem avaliar se essas diferenças são reais ou se podem ter ocorrido por acaso.

---

# Objetivo Analítico

Responder perguntas de negócio utilizando inferência estatística.

O foco deste notebook é transformar observações da EDA em hipóteses testáveis.

---

# Fluxo do Notebook

```text
EDA
 │
 ▼
Identificação de padrões
 │
 ▼
Formulação das hipóteses
 │
 ▼
Análise das distribuições
 │
 ▼
Escolha do teste estatístico
 │
 ▼
Cálculo do p-value
 │
 ▼
Conclusão estatística
```

---

# Conceitos Utilizados

## Hipótese Nula (H₀)

Representa a ausência de diferença entre grupos.

Exemplo:

```text
Filmes e séries possuem o mesmo tempo médio
entre lançamento e entrada no catálogo.
```

---

## Hipótese Alternativa (H₁)

Representa a existência de diferença.

Exemplo:

```text
Filmes e séries possuem tempos diferentes
entre lançamento e entrada no catálogo.
```

---

## Nível de Significância

Foi adotado:

```python
α = 0.05
```

Interpretação:

```text
p-value < 0.05
```

↓

Rejeita-se H₀.

---

# Hipótese 1

## Séries são adicionadas mais rapidamente ao catálogo do que filmes?

### Motivação

A Netflix pode adotar estratégias diferentes para aquisição de filmes e séries.

O objetivo é verificar se existe diferença no tempo entre:

```text
lançamento
        ↓
entrada na Netflix
```

---

### Variável analisada

```python
delay_added
```

Criada durante o ETL.

Representa:

```python
year_added - release_year
```

---

### Grupos comparados

```python
Movie
TV Show
```

---

### Hipóteses

#### H₀

```text
Não existe diferença no delay_added
entre filmes e séries.
```

#### H₁

```text
Existe diferença no delay_added
entre filmes e séries.
```

---

### Teste Estatístico

Antes da escolha do teste são avaliados:

- normalidade;
- presença de outliers;
- formato da distribuição.

Como a variável apresenta assimetria e valores extremos, utiliza-se:

```text
Mann-Whitney U Test
```

---

### Resultado esperado

Determinar se a estratégia de aquisição da Netflix é diferente para filmes e séries.

---

# Hipótese 2

## Filmes voltados para públicos diferentes possuem durações diferentes?

### Motivação

Conteúdos infantis, adolescentes e adultos podem apresentar características distintas de duração.

---

### Variáveis analisadas

```python
rating_group
duration
```

---

### Grupos comparados

```text
Kids
Family
Teen
Adult
```

---

### Hipóteses

#### H₀

```text
Todos os grupos possuem a mesma duração média.
```

#### H₁

```text
Pelo menos um grupo apresenta duração diferente.
```

---

### Teste Estatístico

Como existem mais de dois grupos:

```text
ANOVA
```

Caso os pressupostos não sejam atendidos:

```text
Kruskal-Wallis
```

---

### Resultado esperado

Verificar se o público-alvo influencia a duração dos filmes.

---

# Hipótese 3

## Séries possuem elencos maiores do que filmes?

### Motivação

Séries normalmente apresentam mais episódios e personagens recorrentes.

Isso sugere a possibilidade de elencos maiores.

---

### Variável analisada

```python
n_cast_members
```

Criada durante o ETL.

Representa a quantidade de atores associados ao título.

---

### Grupos comparados

```python
Movie
TV Show
```

---

### Hipóteses

#### H₀

```text
Não existe diferença no tamanho do elenco.
```

#### H₁

```text
Existe diferença no tamanho do elenco.
```

---

### Teste Estatístico

```text
Mann-Whitney U
```

ou

```text
T-Test
```

Dependendo da distribuição observada.

---

### Resultado esperado

Avaliar diferenças estruturais entre filmes e séries.

---

# Hipótese 4

## A estratégia de aquisição mudou após 2020?

### Motivação

A pandemia provocou mudanças importantes no mercado de streaming.

O objetivo é investigar se a Netflix alterou seu comportamento de aquisição.

---

### Variável analisada

```python
delay_added
```

---

### Grupos comparados

```text
Antes de 2020
Após 2020
```

---

### Hipóteses

#### H₀

```text
A distribuição de delay_added permaneceu igual.
```

#### H₁

```text
A distribuição de delay_added mudou após 2020.
```

---

### Teste Estatístico

```text
Mann-Whitney U
```

---

### Resultado esperado

Identificar possíveis mudanças estratégicas na expansão do catálogo.

---

# Análises Complementares

Além dos testes formais, serão produzidas visualizações para auxiliar a interpretação dos resultados.

---

## Boxplots

Objetivo:

```text
Comparar distribuições entre grupos.
```

Aplicações:

- duração por rating;
- elenco por tipo;
- delay por período.

---

## Histogramas

Objetivo:

```text
Avaliar formato das distribuições.
```

Aplicações:

- normalidade;
- assimetria;
- presença de outliers.

---

## KDE Plots

Objetivo:

```text
Comparar densidades entre grupos.
```

---

# Medidas de Efeito

Além do p-value, serão calculadas medidas de efeito para avaliar a magnitude prática dos resultados.

---

## Por que utilizar?

Um resultado pode ser estatisticamente significativo e ainda assim possuir impacto muito pequeno.

Por isso, a análise será composta por:

```text
Significância Estatística
+
Magnitude do Efeito
```

---

## Possíveis métricas

### Cohen's d

Para comparação entre médias.

---

### Rank-Biserial Correlation

Para Mann-Whitney.

---

### Eta Squared (η²)

Para ANOVA.

---

# Critérios de Interpretação

## Cenário 1

```text
p-value < 0.05
```

Resultado:

```text
Diferença estatisticamente significativa.
```

---

## Cenário 2

```text
p-value ≥ 0.05
```

Resultado:

```text
Não há evidências suficientes
para rejeitar a hipótese nula.
```

---

# Entregáveis do Notebook

## Estatística Descritiva

- médias;
- medianas;
- desvios-padrão;
- quartis.

---

## Testes Estatísticos

- Mann-Whitney U;
- ANOVA;
- Kruskal-Wallis;
- Testes de normalidade.

---

## Visualizações

- boxplots;
- histogramas;
- KDE plots.

---

## Resultado Final

Ao término deste notebook será possível determinar, com base em evidências estatísticas, se os padrões identificados durante a EDA representam diferenças reais no catálogo da Netflix.

Os resultados obtidos servirão de base para a próxima etapa do projeto:

```text
03_TimeSeries.ipynb
```

onde será investigada a evolução temporal do catálogo e sua dinâmica de crescimento ao longo dos anos.
````
