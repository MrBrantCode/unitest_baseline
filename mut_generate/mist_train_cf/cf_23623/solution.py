"""
QUESTION:
Write a function to sort a list of n elements using Insertion Sort.
"""

def insertion_sort(lst):
    """
    This function sorts a list of n elements using Insertion Sort.
    
    Args:
        lst (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst