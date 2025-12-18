"""
QUESTION:
Write a function `apply_sigmoid` that takes a pandas DataFrame `df` as input and returns the DataFrame with sigmoid values of each existing column appended to it. The new columns should be named based on the original column names with a 'sigmoid_' prefix. The sigmoid function should be applied element-wise to each column. The function should not modify the original DataFrame and should not use any loops.
"""

import numpy as np
import pandas as pd

def apply_sigmoid(df):
    return pd.concat([df, df.apply(lambda x: 1 / (1 + np.exp(-x))).add_prefix('sigmoid_')], axis=1)