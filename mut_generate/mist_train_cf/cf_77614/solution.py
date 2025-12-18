"""
QUESTION:
Create a function `get_similar_rows` that takes a pandas DataFrame `df` and a `threshold` value as input, and returns a boolean mask indicating the rows in `df` that have at least 95% matching columns with another row. The function should consider a row to be a duplicate if at least 95% of its columns match with another row, regardless of which specific columns are matched.
"""

import pandas as pd
import numpy as np
import itertools

def get_similar_rows(df, threshold):
  mask = np.zeros(len(df), dtype=bool)
  for i,j in itertools.combinations(range(len(df)), 2):
    similarity = sum(df.iloc[i] == df.iloc[j]) / len(df.columns)
    if similarity >= threshold:
      mask[i] = True
      mask[j] = True
  return mask