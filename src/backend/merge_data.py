import pandas as pd

from .clean_data import clean_data


def get_all_data():
    df_2015 = clean_data("2015.csv")
    df_2016 = clean_data("2016.csv")
    df_2017 = clean_data("2017.csv")
    df_2018 = clean_data("2018.csv")
    df_2019 = clean_data("2019.csv")

    # df = pd.merge(df_2015, df_2016, how="outer", on=["Country", "Region"], suffixes=("_2015", "_2016"))

    return [df_2015, df_2016, df_2017, df_2018, df_2019]