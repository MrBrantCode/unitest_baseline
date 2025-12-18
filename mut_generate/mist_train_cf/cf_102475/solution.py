"""
QUESTION:
Write a function `check_same_elements(list1, list2)` that checks if two lists have the same elements regardless of their order. The elements in the lists are strings consisting of lowercase letters only, with a length between 1 and 20 characters inclusive. The lists can have a maximum of 1000 elements. If the lists have the same elements, return True; otherwise, return False.
"""

def check_same_elements(list1, list2):
    return sorted(list1) == sorted(list2)