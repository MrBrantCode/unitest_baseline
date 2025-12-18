"""
QUESTION:
Create a Python function named `verify_even_indices` that takes a list of integers as input. The function should return `True` if all elements at even indices in the list are even numbers, and `False` otherwise.
"""

def verify_even_indices(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True