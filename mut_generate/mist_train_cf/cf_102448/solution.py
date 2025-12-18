"""
QUESTION:
Write a function called `apply_modification` that uses the "apply" function in pandas to modify a specific column in a DataFrame based on a condition. The function should add a suffix to all values in the specified column if they are greater than a specified threshold. Additionally, create another function called `calculate_department_average` that uses the "apply" function to calculate the average value for each group in a specified column, grouped by another column, and assign the result to a new column in the DataFrame. 

The function `apply_modification` should take in three parameters: the DataFrame, the column name to be modified, and the threshold value. The function `calculate_department_average` should take in three parameters: the DataFrame, the column name to calculate the average, and the column name to group by. The DataFrame should have columns 'name', 'department', and 'salary'. The functions should return the modified DataFrame.
"""

import pandas as pd

def apply_modification(df, column_name, threshold):
    """
    Modify a specific column in a DataFrame by adding a suffix to values greater than a specified threshold.

    Parameters:
    df (DataFrame): The input DataFrame.
    column_name (str): The name of the column to be modified.
    threshold (int): The threshold value.

    Returns:
    DataFrame: The modified DataFrame.
    """
    def add_suffix(value):
        if value > threshold:
            return str(value) + ' (High)'
        else:
            return str(value)

    df[column_name] = df[column_name].apply(add_suffix)
    return df

def calculate_department_average(df, value_column, group_column):
    """
    Calculate the average value for each group in a specified column, grouped by another column, 
    and assign the result to a new column in the DataFrame.

    Parameters:
    df (DataFrame): The input DataFrame.
    value_column (str): The name of the column to calculate the average.
    group_column (str): The name of the column to group by.

    Returns:
    DataFrame: The modified DataFrame with the new column.
    """
    df['average_salary'] = df.groupby(group_column)[value_column].transform('mean')
    return df