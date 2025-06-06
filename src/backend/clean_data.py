import pandas as pd

FILEPATH = "src/backend/data/"
MAPPING = {
    "country": "country",
    "region": "region",
    "happiness_rank": "rank",
    "happiness_score": "score",
    "economy": "economy,gdp",
    "family": "family,support",
    "health": "health",
    "freedom": "freedom",
    "trust": "trust,corruption",
    "generosity": "generosity",
    "dyst_res": "dystopia,residual"
}

def clean_data(arg):
    #read data from csv
    df = pd.read_csv(FILEPATH+str(arg)+".csv")

    #rename column names
    df = column_mapping(df)

    #drop columns that are not part of the frame
    df = df.drop(columns=[col for col in df.columns if col not in MAPPING.keys()])

    #fill in the dystopian residual for the missing column
    if "dyst_res" not in df.columns:
        df['dyst_res'] = (df['happiness_score']
                          - df[['economy', 'family', 'health', 'freedom', 'trust', 'generosity']].sum(axis=1))

    #fill in the region for the missing column
    if "region" not in df.columns:
        df_2015 = pd.read_csv(FILEPATH+"2015.csv")
        df_2015 = df_2015.rename(columns={"Country":"country", "Region": "region"})
        df = df.merge(df_2015[['country', 'region']],on='country',how='left')
        df['region'] = df['region'].fillna('N/A')

    #reorder columns
    df = df[MAPPING.keys()]

    return df

def column_mapping(df):
    new_columns = {}

    for col in df.columns:
        new_col_name = rename_column(col)
        if new_col_name:
            new_columns[col] = new_col_name
    return df.rename(columns=new_columns)

def rename_column(col):
    for key, value in MAPPING.items():
        for col_name in value.split(','):
            if col_name in col.lower():
                return key
    return None