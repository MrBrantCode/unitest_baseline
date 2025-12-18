"""
QUESTION:
Write a function called "nested_dict_sum" to calculate the sum of values stored in a nested dictionary with an arbitrary number of levels. The function should recursively traverse the dictionary, adding integer values to the sum and recursively summing the values in any nested dictionaries.
"""

def nested_dict_sum(nested_dict):
    total_sum = 0

    for key, value in nested_dict.items():
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, dict):
            total_sum += nested_dict_sum(value)

    return total_sum