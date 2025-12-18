"""
QUESTION:
Implement a function `custom_groupby_size` that takes a DataFrame, a list of columns to group by, and a list of columns to count, and returns a new DataFrame with the grouped data and the count of occurrences for each group. The function should replicate the behavior of the pandas `groupby` and `size` functions.

Function Signature: `def custom_groupby_size(data: pd.DataFrame, group_cols: List[str], count_cols: List[str]) -> pd.DataFrame:`

Input:
- `data`: A pandas DataFrame containing the data to be grouped and counted.
- `group_cols`: A list of strings representing the columns to group by.
- `count_cols`: A list of strings representing the columns to count.

Output:
- A pandas DataFrame containing the grouped data and the count of occurrences for each group.
"""

import pandas as pd
from typing import List

def custom_groupby_size(data: pd.DataFrame, group_cols: List[str], count_cols: List[str]) -> pd.DataFrame:
    grouped = data.groupby(group_cols)
    if count_cols:
        result = grouped[count_cols].size().reset_index(name='count')
    else:
        result = grouped.size().reset_index(name='count')
    return result