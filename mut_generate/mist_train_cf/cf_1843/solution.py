"""
QUESTION:
Write a function `get_max_key(dictionary)` that returns the key of the maximum element in the dictionary without using the built-in max() function or any other sorting functions, and without iterating over the dictionary more than once.
"""

def entrance(dictionary):
    max_key = None
    max_value = float('-inf')

    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value

    return max_key