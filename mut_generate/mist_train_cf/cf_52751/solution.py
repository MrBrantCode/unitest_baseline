"""
QUESTION:
Create a function `merge_rows` that takes a pandas DataFrame with a single column named 'text' as input. The function should merge every 3 rows of the 'text' column into a single row, with the merged values separated by commas, and return the resulting DataFrame.
"""

import pandas as pd

def merge_rows(df):
    merged_rows = []
    for i in range(0, len(df), 3):
        merged_rows.append(', '.join(df['text'].iloc[i:i+3]))
    result = pd.DataFrame({'text': merged_rows})
    return result