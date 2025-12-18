"""
QUESTION:
Write a function `sort_and_remove_duplicates` that takes an array of integers as input and returns a new sorted array with no duplicates. The function should run in O(n log n) time and use O(n) space.
"""

def sort_and_remove_duplicates(arr):
    """
    Sorts an array of integers and removes duplicates in O(n log n) time and O(n) space.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        list: A new sorted list with no duplicates.
    """
    # Create a hash set to store unique elements
    unique_elements = set(arr)
    
    # Convert the hash set back into a list
    unique_list = list(unique_elements)
    
    # Sort the list using a standard sorting algorithm
    unique_list.sort()
    
    return unique_list