"""
QUESTION:
Create a function named `reverse_list` that takes a list of integers as input and reverses it without using the built-in `reverse()` method, the `[::-1]` slicing syntax, or any temporary data structures such as lists or arrays. The function should only use basic operations like swapping elements, indexing, and iteration.
"""

def entrance(lst):
    if len(lst) == 0:
        return []

    n = len(lst)

    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

    return lst