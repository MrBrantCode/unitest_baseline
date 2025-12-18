"""
QUESTION:
Create a function `filter_and_format_date` that takes a pandas DataFrame `df` with a 'Date' column and a list of two dates `date_range`. Filter the DataFrame to include only rows where the 'Date' falls within the given date range (inclusive) and format the 'Date' column to display the day, abbreviated month name, year, and day of the week.
"""

import pandas as pd

def filter_and_format_date(df, date_range):
    """
    Filter a DataFrame to include only rows where the 'Date' falls within the given date range (inclusive)
    and format the 'Date' column to display the day, abbreviated month name, year, and day of the week.

    Parameters:
    df (pd.DataFrame): DataFrame with a 'Date' column
    date_range (list): List of two dates in the format 'dd-mmm-yyyy'

    Returns:
    pd.DataFrame: Filtered DataFrame with formatted 'Date' column
    """
    # Convert date range to datetime format for comparison
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])

    # Filter DataFrame to include only rows within the given date range
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Format the 'Date' column
    df['Date'] = df['Date'].dt.strftime('%d-%b-%Y %A')

    return df