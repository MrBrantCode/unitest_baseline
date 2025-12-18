"""
QUESTION:
Create a function `select_data` that takes a Pandas DataFrame and a string of conditions as input. The function should filter the DataFrame based on the conditions and return the filtered DataFrame. The conditions should support at least two logical operators (e.g., AND, OR) and multiple conditions, as well as mathematical operations. The function should also handle cases where the specified columns in the conditions do not exist in the DataFrame.
"""

import pandas as pd

def select_data(df, conditions):
    try:
        return df.query(conditions)
    except pd.core.computation.ops.UndefinedVariableError:
        print(f"The specified conditions are not valid.")
        return None