"""
QUESTION:
Write a function named `swap_entries` that takes a list of elements as input and returns the list with its entries reversed. The function should only use one temporary variable to store the value of one entry during the swapping process. The function should modify the original list and return the modified list.
"""

def swap_entries(lst):
    n = len(lst)
    for i in range(n // 2):
        temp = lst[i]
        lst[i] = lst[n - 1 - i]
        lst[n - 1 - i] = temp
    return lst