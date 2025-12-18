"""
QUESTION:
Create a function `create_position_column` that takes a pandas DataFrame as input with two columns 'Enter' and 'Exit'. The function should return a new column 'Position' in the DataFrame where 'Position' is 1 when 'Enter' is 1 and 'Position' remains 1 until 'Exit' is 1, at which point 'Position' becomes 0. If 'Enter' and 'Exit' occur at the same time, prioritize 'Exit' over 'Enter'. The function should handle overlapping 'Enter' and 'Exit' signals and should be vectorized to improve performance.
"""

import pandas as pd

def create_position_column(df):
    """
    Create a new column 'Position' in the DataFrame where 'Position' is 1 when 'Enter' is 1 
    and 'Position' remains 1 until 'Exit' is 1, at which point 'Position' becomes 0.

    Parameters:
    df (pd.DataFrame): DataFrame with 'Enter' and 'Exit' columns.

    Returns:
    pd.DataFrame: The input DataFrame with the added 'Position' column.
    """
    df['Position'] = 0
    position = 0

    for i in range(0, len(df)):
        if df['Enter'].iloc[i] == 1 and position == 0:
            position = 1
            df['Position'].iloc[i] = position
        elif df['Exit'].iloc[i] == 1 and position == 1:
            position = 0
            df['Position'].iloc[i] = position
        else:
            df['Position'].iloc[i] = position

    return df