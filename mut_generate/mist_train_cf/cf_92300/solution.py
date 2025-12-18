"""
QUESTION:
Write a function `has_duplicate` that takes a list as input and returns `True` if the list contains any duplicate elements, and `False` otherwise. You are not allowed to use additional data structures such as sets or dictionaries.
"""

def has_duplicate(lst):
    lst.sort()  # Sort the list in ascending order

    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:  # Check if current element is equal to the next element
            return True

    return False