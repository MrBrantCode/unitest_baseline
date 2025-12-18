"""
QUESTION:
Write a function called `split_list_items` that takes a list of strings as input and returns a dictionary where the keys are the first character of each string in the list and the values are the remaining characters.
"""

def split_list_items(lst):
    return {item[0]: item[1:] for item in lst}