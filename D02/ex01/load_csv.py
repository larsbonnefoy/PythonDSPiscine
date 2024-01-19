import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """
        Loads file given by path and converts it to a pandas data frame
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
