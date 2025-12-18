"""
QUESTION:
Create a function named `is_sorted` that implements a sorting algorithm to check if an array is sorted in ascending order without using any built-in sorting functions. The function will be used to filter permutations of the array [7, 11, 19, 22] and return those that are sorted in ascending order. The function should take an array of integers as input and return a boolean value indicating whether the array is sorted.
"""

def is_sorted(array):
    """
    Checks if an array is sorted in ascending order.
    
    Args:
    array (list): A list of integers.
    
    Returns:
    bool: True if the array is sorted in ascending order, False otherwise.
    """
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True