"""
QUESTION:
Write a function `remove_duplicates` that takes a list as input and returns a new list containing all unique elements from the input list, without modifying the original list.
"""

def remove_duplicates(input_list):
    return [x for i, x in enumerate(input_list) if x not in input_list[:i]]