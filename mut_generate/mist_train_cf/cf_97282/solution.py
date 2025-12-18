"""
QUESTION:
Write a function `sum_of_numbers` that takes a JSON string as input, parses it into a Python object, and returns the sum of all the numbers in the value. The input JSON string can contain key-value pairs, where the key is a string and the value can be of any valid JSON data type (string, number, boolean, array, object, null). The function should handle nested arrays and objects. The function should not take any additional arguments besides the JSON string.
"""

import json

def sum_of_numbers(json_str):
    """
    This function calculates the sum of all numbers in a given JSON string.
    
    Args:
        json_str (str): A JSON string containing key-value pairs.
        
    Returns:
        int: The sum of all numbers in the JSON string.
    """

    def recursive_sum(obj):
        total = 0
        if isinstance(obj, dict):
            for value in obj.values():
                total += recursive_sum(value)
        elif isinstance(obj, list):
            for element in obj:
                total += recursive_sum(element)
        elif isinstance(obj, (int, float)):
            total += obj
        return total

    parsed_data = json.loads(json_str)
    return recursive_sum(parsed_data)