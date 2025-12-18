"""
QUESTION:
Write a function named `fourth_largest_number` that takes a list of integers as input and returns the fourth largest number in the list. The list is guaranteed to have at least 4 elements.
"""

def fourth_largest_number(nums):
    """
    Returns the fourth largest number in a list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The fourth largest number in the list.
    """
    # Sort the list in descending order
    nums.sort(reverse=True)
    
    # Return the fourth largest number
    return nums[3]