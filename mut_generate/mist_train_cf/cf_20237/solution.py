"""
QUESTION:
Write a function named `remove_duplicates_and_sort_desc` that takes a list of integers as input and returns a new list containing the unique numbers from the input list, sorted in descending order. The input list can contain up to 10^6 elements, and the solution must have a time complexity of O(n log n) or better.
"""

def remove_duplicates_and_sort_desc(nums):
    """
    Removes duplicates from a list of integers and returns a new list containing the unique numbers in descending order.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of unique integers in descending order.
    """
    return sorted(list(set(nums)), reverse=True)