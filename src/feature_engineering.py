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
    Extrai o primeiro país informado na coluna country,
    assumindo-o como país principal da produção.
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

def create_language(df: pd.DataFrame) -> pd.DataFrame:
    """
    Define a principal língua da obra com base no país principal
    de produção (main_country).
    """

    df = df.copy()

    language_mapping = {

        # North America
        'United States': 'English',
        'Canada': 'English',
        'Mexico': 'Spanish',

        # Central America
        'Costa Rica': 'Spanish',
        'Cuba': 'Spanish',
        'Dominican Republic': 'Spanish',
        'El Salvador': 'Spanish',
        'Guatemala': 'Spanish',
        'Honduras': 'Spanish',
        'Jamaica': 'English',
        'Nicaragua': 'Spanish',
        'Panama': 'Spanish',
        'Puerto Rico': 'Spanish',

        # South America
        'Argentina': 'Spanish',
        'Bolivia': 'Spanish',
        'Brazil': 'Portuguese',
        'Chile': 'Spanish',
        'Colombia': 'Spanish',
        'Ecuador': 'Spanish',
        'Paraguay': 'Spanish',
        'Peru': 'Spanish',
        'Uruguay': 'Spanish',
        'Venezuela': 'Spanish',

        # Europe
        'Austria': 'German',
        'Belgium': 'French',
        'Bulgaria': 'Bulgarian',
        'Croatia': 'Croatian',
        'Cyprus': 'Greek',
        'Czech Republic': 'Czech',
        'Denmark': 'Danish',
        'Finland': 'Finnish',
        'France': 'French',
        'Germany': 'German',
        'Greece': 'Greek',
        'Hungary': 'Hungarian',
        'Iceland': 'Icelandic',
        'Ireland': 'English',
        'Italy': 'Italian',
        'Luxembourg': 'French',
        'Netherlands': 'Dutch',
        'Norway': 'Norwegian',
        'Poland': 'Polish',
        'Portugal': 'Portuguese',
        'Romania': 'Romanian',
        'Russia': 'Russian',
        'Serbia': 'Serbian',
        'Slovakia': 'Slovak',
        'Slovenia': 'Slovene',
        'Spain': 'Spanish',
        'Sweden': 'Swedish',
        'Switzerland': 'German',
        'Turkey': 'Turkish',
        'Ukraine': 'Ukrainian',
        'United Kingdom': 'English',

        # Africa
        'Algeria': 'Arabic',
        'Angola': 'Portuguese',
        'Botswana': 'English',
        'Burkina Faso': 'French',
        'Cameroon': 'French',
        'Congo': 'French',
        'Egypt': 'Arabic',
        'Ethiopia': 'Amharic',
        'Ghana': 'English',
        'Kenya': 'English',
        'Malawi': 'English',
        'Mauritius': 'French',
        'Morocco': 'Arabic',
        'Namibia': 'English',
        'Nigeria': 'English',
        'Senegal': 'French',
        'South Africa': 'English',
        'Sudan': 'Arabic',
        'Tunisia': 'Arabic',
        'Uganda': 'English',
        'Zimbabwe': 'English',

        # Asia
        'Afghanistan': 'Dari',
        'Bangladesh': 'Bengali',
        'Cambodia': 'Khmer',
        'China': 'Mandarin',
        'Hong Kong': 'Cantonese',
        'India': 'Hindi',
        'Indonesia': 'Indonesian',
        'Iran': 'Persian',
        'Iraq': 'Arabic',
        'Israel': 'Hebrew',
        'Japan': 'Japanese',
        'Jordan': 'Arabic',
        'Kazakhstan': 'Kazakh',
        'Kuwait': 'Arabic',
        'Lebanon': 'Arabic',
        'Malaysia': 'Malay',
        'Mongolia': 'Mongolian',
        'Nepal': 'Nepali',
        'Pakistan': 'Urdu',
        'Philippines': 'Filipino',
        'Saudi Arabia': 'Arabic',
        'Singapore': 'English',
        'South Korea': 'Korean',
        'Sri Lanka': 'Sinhala',
        'Syria': 'Arabic',
        'Taiwan': 'Mandarin',
        'Thailand': 'Thai',
        'United Arab Emirates': 'Arabic',
        'Vietnam': 'Vietnamese',

        # Oceania
        'Australia': 'English',
        'New Zealand': 'English',

        # Unknown
        'Unknown': 'Unknown'
    }

    df['language'] = (
        df['main_country']
        .map(language_mapping)
        .fillna('Unknown')
        .astype('category')
    )

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
    Extrai o primeiro gênero informado na coluna listed_in e o
    agrupa em categorias mais amplas.
    """

    df = df.copy()

    genre_mapping = {

        # Drama
        'Dramas': 'Drama',
        'TV Dramas': 'Drama',

        # Comedy
        'Comedies': 'Comedy',
        'TV Comedies': 'Comedy',
        'Stand-Up Comedy': 'Comedy',
        'Stand-Up Comedy & Talk Shows': 'Comedy',

        # Action
        'Action & Adventure': 'Action & Adventure',
        'TV Action & Adventure': 'Action & Adventure',

        # Documentary
        'Documentaries': 'Documentary',
        'Docuseries': 'Documentary',

        # Horror
        'Horror Movies': 'Horror',
        'TV Horror': 'Horror',

        # Crime
        'Crime TV Shows': 'Crime',
        'Thrillers': 'Crime',

        # International
        'International Movies': 'International',
        'International TV Shows': 'International',

        # Family
        'Children & Family Movies': 'Family',
        "Kids' TV": 'Family',

        # TV Shows
        'British TV Shows': 'TV Shows',
        'Classic & Cult TV': 'TV Shows',

        # Reality
        'Reality TV': 'Reality',

        # Romance
        'Romantic Movies': 'Romance',
        'Romantic TV Shows': 'Romance',

        # Anime
        'Anime Features': 'Anime',
        'Anime Series': 'Anime',

        # Sci-Fi
        'Sci-Fi & Fantasy': 'Sci-Fi & Fantasy',
        'TV Sci-Fi & Fantasy': 'Sci-Fi & Fantasy',

        # Music
        'Music & Musicals': 'Music',

        # Sports
        'Sports Movies': 'Sports',

        # Other
        'Classic Movies': 'Other',
        'Cult Movies': 'Other',
        'Independent Movies': 'Other',
        'LGBTQ Movies': 'Other',
        'Movies': 'Other',
        'Spanish-Language TV Shows': 'Other'
    }

    df['genre'] = (df['listed_in'].str.split(',').str[0].str.strip().map(genre_mapping).fillna('Other').astype('category'))

    return df

def create_release_decade(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria a década de lançamento do título.
    Ex.: 1994 -> 1990
    """

    df = df.copy()

    df['release_decade'] = (
        (df['release_year'] // 10 * 10)
        .astype('Int64')
    )

    return df

def create_duration_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Classifica a duração de acordo com o tipo do título.

    Movies:
        - Short Film: até 40 min
        - Medium-length Film: 41 a 70 min
        - Feature Film: acima de 70 min

    TV Shows:
        - Limited Series: 1 temporada
        - Short Series: 2 a 3 temporadas
        - Long-running Series: 4 ou mais temporadas
    """

    df = df.copy()

    df['duration_category'] = 'Unknown'

    movie_mask = df['type'] == 'Movie'
    tv_mask = df['type'] == 'TV Show'

    df.loc[movie_mask & (df['duration'] <= 40), 'duration_category'] = 'Short Film'
    df.loc[movie_mask & df['duration'].between(41, 70), 'duration_category'] = 'Medium-length Film'
    df.loc[movie_mask & (df['duration'] > 70), 'duration_category'] = 'Feature Film'

    df.loc[tv_mask & (df['duration'] == 1), 'duration_category'] = 'Limited Series'
    df.loc[tv_mask & df['duration'].between(2, 3), 'duration_category'] = 'Short Series'
    df.loc[tv_mask & (df['duration'] >= 4), 'duration_category'] = 'Long-running Series'

    df['duration_category'] = df['duration_category'].astype('category')

    return df

def create_n_countries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Conta o número de países associados à produção do título.
    """

    df = df.copy()

    df['n_countries'] = (
        df['country']
        .replace('Unknown', pd.NA)
        .str.split(',')
        .str.len()
        .fillna(0)
        .astype(int)
    )

    return df


def create_n_genres(df: pd.DataFrame) -> pd.DataFrame:
    """
    Conta o número de gêneros associados ao título.
    """

    df = df.copy()

    df['n_genres'] = (
        df['listed_in']
        .str.split(',')
        .str.len()
        .astype(int)
    )

    return df


def create_n_cast_members(df: pd.DataFrame) -> pd.DataFrame:
    """
    Conta o número de membros do elenco informados.
    """

    df = df.copy()

    df['n_cast_members'] = (
        df['cast']
        .replace('Not Informed', pd.NA)
        .str.split(',')
        .str.len()
        .fillna(0)
        .astype(int)
    )

    return df


def create_n_directors(df: pd.DataFrame) -> pd.DataFrame:
    """
    Conta o número de diretores informados.
    """

    df = df.copy()

    df['n_directors'] = (
        df['director']
        .replace('Not Informed', pd.NA)
        .str.split(',')
        .str.len()
        .fillna(0)
        .astype(int)
    )

    return df