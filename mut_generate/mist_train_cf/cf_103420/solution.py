"""
QUESTION:
Create a function named `sort_animal_data` that takes a list of dictionaries as input where each dictionary contains 'animal', 'age', and 'weight' keys. The function should return a Pandas DataFrame created from the input list and sorted in descending order based on the 'animal' column.
"""

import pandas as pd

def sort_animal_data(data):
    """
    Create a Pandas DataFrame from a list of dictionaries and sort it based on the 'animal' column in descending order.

    Args:
        data (list): A list of dictionaries where each dictionary contains 'animal', 'age', and 'weight' keys.

    Returns:
        pd.DataFrame: A Pandas DataFrame sorted in descending order based on the 'animal' column.
    """
    return pd.DataFrame(data).sort_values('animal', ascending=False)