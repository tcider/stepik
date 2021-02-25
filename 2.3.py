import pandas as pd
import numpy as np


def calculate_statistics(df, ticket_ids):
    res = dict()
    tmp = df.query('ticket_id in @ticket_ids')
    res['mean'] = tmp.price.mean()
    res['median'] = tmp.price.median()
    res['std'] = tmp.price.std()

    return res