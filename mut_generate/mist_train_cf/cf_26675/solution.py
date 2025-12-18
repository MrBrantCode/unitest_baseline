"""
QUESTION:
Implement the `_group` and `_bundle_groups` functions as follows:

- `_group(data, step=4)`: Takes a pandas DataFrame `data` and an optional parameter `step` (default value is 4). It adds a new column 'type' to the DataFrame, categorizing rows into 'data' or 'target' based on the value of `step`. If the row index is a multiple of `step`, it is categorized as 'target'; otherwise, it is categorized as 'data'. The function then removes any temporary columns and returns the modified DataFrame.

- `_bundle_groups(data, index, group_size)`: Takes a pandas DataFrame `data`, an integer `index`, and an integer `group_size`. It returns a NumPy array containing the concatenated values of the rows in the DataFrame `data` starting from the given `index` and spanning `group_size` rows.
"""

import pandas as pd
import numpy as np

def group(data, step=4):
    data['type'] = ['data' if (index+1)%step != 0 else 'target' for index, _ in data.iterrows()]
    data['type'] = data['type'].astype('category')
    return data

def bundle_groups(data, index, group_size):
    return np.concatenate([data.iloc[index + a].values for a in range(0, group_size)])