"""
QUESTION:
Create a function called `calculate_time_spent` that takes a dictionary of habits as input. The dictionary should have habit names as keys and another dictionary with 'Frequency', 'Duration', and 'Score' as values. The function should return a Pandas DataFrame that includes a new column called "Time Spent" which measures the amount of time in minutes spent daily for each of the given habits. The DataFrame should be sorted in descending order of "Score" and "Time Spent".
"""

import pandas as pd

def calculate_time_spent(habits):
    df = pd.DataFrame.from_dict(habits, orient='index')
    df['Time Spent'] = df['Frequency'] * df['Duration']
    return df.sort_values(by=['Score', 'Time Spent'], ascending=False)