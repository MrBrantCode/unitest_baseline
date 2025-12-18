"""
QUESTION:
Create a function named `unique_values` that takes two lists `list1` and `list2` as input and returns a new list containing the unique values from both inputs. The function should remove duplicates and the order of elements in the output list is not specified.
"""

def unique_values(list1, list2):
    return list(set(list1 + list2))