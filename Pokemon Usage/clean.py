import pandas as pd

def clean_df (json_file):

    raw = pd.read_json("gen8ou-0.json")
    df = raw[raw['data'].notna()]['data']
    
    top_mons = {}
    ix = list(df.index)

    for row in range(len(df)):
        if df[row]['usage'] >= .02:
            mon = ix[row]
            top_6 = list(dict(sorted(df[row]['Moves'].items(), key=lambda item: item[1], reverse=True)))[:6]
            top_mons[mon] = [top_6, df[row]['usage']]
    
    return pd.DataFrame.from_dict(top_mons, orient = 'index').rename(columns = {0:"Moves", 1:"Usage"})