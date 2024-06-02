import json
import pandas as pd
from itertools import groupby
from operator import itemgetter

df = pd.read_csv("data.csv", usecols=["Items","ImageURL","Categories","Ratio"])
df = df.to_dict(orient="records")

grouped_data = {}
for k, v in groupby(df, key=itemgetter('Categories')):
    v = list(v)
    new_v = []
    for i in v:
        del i["Categories"]
        new_v.append(i)
    lenght = len(new_v)
    grouped_data[k] = {
        "lenght": lenght,
        "data": new_v
    }


response = {
    "Sword": grouped_data["Sword"],
    "Accessory": grouped_data["Accessory"],
    "Material": grouped_data["Material"],
    "Stone": grouped_data["Stone"],
    "GamePass": grouped_data["GamePass"],
}
with open("index.html", "w") as f:
    json.dump(response, f)