"""
QUESTION:
Write a function named `remove_duplicates_and_sort_desc` that takes an array of integers as input. Remove the duplicate elements from the array and sort the remaining elements in descending order. If the input array is empty or contains only one element, return the original array.
"""

def remove_duplicates_and_sort_desc(nums):
    """
    Removes duplicate elements from the input array and sorts the remaining elements in descending order.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of integers with duplicates removed and sorted in descending order.
    """
    return sorted(list(set(nums)), reverse=True)