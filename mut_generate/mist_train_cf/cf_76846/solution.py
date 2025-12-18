"""
QUESTION:
Create a function `sort_dict_by_value` that takes a dictionary as input and returns a new dictionary sorted in ascending order based on the numerical values. The function should be efficient enough to handle dictionaries with at least 1,000,000 items and handle cases with both positive and negative values, as well as duplicate values. The function should return a dictionary with the keys arranged in ascending order for duplicate values.
"""

def sort_dict_by_value(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))