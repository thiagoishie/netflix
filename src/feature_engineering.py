import pandas as pd

def create_rating_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa as classificações indicativas em categorias mais amplas.
    """

    df = df.copy()

    rating_group = {
        'TV-Y': 'Kids',
        'TV-Y7': 'Kids',
        'TV-Y7-FV': 'Kids',
        'G': 'Kids',

        'TV-G': 'Family',
        'PG': 'Family',

        'TV-PG': 'Teen',
        'TV-14': 'Teen',
        'PG-13': 'Teen',

        'TV-MA': 'Adult',
        'R': 'Adult',
        'NC-17': 'Adult',

        'NR': 'Unknown',
        'UR': 'Unknown'
    }

    df['rating_group'] = (df['rating'].map(rating_group).astype('category'))

    return df

def create_main_country(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extrai o primeiro país informado na coluna country.
    """

    df = df.copy()

    df['main_country'] = (df['country'].str.split(',').str[0].str.strip().astype('category'))

    return df


def create_continent(df: pd.DataFrame) -> pd.DataFrame:
    """
    Classifica o país principal da produção em continentes/regiões.
    """

    df = df.copy()

    continent_mapping = {

        # América do Norte
        'United States': 'North America',
        'Canada': 'North America',
        'Mexico': 'North America',

        # América Central
        'Costa Rica': 'Central America',
        'Cuba': 'Central America',
        'Dominican Republic': 'Central America',
        'El Salvador': 'Central America',
        'Guatemala': 'Central America',
        'Honduras': 'Central America',
        'Jamaica': 'Central America',
        'Nicaragua': 'Central America',
        'Panama': 'Central America',
        'Puerto Rico': 'Central America',

        # América do Sul
        'Argentina': 'South America',
        'Bolivia': 'South America',
        'Brazil': 'South America',
        'Chile': 'South America',
        'Colombia': 'South America',
        'Ecuador': 'South America',
        'Paraguay': 'South America',
        'Peru': 'South America',
        'Uruguay': 'South America',
        'Venezuela': 'South America',

        # Europa
        'Austria': 'Europe',
        'Belgium': 'Europe',
        'Bulgaria': 'Europe',
        'Croatia': 'Europe',
        'Cyprus': 'Europe',
        'Czech Republic': 'Europe',
        'Denmark': 'Europe',
        'Finland': 'Europe',
        'France': 'Europe',
        'Germany': 'Europe',
        'Greece': 'Europe',
        'Hungary': 'Europe',
        'Iceland': 'Europe',
        'Ireland': 'Europe',
        'Italy': 'Europe',
        'Luxembourg': 'Europe',
        'Netherlands': 'Europe',
        'Norway': 'Europe',
        'Poland': 'Europe',
        'Portugal': 'Europe',
        'Romania': 'Europe',
        'Russia': 'Europe',
        'Serbia': 'Europe',
        'Slovakia': 'Europe',
        'Slovenia': 'Europe',
        'Spain': 'Europe',
        'Sweden': 'Europe',
        'Switzerland': 'Europe',
        'Turkey': 'Europe',
        'Ukraine': 'Europe',
        'United Kingdom': 'Europe',

        # África
        'Algeria': 'Africa',
        'Angola': 'Africa',
        'Botswana': 'Africa',
        'Burkina Faso': 'Africa',
        'Cameroon': 'Africa',
        'Egypt': 'Africa',
        'Ethiopia': 'Africa',
        'Ghana': 'Africa',
        'Kenya': 'Africa',
        'Malawi': 'Africa',
        'Mauritius': 'Africa',
        'Morocco': 'Africa',
        'Namibia': 'Africa',
        'Nigeria': 'Africa',
        'Senegal': 'Africa',
        'South Africa': 'Africa',
        'Sudan': 'Africa',
        'Tunisia': 'Africa',
        'Uganda': 'Africa',
        'Zimbabwe': 'Africa',

        # Ásia
        'Afghanistan': 'Asia',
        'Bangladesh': 'Asia',
        'Cambodia': 'Asia',
        'China': 'Asia',
        'Hong Kong': 'Asia',
        'India': 'Asia',
        'Indonesia': 'Asia',
        'Iran': 'Asia',
        'Iraq': 'Asia',
        'Israel': 'Asia',
        'Japan': 'Asia',
        'Jordan': 'Asia',
        'Kazakhstan': 'Asia',
        'Kuwait': 'Asia',
        'Lebanon': 'Asia',
        'Malaysia': 'Asia',
        'Mongolia': 'Asia',
        'Nepal': 'Asia',
        'Pakistan': 'Asia',
        'Philippines': 'Asia',
        'Saudi Arabia': 'Asia',
        'Singapore': 'Asia',
        'South Korea': 'Asia',
        'Sri Lanka': 'Asia',
        'Syria': 'Asia',
        'Taiwan': 'Asia',
        'Thailand': 'Asia',
        'United Arab Emirates': 'Asia',
        'Vietnam': 'Asia',

        # Oceania
        'Australia': 'Oceania',
        'New Zealand': 'Oceania',

        # Valores ausentes
        'Unknown': 'Unknown'
    }

    df['continent'] = (df['main_country'].map(continent_mapping).fillna('Unknown').astype('category'))

    return df

def create_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria variáveis derivadas da data de adição ao catálogo.
    """

    df = df.copy()

    # ano em que o título foi adicionado à Netflix
    df['year_added'] = (df['date_added'].dt.year.astype('Int64'))

    # tempo (em anos) entre lançamento e entrada no catálogo
    df['delay_added'] = (df['year_added']- df['release_year']).astype('Int64')

    return df

def create_genre(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extrai o primeiro gênero informado na coluna listed_in,
    assumindo-o como gênero principal da obra.
    """

    df = df.copy()

    df['genre'] = (df['listed_in'].str.split(',').str[0].str.strip().astype('category'))

    return df