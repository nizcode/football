import pandas as pd
from pandas.io.json import json_normalize
import json
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('StatsBombData/data/three-sixty') if isfile(join('StatsBombData/data/three-sixty', f))]

dfs = []
for i,j in enumerate(onlyfiles):
    #Load in all match events
    with open('StatsBombData/data/events/'+j) as data_file:
        #print (mypath+'events/'+file)
        data = json.load(data_file)
    with open('StatsBombData/data/three-sixty/' + j) as data_file:
    # print (mypath+'events/'+file)
        data1 = json.load(data_file)
    dfe = json_normalize(data, sep="_").assign(match_id=j[:-5])
    dfp = json_normalize(data1, sep="_").assign(match_id=j[:-5])
    shots = dfe.loc[dfe['type_name'] == 'Shot']
    shotsp = pd.merge(dfe,dfp.loc[dfp.isin(dfe['id']), :])
    dfs[i] = shotsp
outdf = pd.concat(df.set_index('id') for df in dfs)
jsondf = outdf.to_json("combined.json")