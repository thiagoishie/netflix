import pandas as pd


def clean_netflix(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # remover a coluna show_id
    df = df.drop('show_id', axis=1)

    # preencher valores ausentes
    df['director'] = df['director'].fillna('Not Informed')
    df['cast'] = df['cast'].fillna('Not Informed')
    df['country'] = df['country'].fillna('Unknown')

    # converter data
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(),errors='coerce')

    # corrigir registros incorretos
    df.loc[5541, 'duration'] = df.loc[5541, 'rating']
    df.loc[5541, 'rating'] = pd.NA

    df.loc[5794, 'duration'] = df.loc[5794, 'rating']
    df.loc[5794, 'rating'] = pd.NA

    df.loc[5813, 'duration'] = df.loc[5813, 'rating']
    df.loc[5813, 'rating'] = pd.NA

    # preencher rating ausente
    df['rating'] = df['rating'].fillna('UR')

    # converter categorias
    df['type'] = df['type'].astype('category')
    df['rating'] = df['rating'].astype('category')

    # converter duração
    df['duration'] = (df['duration'].str.extract(r'(\d+)')[0].astype(int))

    return df