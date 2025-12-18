"""
QUESTION:
Write a function named 'largest_number' that takes a list of integers as input and returns the sum of the two largest numbers in the list after sorting it in descending order.
"""

def largest_number(nums):
    """
    This function calculates the sum of the two largest numbers in a given list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of the two largest numbers in the list.
    """
    # Sort the list in descending order
    sorted_nums = sorted(nums, reverse=True)
    
    # Return the sum of the first two elements (the two largest numbers)
    return sum(sorted_nums[:2])