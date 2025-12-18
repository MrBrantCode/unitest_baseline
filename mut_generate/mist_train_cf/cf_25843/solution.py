"""
QUESTION:
Create a function called `remove_nulls` that takes a dictionary as input. The function should recursively remove all key-value pairs where the value is `None` from a nested dictionary. Return the resulting dictionary with no 'null' values.
"""

def remove_nulls(dictionary):
    if isinstance(dictionary, dict):
        return {key: remove_nulls(value) 
                for key, value in dictionary.items() if value is not None}
    else:
        return dictionary