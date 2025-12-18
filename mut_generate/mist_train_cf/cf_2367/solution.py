"""
QUESTION:
Create a function called `remove_duplicates` that takes a pandas DataFrame `df` as input and returns a new DataFrame with duplicate rows removed, while keeping track of the original index positions of the duplicates. The function should not use any built-in pandas functions or methods that directly handle duplicates, and it should have a time complexity of O(n^2), where n is the number of rows in the DataFrame.
"""

import pandas as pd

def remove_duplicates(df):
    duplicates = {}
    
    for i, row in df.iterrows():
        row_tuple = tuple(row)
        
        if row_tuple not in duplicates:
            duplicates[row_tuple] = [i]
        else:
            duplicates[row_tuple].append(i)
    
    unique_df = pd.DataFrame(columns=df.columns)
    
    for row_tuple, indices in duplicates.items():
        if len(indices) == 1:
            unique_df.loc[indices[0]] = list(row_tuple)
    
    return unique_df