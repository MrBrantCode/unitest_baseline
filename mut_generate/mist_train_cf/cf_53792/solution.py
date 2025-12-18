"""
QUESTION:
Write a function called `top_correlations` that takes a pandas DataFrame and an integer `n` as input, and returns a pandas Series containing the top n pairs of most correlated columns in the DataFrame. If ties occur, return all of them. If the DataFrame is empty or `n` is zero, return an empty pandas Series.
"""

import pandas as pd
import numpy as np

def top_correlations(dataframe: pd.DataFrame, n: int) -> pd.Series:
    if dataframe.empty or n==0:
        return pd.Series()

    corr_matrix = dataframe.corr().abs()  
    upper_matrix = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))  

    sorted_correlations = upper_matrix.stack().sort_values(ascending=False)
    top_correlations = sorted_correlations[sorted_correlations == sorted_correlations.iloc[n-1]]

    return top_correlations