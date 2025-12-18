"""
QUESTION:
Create a function called "calculate_time_spent" that takes a Pandas DataFrame as input. The DataFrame should have columns for "Frequency" and "Duration" and "Score". The function should add a new column called "Time Spent" which is the product of the "Frequency" and "Duration" columns. Then, sort the DataFrame in descending order by "Score" and "Time Spent". The input DataFrame is a dictionary that has been converted to a DataFrame using the "from_dict" method with the "orient" parameter set to 'index'.
"""

import pandas as pd

def calculate_time_spent(df):
    # Calculate the time spent for each habit
    df['Time Spent'] = df['Frequency'] * df['Duration']

    # Sort the DataFrame in descending order of "Score" and "Time Spent"
    df = df.sort_values(by=['Score', 'Time Spent'], ascending=False)

    return df