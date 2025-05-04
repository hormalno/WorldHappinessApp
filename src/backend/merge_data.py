import pandas as pd

def merge_and_reformat(left, right):
    merged = pd.merge(left, right, how="outer", on="country")
    merged = reformat(merged)
    return merged


def reformat(df):
    #combine regions if available
    if "region_x" in df.columns and "region_y" in df.columns:
        df.insert(1, "region", df['region_x'].combine_first(df['region_y']))
        df = df.drop(columns=['region_x', 'region_y'])
        df['region'] = df['region'].fillna('N/A').astype(str)

    score_columns = ["economy", "family", "health", "freedom", "trust", "generosity", "dyst_res"]

    #combine each score columns
    for score_col in score_columns:
        df[score_col] = df[[col for col in df.columns if col in [(score_col+"_x"), (score_col+"_y")]]].mean(axis=1)
        df = df.drop(columns=[col for col in df.columns if col in [(score_col+"_x"), (score_col+"_y")]])

    #calculate happiness score
    df.insert(2, "happiness_score", df[[col for col in df.columns if col in score_columns]].sum(axis=1))
    df = df.drop(columns=['happiness_score_x', 'happiness_score_y'])

    #calculate the rank
    df = df.drop(columns=['happiness_rank_x', 'happiness_rank_y'])
    df.insert(2, "happiness_rank", df['happiness_score'].rank(ascending=False, method='min').astype(int))



    return df