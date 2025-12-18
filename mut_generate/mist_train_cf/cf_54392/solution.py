"""
QUESTION:
Create a function `exists_in_both(list1, list2, value)` that takes two lists and a value. Return `True` if the value is present in both lists, treating the lists as if they were sorted in non-ascending order. The function should work with any list length and value type that can be compared for equality.
"""

def exists_in_both(list1, list2, value):
    return value in list1 and value in list2