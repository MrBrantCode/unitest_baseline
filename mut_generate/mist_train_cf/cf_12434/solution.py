"""
QUESTION:
Write a function `has_duplicate(lst)` that takes a list `lst` as input and returns `True` if the list contains any duplicate elements, and `False` otherwise. You cannot use additional data structures such as sets or dictionaries.
"""

def has_duplicate(lst):
    lst.sort()  # Sort the list in ascending order

    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:  # Check if current element is equal to the next element
            return True

    return False