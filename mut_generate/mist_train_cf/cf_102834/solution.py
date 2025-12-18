"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of integers as input, removes any duplicate elements, and returns the array in ascending order. The function should be able to handle any array of integers.
"""

def remove_duplicates(arr):
    """
    Removes duplicates from the given array of integers and returns the array in ascending order.
    
    Parameters:
    arr (list): The input array of integers.
    
    Returns:
    list: The array with duplicates removed and sorted in ascending order.
    """
    return sorted(set(arr))