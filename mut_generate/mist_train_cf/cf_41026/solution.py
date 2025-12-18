"""
QUESTION:
Implement a function `fillna_and_transform` that takes a pandas DataFrame `dataTable` as input, fills all NaN values with 0, unstacks the DataFrame, and adds 1 to each value. The function should return the transformed DataFrame.
"""

import pandas as pd

def fillna_and_transform(dataTable: pd.DataFrame) -> pd.DataFrame:
    dataTable.fillna(0, inplace=True)  # Fill NaN values with 0
    transformed_data = (dataTable.stack() + 1).unstack()  # Unstack the DataFrame and add 1 to each value
    return transformed_data