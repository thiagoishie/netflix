from pathlib import Path
import pandas as pd

from src.extract import read_csv
from src.cleaning import clean_netflix
from src.feature_engineering import (
    create_rating_group,
    create_main_country,
    create_continent,
    create_language,
    create_date_features,
    create_genre,
    create_release_decade,
    create_duration_category,
    create_n_countries,
    create_n_genres,
    create_n_cast_members,
    create_n_directors
)


def _prepare_netflix(path: str | Path) -> pd.DataFrame:
    """
    Executa todo o pipeline de preparação dos dados.
    """

    df = read_csv(path)

    df = clean_netflix(df)

    transformations = [
        create_rating_group,
        create_main_country,
        create_continent,
        create_language,
        create_date_features,
        create_genre,
        create_release_decade,
        create_duration_category,
        create_n_countries,
        create_n_genres,
        create_n_cast_members,
        create_n_directors
    ]

    for transform in transformations:
        df = transform(df)

    return df


def load_netflix(path: str | Path) -> pd.DataFrame:
    """
    Retorna a tabela principal do catálogo da Netflix.
    """

    df = _prepare_netflix(path)

    column_order = [
        # identificação
        'type',
        'title',
        'description',

        # pessoas envolvidas
        'director',
        'n_directors',
        'cast',
        'n_cast_members',

        # localização
        'country',
        'n_countries',
        'main_country',
        'continent',
        'language',

        # tempo
        'release_year',
        'release_decade',
        'date_added',
        'year_added',
        'delay_added',

        # classificação indicativa
        'rating',
        'rating_group',

        # formato do conteúdo
        'duration',
        'duration_category',

        # gêneros
        'listed_in',
        'n_genres',
        'genre'
    ]

    return df[column_order]

def load_netflix_directors(path: str) -> pd.DataFrame:
    """
    Retorna a tabela relacional entre títulos e diretores.
    """

    df = load_netflix(path)

    directors_df = (
        df[['title', 'director']]
        .query("director != 'Not Informed'")
        .assign(director=lambda x: x['director'].str.split(','))
        .explode('director')
    )

    directors_df['director'] = directors_df['director'].str.strip()

    return directors_df.reset_index(drop=True)


def load_netflix_cast(path: str) -> pd.DataFrame:
    """
    Retorna a tabela relacional entre títulos e atores.
    """

    df = load_netflix(path)

    cast_df = (
        df[['title', 'cast']]
        .query("cast != 'Not Informed'")
        .assign(cast=lambda x: x['cast'].str.split(','))
        .explode('cast')
    )

    cast_df['cast'] = cast_df['cast'].str.strip()

    return cast_df.reset_index(drop=True)

from pathlib import Path


def save_processed_data(path: str) -> None:
    """
    Salva os datasets processados.
    """

    project_root = Path(__file__).resolve().parent.parent

    processed_path = project_root / 'data' / 'processed'

    processed_path.mkdir(parents=True, exist_ok=True)

    netflix = load_netflix(path)

    netflix_directors = load_netflix_directors(path)

    netflix_cast = load_netflix_cast(path)

    netflix.to_csv(
        processed_path / 'netflix.csv',
        index=False
    )

    netflix_directors.to_csv(
        processed_path / 'netflix_directors.csv',
        index=False
    )

    netflix_cast.to_csv(
        processed_path / 'netflix_cast.csv',
        index=False
    )

    print('Arquivos salvos com sucesso!')