import pandas as pd

from src.backend.clean_data import clean_data_2015, clean_data_2016


def get_all_data():
    df_2015 = clean_data_2015()
    df_2016 = clean_data_2016()

    # df = pd.merge(df_2015, df_2016, how="outer", on=["Country", "Region"], suffixes=("_2015", "_2016"))

    return df_2015