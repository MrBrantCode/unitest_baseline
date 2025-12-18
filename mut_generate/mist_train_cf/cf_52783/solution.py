"""
QUESTION:
Write a function `convert_date_format` that takes a pandas DataFrame column containing datetime strings in various formats as input and returns the same column with all datetime strings converted to the "dd.mm.yyyy" format. The column may contain datetime strings in formats such as "yyyy-mm-dd" and "dd.mm.yyyy".
"""

import pandas as pd

def convert_date_format(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name]).dt.strftime('%d.%m.%Y')
    return df[column_name]