"""
QUESTION:
Implement a function `list_difference(lst1, lst2)` that takes two lists of integers as input and returns a new list containing elements present in `lst1` but not in `lst2`. The solution should have a time complexity of O(n).
"""

def list_difference(lst1, lst2):
    set_1 = set(lst1)
    set_2 = set(lst2)
    difference = set_1 - set_2
    return list(difference)