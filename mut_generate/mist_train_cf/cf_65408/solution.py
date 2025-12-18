"""
QUESTION:
Create a function `max_in_stride` that takes a pandas Series `s` and an integer `n` as input. The function should return a list of the maximum values in each subset of `n` consecutive values in `s`, in the order they appear in the original series.
"""

import pandas as pd

def max_in_stride(s, n):
    return [s[i:i+n].max() for i in range(0, len(s), n)]