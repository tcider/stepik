import pandas as pd
import numpy as np

def find_nearest(df, price):
    tmp = df.copy()
    tmp.price.dropna(inplace=True)
    tmp['new'] = abs(tmp['price'] - price)
    return df.iloc[tmp['new'].argmin()]