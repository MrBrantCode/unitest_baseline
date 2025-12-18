"""
ORIGINAL QUESTION:
Write a function called `check_lists` that takes two lists of strings as input, each containing lowercase letters only and having a length between 1 and 10 characters inclusive. The lists can have a maximum of 100 elements. The function should return True if the two lists have the same elements regardless of their order, and False otherwise.
"""

def check_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    return set(list1) == set(list2)