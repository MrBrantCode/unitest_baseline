"""
QUESTION:
Write a function `pivot_json_data` that takes a pandas DataFrame with a 'Date' column and a 'message' column containing mixed data, including JSON strings, as input. The function should return a new DataFrame where the JSON data is extracted, transformed, and pivoted into a time series format. The resulting DataFrame should have the 'Date' column as the index and separate columns for each unique JSON key found in the 'message' column.
"""

import pandas as pd
import numpy as np
import ast

def pivot_json_data(df):
    # this will convert the string representation of dictionary to a dictionary
    df['message'] = df['message'].apply(lambda x: [ast.literal_eval(i) if i.startswith("{") else i for i in x])

    def split_and_explode(df, col):
        s = df[col]
        i = np.arange(len(s)).repeat(s.str.len())
        return df.iloc[i].assign(**{col: np.concatenate(s)})

    df = split_and_explode(df, 'message').reset_index(drop=True)

    json_rows = df[df['message'].apply(lambda x: isinstance(x, dict))]

    json_df = pd.json_normalize(json_rows['message'])
    json_df = pd.concat([json_rows.drop('message', axis=1).reset_index(drop=True), json_df.reset_index(drop=True)], axis=1)

    pivot_df = pd.pivot_table(json_df, index='Date', aggfunc='first')
    
    return pivot_df