import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """
    Loads csv into pandas data frame
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
