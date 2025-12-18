"""
QUESTION:
Create a function named `create_dictionary` that takes two lists `list1` and `list2` as input. The function should return a dictionary where elements from `list1` are keys and elements from `list2` are values. The function should return an empty dictionary if `list1` and `list2` are not of equal length.
"""

def create_dictionary(list1, list2):
    if len(list1) != len(list2):
        return {}
    else:
        return dict(zip(list1, list2))