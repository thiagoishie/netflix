import pandas as pd


def read_csv(path: str) -> pd.DataFrame:
    """
    Lê um arquivo CSV e retorna um DataFrame.
    """
    
    return pd.read_csv(path)