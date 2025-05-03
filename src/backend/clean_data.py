import pandas as pd

df_2015 = pd.read_csv("data/2015.csv")
df_2016 = pd.read_csv("data/2016.csv")
df_2017 = pd.read_csv("data/2017.csv")
df_2018 = pd.read_csv("data/2018.csv")
df_2019 = pd.read_csv("data/2019.csv")

# df_2015.rename(columns="Happiness Rank": "")
# df_2015.drop_duplicates(subset=['Country'])

def clean_data_2015():
    return df_2015

def clean_data_2016():
    return df_2015