"""
QUESTION:
Create a function called `format_data` that takes in a list of dictionaries representing table rows. Each dictionary must have the keys "Name", "Age", and "City". The function should return a JSON formatted string representing the table data. 

The function should be implemented using Python and utilize the `json` module.
"""

import json

def format_data(data):
    """
    This function takes in a list of dictionaries representing table rows.
    Each dictionary must have the keys "Name", "Age", and "City".
    The function returns a JSON formatted string representing the table data.

    Args:
        data (list): A list of dictionaries, each dictionary representing a table row.

    Returns:
        str: A JSON formatted string representing the table data.
    """
    return json.dumps(data)