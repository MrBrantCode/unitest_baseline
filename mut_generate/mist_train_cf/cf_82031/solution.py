"""
QUESTION:
Construct a function called `construct_multi_index_df` that takes a list of tuples as input, where each tuple contains an integer, a dictionary with a "fruit" key, and another tuple containing a fruit color. The function should return a Pandas DataFrame with a multi-index, where the first level index is composed of the integer and the fruit type, and the second level index is the fruit color. Each level of the index should be labeled.
"""

import pandas as pd

def construct_multi_index_df(data):
    """
    Construct a Pandas DataFrame with a multi-index from a list of tuples.

    Parameters:
    data (list): A list of tuples containing an integer, a dictionary with a "fruit" key, and another tuple containing a fruit color.

    Returns:
    pd.DataFrame: A Pandas DataFrame with a multi-index, where the first level index is composed of the integer and the fruit type, and the second level index is the fruit color.
    """

    # Create a list to store the tuples
    tuples = []

    # Loop through each tuple from data
    for item in data:
        # Get the integer
        integer = item[0]
        
        # Get the fruit type from the dictionary
        fruit_type = item[1]['fruit']
        
        # Get the fruit color from the tuple
        fruit_color = item[2]
        
        # Add the tuple to the list
        tuples.append(((integer, fruit_type), fruit_color))

    # Create a Multi-Index
    index = pd.MultiIndex.from_tuples(tuples, names=[('integer', 'fruit'), 'color'])

    # Create a DataFrame
    df = pd.DataFrame(index=index)

    return df