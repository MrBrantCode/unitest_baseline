"""
QUESTION:
Write a function `delete_keys_greater_than_n` that takes a dictionary and an integer `n` as input, and returns a new dictionary where all keys greater than `n` are removed. The dictionary keys are guaranteed to be integers and are sorted in ascending order. Implement this function in a way that achieves the most efficient time complexity possible.
"""

def delete_keys_greater_than_n(dictionary, n):
    return {key: value for key, value in dictionary.items() if key <= n}