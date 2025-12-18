"""
QUESTION:
Create a function named `expand_lists_to_columns` that takes a Pandas Series containing lists of unequal lengths as input. The function should return a DataFrame where each list in the input Series has been expanded into separate columns. The columns should be named `code_0`, `code_1`, `code_2`, etc. If a list is not long enough to populate a column, the remaining cells in that column should be filled with NaNs.
"""

import pandas as pd

def expand_lists_to_columns(series):
    """
    Expand a Pandas Series containing lists of unequal lengths into a DataFrame.

    Parameters:
    series (pd.Series): A Pandas Series containing lists of unequal lengths.

    Returns:
    pd.DataFrame: A DataFrame where each list in the input Series has been expanded into separate columns.
    """
    result = pd.DataFrame(series.to_list())
    result.columns = ['code_' + str(col) for col in result.columns]
    return result