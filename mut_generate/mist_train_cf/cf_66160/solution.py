"""
QUESTION:
Implement a function `data_cleaning` that takes a pandas DataFrame as input, removes duplicate rows, and drops any rows with null values. The function should return the cleaned DataFrame. 

Also, analyze the cleaned DataFrame to find the average trip duration, most popular starting point, and least popular ending point. The DataFrame columns for trip duration, starting point, and ending point are 'tripduration', 'start station id', and 'end station id' respectively. 

Finally, visualize the average trip duration, top 10 most popular starting locations, and top 10 least popular ending locations using suitable plots.
"""

import pandas as pd

def data_cleaning(dataframe):
    # Dealing with duplicate values
    dataframe.drop_duplicates(keep='first', inplace=True)

    # Dealing with null values. Here it's assuming we'll just drop the rows with any null values.
    dataframe.dropna(how="any", inplace=True)

    return dataframe