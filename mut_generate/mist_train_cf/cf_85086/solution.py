"""
QUESTION:
Design a Python function named `tuple_to_dict` that takes a tuple of integers as input and returns a nested dictionary where each element of the tuple becomes a key, and its value is a dictionary created from the rest of the elements in the tuple. The function should handle an empty tuple by returning an empty dictionary.
"""

def tuple_to_dict(input_tuple):
    if not input_tuple:  # If tuple is empty, return an empty dictionary
        return {}
    return {input_tuple[0]: tuple_to_dict(input_tuple[1:])} # recursive call with rest of the tuple