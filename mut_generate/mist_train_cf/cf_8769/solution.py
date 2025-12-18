"""
QUESTION:
Create a function named `reverse_list` that takes a list of integers as input and reverses the order of its elements. The function should not use the built-in `reverse()` method, the `[::-1]` slicing syntax, or any temporary data structures such as lists or arrays. It should only use basic operations like swapping elements, indexing, and iteration. The function must correctly handle empty lists, lists with duplicate elements, lists with negative integers, and very large lists with more than 1 million elements.
"""

def reverse_list(lst):
    # Check if the list is empty
    if len(lst) == 0:
        return []

    # Get the length of the list
    n = len(lst)

    # Swap elements to reverse the list
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

    return lst