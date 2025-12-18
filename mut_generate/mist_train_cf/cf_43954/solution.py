"""
QUESTION:
Convert a Scikit-learn Bunch object to a Pandas DataFrame.

Create a function named `convert_bunch_to_df` that takes a Scikit-learn Bunch object as input and returns a Pandas DataFrame. The Bunch object contains data in the 'data' key, target values in the 'target' key, and column names in the 'feature_names' key. The resulting DataFrame should have the column names from 'feature_names' and an additional column for the target values.
"""

import pandas as pd
import numpy as np

def convert_bunch_to_df(data):
    return pd.DataFrame(data=np.c_[data['data'], data['target']],
                        columns=list(data['feature_names']) + ['target'])