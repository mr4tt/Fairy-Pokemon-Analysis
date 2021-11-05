import pandas as pd
pd.set_option('display.max_columns', None)


def cleanTxt(csvfile, txtfile, minRating):

    new_df = pd.DataFrame()
    df = pd.read_csv(csvfile)
    f = open(txtfile, "r").read()
    f = f.replace(' ', '')
    arr1 = f.split('\n')
    # first pokemon at arr1[5]
    # last pokemon at arr1[len(arr)-3]
    arr2 = arr1[5].split('|')
    # ['', '1', 'Starmie', '37.22067%', '533', '37.221%', '479', '38.259%', '']

    for i in range(df.shape[0]):
        df.at[i,'Min Rating'] =  minRating

    for i in range(5, len (arr1) - 2):
        arr2 = arr1[i].split('|')
        poke = arr2[2]
        index = df.index
        condition = df["name"] == poke
       

        
        usage = float(arr2[3][:-1])/100
        if(usage < .02):
            break
        else:
            try:
                ind = index[condition].tolist()[0]
            except:
                print(poke)
                continue
            df.at[ind, "Usage"] = usage
            # print(df.iloc[ind])
            new_df = new_df.append(df.iloc[ind])

    return new_df

"""
gen = "5"
format = "uu"
rating = "0"

ans = cleanTxt("Pokemon Usage\Oldest Data\data\gen" + gen +"\gen" + gen + format + "-" + rating,"Pokemon Usage\Oldest Data\ow-txt\gen" + gen + "\gen" +gen + format +"-" + rating + ".txt", int(rating) )

print(ans.shape)
ans = ans[['name', "Moves","Usage","Gen","Format","Min Rating"]]
ans.to_csv("Pokemon Usage\Oldest Data\data-txt\gen" + gen +"\gen" + gen + format + "-" + rating,  index=False)
"""


gen = "6"
format = "uu"
rating = "1760"
ans = cleanTxt("Pokemon Usage\Oldest Data\data\gen" + gen +"\\" + format + "-" + rating,"Pokemon Usage\Oldest Data\ow-txt\gen" + gen + "\\" + format +"-" + rating + ".txt", int(rating) )

print(ans.shape)
ans = ans[['name', "Moves","Usage","Gen","Format","Min Rating"]]
ans.to_csv("Pokemon Usage\Oldest Data\data-txt\gen" + gen +"\gen" + gen + format + "-" + rating,  index=False)
