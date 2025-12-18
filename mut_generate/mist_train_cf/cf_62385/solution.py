"""
QUESTION:
Write a Python function, `calculate_std_dev`, that takes a list of integers as input and returns the standard deviation of the numbers in the list using the pandas library. The function should not take any other parameters.
"""

import pandas as pd

def calculate_std_dev(data):
    """
    Calculate the standard deviation of a list of numbers.

    Parameters:
    data (list): A list of integers.

    Returns:
    float: The standard deviation of the numbers in the list.
    """
    df = pd.DataFrame(data, columns=['Numbers'])
    return df['Numbers'].std()