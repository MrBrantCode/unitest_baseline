"""
QUESTION:
Write a function `dict_cumulative_sum` that takes a multi-tiered dictionary as input. The dictionary can contain nested dictionaries, lists, and integer values. The function should return the cumulative sum of all integer values encountered in the dictionary. Note that the function should handle only integer values and return 0 for non-integer and non-collection values.
"""

def dict_cumulative_sum(data):
    if isinstance(data, dict):
        return sum(dict_cumulative_sum(val) for val in data.values())
    elif isinstance(data, list):
        return sum(dict_cumulative_sum(val) for val in data)
    elif isinstance(data, int):
        return data
    else:
        return 0