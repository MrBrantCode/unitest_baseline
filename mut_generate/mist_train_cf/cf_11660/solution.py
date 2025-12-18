"""
QUESTION:
Write a function `remove_and_sort` that takes an array of integers as input, removes any element that is greater than 10 and less than 20, and returns the remaining elements in descending order. The input array can contain duplicate elements.
"""

def remove_and_sort(arr):
    """
    Removes elements greater than 10 and less than 20 from the input array and returns the remaining elements in descending order.
    
    Parameters:
    arr (list): The input array of integers.
    
    Returns:
    list: The modified array with elements greater than 10 and less than 20 removed, sorted in descending order.
    """
    return sorted([num for num in arr if not 10 < num < 20], reverse=True)