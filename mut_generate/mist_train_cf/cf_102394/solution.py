"""
QUESTION:
Write a function `square_and_sort` that takes a list of integers as input, removes any negative numbers, squares each remaining number, sorts the transformed list in descending order, and returns the sorted list.
"""

def square_and_sort(nums):
    """
    This function takes a list of integers, removes any negative numbers, 
    squares each remaining number, sorts the transformed list in descending order, 
    and returns the sorted list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A sorted list of squared integers.
    """
    # Remove negative numbers and square each number
    squared_nums = [num ** 2 for num in nums if num >= 0]
    
    # Sort the transformed list in descending order
    squared_nums.sort(reverse=True)
    
    return squared_nums