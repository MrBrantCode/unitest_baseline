"""
QUESTION:
Write a function called `split_list_items` that takes a list of strings as input and returns a dictionary where each key is the first character of each string and the value is the remaining characters of the corresponding string.
"""

def split_list_items(lst):
    return {item[0]: item[1:] for item in lst}