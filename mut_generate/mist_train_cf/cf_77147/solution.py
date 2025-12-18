"""
QUESTION:
Write a function named `modify_quantity` that takes a pandas DataFrame as input. The function should randomly select 20% of the DataFrame's rows using `df.sample(n)` with `random_state` set to 0, and then modify the 'Quantity' column values of these selected rows to zero, while retaining their original indices.
"""

import pandas as pd

def modify_quantity(df):
    """
    Modify the 'Quantity' column values of 20% of the DataFrame's rows to zero.

    Parameters:
    df (pd.DataFrame): Input DataFrame.

    Returns:
    pd.DataFrame: DataFrame with modified 'Quantity' column.
    """
    subset_indexes = df.sample(frac=0.2, random_state=0).index
    df.loc[subset_indexes, 'Quantity'] = 0
    return df