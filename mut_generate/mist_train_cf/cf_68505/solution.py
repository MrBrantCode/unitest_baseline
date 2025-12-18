"""
QUESTION:
Create a function called `process_df` that takes a pandas DataFrame as input, filters it to include only rows where 'Age' is greater than 18 and 'Country' is 'USA', sorts the result by 'Age' in descending order, then divides the sorted data into two separate DataFrames based on the first letter of 'Profession': one for professions starting with letters A-M and one for professions starting with letters N-Z. The function should return the sorted DataFrame and the two segmented DataFrames, along with the total count of records in each segmented DataFrame.
"""

import pandas as pd

def process_df(df):
    # Filter users who are above 18 and living in 'USA'
    filtered_df = df[(df['Age'] > 18) & (df['Country'] == 'USA')]

    # Sort these filtered data in descending order according to the 'Age' column
    sorted_df = filtered_df.sort_values(by='Age', ascending=False)

    # Divide these data into two separate DataFrames
    df_A_M = sorted_df[sorted_df['Profession'].str[0].between('A', 'M')]
    df_N_Z = sorted_df[sorted_df['Profession'].str[0].between('N', 'Z')]

    # Get the total count of records in each DataFrame
    count_A_M = df_A_M.shape[0]
    count_N_Z = df_N_Z.shape[0]

    # Return the sorted DataFrame, the two segmented DataFrames, and the respective count of records
    return sorted_df, df_A_M, df_N_Z, count_A_M, count_N_Z