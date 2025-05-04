from backend import get_all_data

def sort_all_data_by_rank_asc():
    df = get_all_data()
    df = df.sort_values('happiness_rank')
    return df

def sort_all_data_by_rank_desc():
    df = get_all_data()
    df = df.sort_values('happiness_rank', ascending=False)
    return df
