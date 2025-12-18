"""
QUESTION:
Implement a function named `insertion_sort` that sorts an array of n numbers in descending order using the insertion sort algorithm. The function should have a time complexity of O(n^2), handle edge cases such as already sorted arrays, duplicate numbers, and negative numbers, as well as floating-point numbers. The function should also count the number of comparisons made during the sorting process and return both the sorted array and the number of comparisons.
"""

def insertion_sort(arr):
    """
    Sorts an array in descending order using the insertion sort algorithm.

    Args:
    arr (list): A list of numbers to be sorted.

    Returns:
    tuple: A tuple containing the sorted array and the number of comparisons made during the sorting process.
    """
    comparisons = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        
        arr[j + 1] = key
        comparisons += 1
    
    return arr, comparisons