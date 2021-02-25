import pandas as pd
import numpy as np

def find_null_columns(df):
    #ss = df.isnull.sum(axis=0)
    res = list()
    for d in df.columns:
        if df[d].isnull().sum() > 0:
            res.append(d)
    return res
