"""
QUESTION:
Create a function named `count_items` that takes in a dictionary as a parameter. The function should return two values: the number of unique values in the dictionary (excluding keys) and a list of all the keys in the dictionary that have a unique value.
"""

def count_items(dictionary):
    values = list(dictionary.values())
    unique_values = set(values)
    unique_keys = [key for key, value in dictionary.items() if values.count(value) == 1]
    return len(unique_values), unique_keys