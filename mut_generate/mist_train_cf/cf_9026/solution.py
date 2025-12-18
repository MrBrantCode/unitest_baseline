"""
QUESTION:
Write a Python function `compute_max_value` that takes a dictionary as input. The function should iterate over the dictionary, and for each key, it should check if the value is an integer and divisible by 3. If these conditions are met, the function should keep track of the maximum value for each key and return a dictionary with these maximum values. If a key has multiple values that meet the conditions, the function should only store the maximum value.
"""

def compute_max_value(dictionary):
    result = {}
    for key, value in dictionary.items():
        if isinstance(value, int) and value % 3 == 0:
            if key not in result or value > result[key]:
                result[key] = value
    return result