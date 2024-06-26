import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """
    Loads file given by path into csv
    """
    try:
        df = pd.read_csv(path)
        print(df.shape)
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
