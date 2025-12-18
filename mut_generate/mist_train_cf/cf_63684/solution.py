"""
QUESTION:
Create a function `convert_to_dict(lst)` that takes a list `lst` of strings as input and returns a dictionary where each unique item in the list (case-insensitive) is a key and its corresponding value is the index of its first occurrence in the list.
"""

def convert_to_dict(lst):
    result = {}
    for i, item in enumerate(lst):
        lower_item = item.lower()
        if lower_item not in result:
            result[lower_item] = i
    return result