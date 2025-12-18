"""
QUESTION:
Write a function `find_common_keys(dictionary, lst)` that takes a dictionary and a list as parameters. Return a new list containing the keys from the dictionary that are also present in the list, sorted in ascending order.
"""

def find_common_keys(dictionary, lst):
    return sorted([key for key in dictionary if key in lst])