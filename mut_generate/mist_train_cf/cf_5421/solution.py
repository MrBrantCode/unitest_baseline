"""
QUESTION:
Write a function named `calculate_income_average` that takes a pandas DataFrame `df` as input. The function should count the number of rows where 'Country' is 'United States', 'State' is 'California', 'Gender' is 'Female', and 'Age' is less than or equal to 30. It should also calculate the average 'Income' of these rows. The function should return the count and the average income.
"""

import pandas as pd

def calculate_income_average(df: pd.DataFrame) -> tuple:
    """
    This function calculates the count and average income of rows in a DataFrame 
    where 'Country' is 'United States', 'State' is 'California', 'Gender' is 'Female', 
    and 'Age' is less than or equal to 30.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    tuple: A tuple containing the count and the average income.
    """

    # Filter the DataFrame based on the specified conditions
    filtered_df = df[(df['Country'] == 'United States') & (df['State'] == 'California') & (df['Gender'] == 'Female') & (df['Age'] <= 30)]

    # Count the number of rows with specified conditions
    count = len(filtered_df)

    # Calculate the average of the 'Income' column for remaining rows
    average_income = filtered_df['Income'].mean()

    return count, average_income