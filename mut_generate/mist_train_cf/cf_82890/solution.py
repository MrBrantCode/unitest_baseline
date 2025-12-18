"""
QUESTION:
Write a function `count_unique` that takes an array of integers and its size as input and returns the number of distinct integers in the array. The function should be efficient and handle duplicate integers correctly.
"""

def count_unique(array, n):
    """
    This function takes an array of integers and its size as input and returns the number of distinct integers in the array.

    Parameters:
    array (list): A list of integers.
    n (int): The size of the array.

    Returns:
    int: The number of unique integers in the array.
    """
    unique = set()
    
    for i in range(n):
        # Add integer to set. If integer is already in set, it will not be added again.
        unique.add(array[i])
    
    return len(unique)  # Number of unique elements equals the size of the set.