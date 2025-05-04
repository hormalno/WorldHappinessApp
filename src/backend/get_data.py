from functools import reduce
from .clean_data import clean_data
from .merge_data import merge_and_reformat

def get_data_by_year(year):
    return clean_data(str(year)+".csv")

def get_all_data():
    df_2015 = get_data_by_year("2015")
    df_2016 = get_data_by_year("2016")
    df_2017 = get_data_by_year("2017")
    df_2018 = get_data_by_year("2018")
    df_2019 = get_data_by_year("2019")

    merged_df = reduce(merge_and_reformat, [df_2015, df_2016, df_2017, df_2018, df_2019])

    return merged_df

def get_data_by_year_and_country(year, country):
    df = get_data_by_year(year)
    return df[df['country'] == country]

def get_all_data_by_country(country):
    df = get_all_data()
    return df[df['country'] == country]

def get_data_by_year_and_region(year, region):
    df = get_data_by_year(year)
    return df[df['region'] == region]

def get_all_data_by_region(region):
    df = get_all_data()
    return df[df['region'] == region]

def get_all_region():
    df = get_all_data()
    return sorted(df['region'].unique().tolist())

def get_all_country(region=None):
    df = get_all_data()

    if region:
        return sorted(df[df['region'] == region]['country'].unique())

    return sorted(df['country'].unique().tolist())


