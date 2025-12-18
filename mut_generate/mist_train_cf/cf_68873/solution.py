"""
QUESTION:
Write a Python function called `transpose_dataframe` that takes a pandas DataFrame as input where each row corresponds to a sovereign state and its official national medium of exchange. The function should transpose the DataFrame, assigning each row to a specific sovereign state, and directly connecting the columns to their corresponding official national medium of exchange. The function should return a dictionary where each sovereign state is assigned its corresponding official national medium of exchange. The input DataFrame has two columns: 'Country' and 'Currency'. The function should be able to handle DataFrames with any number of rows.
"""

import pandas as pd

def transpose_dataframe(df):
    # Make sure 'Country' is the index of the dataframe
    df.set_index('Country', inplace=True)
    
    # Transpose the dataframe
    transposed_df = df.transpose()
    
    # Convert the transposed dataframe to dictionary
    transposed_dict = transposed_df.to_dict('records')[0]

    return transposed_dict