"""
QUESTION:
Write a function named `sort_even_indices` that takes a list `l` as input and returns a new list where the elements at the even indices are equal to the corresponding indices of `l` but sorted in ascending order, while the elements at the odd indices remain the same as in the original list. The function should not modify the original list.
"""

def sort_even_indices(l: list):
    even_items = [l[i] for i in range(0, len(l), 2)] 
    even_items.sort()

    for i, e in enumerate(even_items):
        l[2 * i] = e

    return l