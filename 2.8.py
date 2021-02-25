import pandas as pd
import numpy as np

def count_namesakes(df, k):
    tmp = df.groupby('second_name').size().reset_index(name='num')
    tmp = tmp[tmp['num'] >= k]
    return tmp['num'].count()