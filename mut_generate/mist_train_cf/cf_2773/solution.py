"""
QUESTION:
Implement a function named `custom_sort` that takes an array of integers as input and adds the numbers 2, 4, and 5 to the array. The array should not be empty initially and must have a size of 5. After adding the numbers, sort the array in ascending order using a custom sorting algorithm and return the sorted array. If the array is empty or not of size 5, raise an exception.
"""

def custom_sort(arr):
    """
    Adds numbers 2, 4, and 5 to the input array, then sorts it in ascending order using a custom sorting algorithm.
    
    Args:
    arr (list): Input array of integers. The array should not be empty and must have a size of 5.
    
    Returns:
    list: The sorted array.
    
    Raises:
    Exception: If the array is empty or not of size 5.
    """
    
    # Check if array is empty or not of size 5
    if len(arr) != 5:
        raise Exception("Array should not be empty and must have a size of 5")
    
    # Add numbers 2, 4, and 5 to the array
    arr.extend([2, 4, 5])
    
    # Custom sorting algorithm (Bubble Sort implementation)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr