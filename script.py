#pip install prettytable pandas
import json
import pandas as pd
from itertools import groupby
from operator import itemgetter
from prettytable import PrettyTable

df = pd.read_csv("data.csv")
df = df.to_dict(orient="records")

for k, v in groupby(df, key=itemgetter('Categories')):
    v = list(v)
    table = PrettyTable(["ID", "Item", "Ratio"])
    for index, i in enumerate(v):
        del i["ImageURL"]
        del i["Categories"]
        table.add_row([index+1, i["Items"], i["Ratio"]])

    with open(f"{k}.html", "w", encoding="utf-8") as f:
        f.write(str(table))
