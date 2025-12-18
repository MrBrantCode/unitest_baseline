"""
QUESTION:
Create a function `remove_duplicates(lst)` that takes a list `lst` as input and returns a new list with duplicate elements removed. The function should use list comprehension and have a time complexity less than O(n^2) and a space complexity of O(1). The solution should not use any built-in Python functions or methods related to duplicate removal or list manipulation.
"""

def remove_duplicates(lst):
    return [x for i, x in enumerate(lst) if x not in lst[:i]]