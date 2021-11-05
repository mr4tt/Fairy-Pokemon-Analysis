from numpy import generic
import pandas as pd
import json

# Takes input JSON Chaos file, outputs clean DataFrame


def clean_df(path_to_json):

    raw = pd.read_json(path_to_json)

    metagame = raw.loc['metagame'][0]
    gen = metagame[3]
    format_name = metagame[4:]
    rating = raw.loc["cutoff"][0]

    df = raw[raw['data'].notna()]['data']

    top_mons = {}
    ix = list(df.index)

    for row in range(len(df)):
        if df[row]['usage'] >= .02:
            mon = ix[row]
            top_6 = list(dict(sorted(df[row]['Moves'].items(
            ), key=lambda item: item[1], reverse=True)))[:6]
            top_mons[mon] = [top_6, df[row]['usage']]

    cleaned = pd.DataFrame.from_dict(top_mons, orient='index').rename(
        columns={0: "Moves", 1: "Usage"})
    cleaned["Gen"] = gen
    cleaned["Format"] = format_name
    cleaned["Min Rating"] = rating
    return cleaned


# Data from 2014 was formatted slightly different so I made this method
def old_clean(path_to_json):

    
    
    numBattles = 0
    metagame = ''
    with open(path_to_json) as json_file:
        data = json.load(json_file)

        numBattles = data["info"]["number of battles"]
        metagame = data["info"]["metagame"]

    raw = pd.read_json(path_to_json)
    if(len(metagame) < 6 ):
        format_name = metagame
        gen = "6"
    else:
        metagame = raw.loc['metagame'][0]
        gen = metagame[3]
        format_name = metagame[4:]
    rating = raw.loc["cutoff"][0]

    df = raw[raw['data'].notna()]['data']

    top_mons = {}
    ix = list(df.index)

    for row in range(len(df)):
        if df[row]["Raw count"]/numBattles >= .001:
            mon = ix[row]
            top_6 = list(dict(sorted(df[row]['Moves'].items(
            ), key=lambda item: item[1], reverse=True)))[:6]
            top_mons[mon] = [top_6, df[row]["Raw count"]/numBattles]

    cleaned = pd.DataFrame.from_dict(top_mons, orient='index').rename(
        columns={0: "Moves", 1: "Usage"})
    cleaned["Gen"] = gen
    cleaned["Format"] = format_name
    cleaned["Min Rating"] = rating
    return cleaned
