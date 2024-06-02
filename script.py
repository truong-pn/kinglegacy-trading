import json
import pandas as pd
from itertools import groupby
from operator import itemgetter

df = pd.read_csv("data.csv", usecols=["Items","ImageURL","Categories","Ratio"])
df = df.to_dict(orient="records")

for k, v in groupby(df, key=itemgetter('Categories')):
    v = list(v)
    new_v = []
    for i in v:
        del i["Categories"]
        new_v.append(i)
    lenght = len(new_v)
    with open(f"{k}.html", "w") as f:
        response = {
            "lenght": lenght,
            "data": new_v
        }
        json.dump(response, f)
