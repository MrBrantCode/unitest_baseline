"""
QUESTION:
Create a function `process_crypto_data(df, sortby)` that takes a pandas DataFrame `df` and a string `sortby` as input. The function should process and format cryptocurrency data for display. 

If the DataFrame `df` is not empty and the `sortby` column is either "Market Cap [$]" or "Volume [$]", filter the DataFrame to include only rows where both "Volume [$]" and "Market Cap [$]" columns are not null, and then sort the DataFrame by the `sortby` column in descending order. Format the "Volume [$]" and "Market Cap [$]" columns to display large numbers in a readable format (e.g., 123456789 as 123.46B) and return the formatted DataFrame.

Restrictions: 
- The function should handle cases where the DataFrame is empty or the `sortby` column is not "Market Cap [$]" or "Volume [$]".
- The function should not modify the original DataFrame.
"""

import pandas as pd

def format_large_numbers(x):
    if x >= 1e12:
        return f"{x/1e12:.2f}T"
    elif x >= 1e9:
        return f"{x/1e9:.2f}B"
    elif x >= 1e6:
        return f"{x/1e6:.2f}M"
    elif x >= 1e3:
        return f"{x/1e3:.2f}K"
    else:
        return f"{x:.2f}"

def process_crypto_data(df: pd.DataFrame, sortby: str) -> pd.DataFrame:
    if not df.empty and sortby in ["Market Cap [$]", "Volume [$]"]:
        df = df.copy()
        df = df[(df["Volume [$]"].notna()) & (df["Market Cap [$]"].notna())].sort_values(by=sortby, ascending=False)
        for col in ["Volume [$]", "Market Cap [$]"]:
            if col in df.columns:
                df[col] = df[col].apply(format_large_numbers)
    return df