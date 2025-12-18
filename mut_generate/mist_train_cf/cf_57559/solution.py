"""
QUESTION:
Write a function `max_elements_by_index` that takes two arrays `a` and `index` as input. The function should return an array of maximum values in `a` for each unique index in `index`. Assume that the length of `a` and `index` are the same, and the values in `index` are non-negative integers.
"""

import pandas as pd

def max_elements_by_index(a, index):
    df = pd.DataFrame({'a': a, 'index': index})
    return df.groupby('index')['a'].max().values