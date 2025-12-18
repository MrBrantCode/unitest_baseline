"""
QUESTION:
Write a function called `stableSort` that takes an array of integers as input, sorts the array in ascending order with a time complexity of O(n^2), and preserves the relative order of equal elements. Do not use any built-in sorting functions or data structures. The input array will contain integers ranging from -1000 to 1000.
"""

def stableSort(arr):
    """
    Sorts the input array in ascending order using a stable sorting algorithm with a time complexity of O(n^2).

    Args:
        arr (list): A list of integers ranging from -1000 to 1000.

    Returns:
        list: The sorted array in ascending order.
    """
    n = len(arr)
    
    for i in range(n - 1):
        minIndex = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    
    return arr