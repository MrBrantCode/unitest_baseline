"""
QUESTION:
Create a function named `parse_json_data` that takes a list of JSON objects as input and returns a Pandas DataFrame. The JSON objects contain personal data with nested address objects and phone numbers. The function should handle missing values by replacing them with 'Not provided'. 

The JSON objects have the following structure:
- name: string
- age: string
- address: object with street, city, state, country, and postal_code properties
- phone_numbers: object with work, home, and mobile properties

The function should use the pandas library to parse the JSON data into a DataFrame.
"""

import pandas as pd

def parse_json_data(data):
    """
    This function takes a list of JSON objects as input and returns a Pandas DataFrame.
    The JSON objects contain personal data with nested address objects and phone numbers.
    The function handles missing values by replacing them with 'Not provided'.

    Parameters:
    data (list): A list of JSON objects

    Returns:
    pandas.DataFrame: A DataFrame containing the parsed data
    """
    
    # Normalize the json data
    df = pd.json_normalize(data, sep='_')
    
    # Replace NaN values with 'Not provided'
    df.fillna('Not provided', inplace=True)
    
    return df