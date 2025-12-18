"""
QUESTION:
Write a function `get_next_element(lst)` that takes a list `lst` as input and returns the next element (i.e., the second element) in the list without modifying the original list. The function should have a time complexity of O(1) and should work with lists of any data type. If the list is empty or contains only one element, the function should return None.
"""

def get_next_element(lst):
    if len(lst) <= 1:
        return None
    return lst[1]