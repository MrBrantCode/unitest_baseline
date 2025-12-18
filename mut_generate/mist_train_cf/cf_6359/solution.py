"""
QUESTION:
Implement the function `insertion_sort(lst)` to sort a list of positive integers in ascending order while preserving the original order of duplicate integers. The list may contain up to 100,000 elements. The function should return the sorted list.
"""

def insertion_sort(lst):
    """
    Sorts a list of positive integers in ascending order while preserving the original order of duplicate integers.
    
    Args:
        lst (list): A list of positive integers.
    
    Returns:
        list: The sorted list of integers.
    """
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst