"""
QUESTION:
Develop a function named `sum_values` that takes a dictionary as input and returns the sum of all its values, including those in nested dictionaries. The input dictionary can contain integers as values and nested dictionaries. If the input is not a dictionary, return 0.
"""

def sum_values(my_dict):
    if isinstance(my_dict, dict):
        return sum(sum_values(v) if isinstance(v, dict) else v for v in my_dict.values())
    else:
        return 0