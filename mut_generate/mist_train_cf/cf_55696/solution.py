"""
QUESTION:
Create a function named `rearrange_dict` that takes a dictionary as input and returns a new dictionary with the same key-value pairs rearranged in ascending order based on the integer values. The function should use the dictionary's numerical entities as the sorting criteria.
"""

def rearrange_dict(my_dict):
    return dict(sorted(my_dict.items(), key=lambda item: item[1]))