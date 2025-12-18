"""
QUESTION:
Create a function `convert_object_columns_to_string` that takes a pandas DataFrame `df` as input. The function should identify all columns containing object data types in `df` and convert them to string data types. Return the modified DataFrame with the same data as the input, but with all object columns cast as string data types.
"""

import pandas as pd

def convert_object_columns_to_string(df: pd.DataFrame) -> pd.DataFrame:
    object_cols = df.select_dtypes(include=['object']).columns
    df[object_cols] = df[object_cols].astype(str)
    return df