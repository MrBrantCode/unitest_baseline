"""
QUESTION:
Implement a function `double_grouped_data` that takes a grouped data frame as input and returns a modified data frame. The function should double the values in the `x` column of each group and preserve the group identifier in the `g` column. The input data frame is already grouped by the `g` column. The function should work with any number of groups and any type of data in the `x` column that supports multiplication by 2.
"""

from pandas import DataFrame

def double_grouped_data(grouped_df):
    return grouped_df.apply(lambda x: x.assign(x=x['x']*2))