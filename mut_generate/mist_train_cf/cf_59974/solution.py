"""
QUESTION:
Create a function called `total_match(lst1, lst2, case_sensitive=False)` that takes in two lists of strings (`lst1` and `lst2`) and an optional parameter `case_sensitive` which defaults to `False`. The function should remove non-alphanumeric characters from the strings, convert them to lowercase if `case_sensitive` is `False`, eliminate duplicate strings while preserving the original order, and return the list with a lesser or equal sum of character lengths. If both lists have an equal total character length, the function should return the first list.
"""

import re

def total_match(lst1, lst2, case_sensitive=False):
    """
    The function takes in two iterables of alphanumeric strings and returns the iterable with a total character length 
    (disregarding white spaces and non-alphanumeric characters) that's less or equal to the other iterable's length, 
    maintaining the original order of the elements in each iterable.

    The function also drops duplicate strings from both lists, keeping only the first occurrence of each string. Text case is ignored during string evaluations by default. This can be modified by setting the case sensitive parameter to True.

    Should both iterables have an equal total character length, the function returns the first iterable.
    """
    lst1 = [re.sub(r'\W+', '', s).lower() if not case_sensitive else re.sub(r'\W+', '', s) for s in lst1]
    lst2 = [re.sub(r'\W+', '', s).lower() if not case_sensitive else re.sub(r'\W+', '', s) for s in lst2]
    lst1, lst2 = list(dict.fromkeys(lst1)), list(dict.fromkeys(lst2))
    return lst1 if sum(len(s) for s in lst1) <= sum(len(s) for s in lst2) else lst2