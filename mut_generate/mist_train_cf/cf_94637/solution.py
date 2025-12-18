"""
QUESTION:
Implement a function `insertion_sort(arr, compare)` that sorts an array of integers in the order specified by the custom comparator function `compare`. The function should return the number of comparisons made during the sorting process. The function should sort the array in-place. The `compare` function is expected to take two integers as input and return `True` if the first integer should come before the second integer in the sorted array.
"""

def insertion_sort(arr, compare):
    """
    Sorts an array of integers in the order specified by the custom comparator function.
    
    Args:
        arr (list): The array to be sorted.
        compare (function): A custom comparator function that takes two integers as input and returns True if the first integer should come before the second integer in the sorted array.
    
    Returns:
        int: The number of comparisons made during the sorting process.
    """
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare(arr[j], key):
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons