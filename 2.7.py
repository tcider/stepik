import pandas as pd
import numpy as np

def find_popular(df, columns):
    columns2 = []
    for c in columns:
        if c not in columns2:
            columns2.append(c)
    tmp = df.copy()
    tmp = tmp[columns2].dropna()
    tmp = tmp.groupby(columns2).size().reset_index(name='new')
    if 'age' in columns2:
        tmp['age'] = tmp['age'].astype(int)
    if 'class' in columns2:
        tmp['class'] = tmp['class'].astype(int)
    try:
        s = tmp[columns2].iloc[tmp['new'].argmax()]
    except:
        return ''
    return s