"""
QUESTION:
Write a function `solve` that takes a Scikit-learn Bunch object `data` as input and returns a Pandas DataFrame representation of the data. The DataFrame should have column names corresponding to the feature names in the Bunch object and an additional 'target' column for the labels.
"""

import pandas as pd
import numpy as np

def solve(data):
    return pd.DataFrame(data=np.c_[data['data'], data['target']],
                        columns=data['feature_names'] + ['target'])