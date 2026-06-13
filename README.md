# Netflix Data Analysis

Projeto de análise exploratória do catálogo da Netflix utilizando Python e Pandas.

## Objetivos

* Realizar a extração e limpeza dos dados;
* Aplicar boas práticas de organização de projetos de dados;
* Desenvolver análises exploratórias sobre o catálogo da Netflix;
* Gerar insights relacionados a filmes e séries disponíveis na plataforma.

## Estrutura do projeto

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


## Feature Engieneering

### Rating

| Rating       | Significado                   | Público                                                        |
| ------------ | ----------------------------- | -------------------------------------------------------------- |
| **TV-MA**    | Mature Audience Only          | Conteúdo adulto (17+)                                          |
| **TV-14**    | Parents Strongly Cautioned    | Pode ser inadequado para menores de 14 anos                    |
| **TV-PG**    | Parental Guidance Suggested   | Orientação dos pais recomendada                                |
| **R**        | Restricted                    | Menores de 17 anos precisam de acompanhante adulto             |
| **PG-13**    | Parents Strongly Cautioned    | Alguns conteúdos podem ser inadequados para menores de 13 anos |
| **TV-Y7**    | Directed to Older Children    | Indicado para crianças a partir de 7 anos                      |
| **TV-Y**     | All Children                  | Adequado para todas as crianças                                |
| **PG**       | Parental Guidance Suggested   | Orientação dos pais sugerida                                   |
| **TV-G**     | General Audience              | Adequado para todos os públicos                                |
| **NR**       | Not Rated                     | Sem classificação oficial                                      |
| **G**        | General Audiences             | Livre para todos os públicos                                   |
| **UR**       | Unrated                       | Versão não classificada / classificação desconhecida           |
| **TV-Y7-FV** | Fantasy Violence              | Crianças 7+, contém violência fantasiosa                       |
| **NC-17**    | No Children Under 17 Admitted | Proibido para menores de 17 anos                               |

---

### Agrupamento por Público

| Grupo       | Ratings                  |
| ----------- | ------------------------ |
| **Kids**    | TV-Y, TV-Y7, TV-Y7-FV, G |
| **Family**  | TV-G, PG                 |
| **Teen**    | TV-PG, TV-14, PG-13      |
| **Adult**   | TV-MA, R, NC-17          |
| **Unknown** | NR, UR                   |


## 🌍 Continentes e Países

| Continente | Países |
|------------|---------|
| **North America** | United States, Canada, Mexico |
| **Central America** | Costa Rica, Cuba, Dominican Republic, El Salvador, Guatemala, Honduras, Jamaica, Nicaragua, Panama, Puerto Rico |
| **South America** | Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Paraguay, Peru, Uruguay, Venezuela |
| **Europe** | Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Liechtenstein, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Russia, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United Kingdom, Vatican City |
| **Africa** | Algeria, Angola, Botswana, Burkina Faso, Cameroon, Congo, Egypt, Ethiopia, Ghana, Kenya, Malawi, Mauritius, Morocco, Namibia, Nigeria, Senegal, South Africa, Sudan, Tunisia, Uganda, Zimbabwe |
| **Asia** | Afghanistan, Bangladesh, Cambodia, China, Hong Kong, India, Indonesia, Iran, Iraq, Israel, Japan, Jordan, Kazakhstan, Kuwait, Lebanon, Malaysia, Mongolia, Nepal, Pakistan, Philippines, Saudi Arabia, Singapore, South Korea, Sri Lanka, Syria, Taiwan, Thailand, United Arab Emirates, Vietnam |
| **Oceania** | Australia, New Zealand |
| **Unknown** | Unknown |