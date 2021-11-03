from numpy import generic
import pandas as pd

# Takes input JSON Chaos file, outputs clean DataFrame
def clean_df (path_to_json):

    raw = pd.read_json(path_to_json)

    metagame = raw.loc['metagame'][0]
    gen = metagame[3]
    format_name = metagame[4:]
    rating = raw.loc["cutoff deviation"][0]

    df = raw[raw['data'].notna()]['data']
    
    top_mons = {}
    ix = list(df.index)

    for row in range(len(df)):
        if df[row]['usage'] >= .02:
            mon = ix[row]
            top_6 = list(dict(sorted(df[row]['Moves'].items(), key=lambda item: item[1], reverse=True)))[:6]
            top_mons[mon] = [top_6, df[row]['usage']]

    cleaned = pd.DataFrame.from_dict(top_mons, orient = 'index').rename(columns = {0:"Moves", 1:"Usage"})
    cleaned["Gen"] = gen
    cleaned["Format"] = format_name
    cleaned["Min Rating"] = rating
    return cleaned
