"""
QUESTION:
Implement a function `get_school_year_extremes` that takes a pandas DataFrame `df` with a datetime index and returns a new DataFrame containing the 4 first and 4 last days of the school year, along with their corresponding data. The function should sort the input DataFrame by date before extracting the first and last days. The school year may not align with the calendar year. The input DataFrame is already sorted by date.
"""

import pandas as pd

def get_school_year_extremes(df: pd.DataFrame) -> pd.DataFrame:
    # Sort the DataFrame by date
    df = df.sort_index()

    # Get the first and last 4 days of the school year
    first_days = df.head(4)
    last_days = df.tail(4)

    # Concatenate the first and last days into a new DataFrame
    result = pd.concat([first_days, last_days])

    return result