"""
QUESTION:
Write a function called `generate_table` that generates a tabular format given a list of dictionaries. The function should take a list of dictionaries as input, convert the data to JSON format, and return the JSON formatted string. The input list of dictionaries should represent a table, where each dictionary in the list represents a row in the table, and the keys of the dictionary represent the column names. 

The function should use the `json` module in Python to convert the list of dictionaries to JSON format. The function should not take any other inputs besides the list of dictionaries and should not return anything other than the JSON formatted string. 

For example, given the input `[{"Name": "John", "Age": 25, "City": "New York"}, {"Name": "Mary", "Age": 30, "City": "Los Angeles"}, {"Name": "Bob", "Age": 35, "City": "Chicago"}]`, the function should return a JSON formatted string representing the input data.
"""

import json

def generate_table(data):
    """
    This function generates a tabular format given a list of dictionaries.
    
    Args:
        data (list): A list of dictionaries where each dictionary represents a row in the table.
        
    Returns:
        str: A JSON formatted string representing the input data.
    """
    json_data = json.dumps(data)
    return json_data