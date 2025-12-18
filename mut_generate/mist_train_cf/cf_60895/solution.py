"""
QUESTION:
Create a function `reorder_dict` that takes a dictionary as input, sorts its items based on their values in ascending order, and returns the sorted dictionary.
"""

def reorder_dict(my_dict):
    my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
    return my_dict