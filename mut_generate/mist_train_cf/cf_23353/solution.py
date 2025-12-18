"""
QUESTION:
Write a function named `find_minimum` that takes a list of integers as input and returns the minimum element in the list. The list is not empty and contains only integers. The function should use a divide and conquer approach to achieve better efficiency.
"""

def find_minimum(nums):
    """
    This function finds the minimum element in a list of integers using a divide and conquer approach.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The minimum element in the list.
    """

    # Base case: If the list contains only one element, return that element
    if len(nums) == 1:
        return nums[0]

    # Find the middle index of the list
    mid = len(nums) // 2

    # Recursively find the minimum element in the left and right halves
    left_min = find_minimum(nums[:mid])
    right_min = find_minimum(nums[mid:])

    # Return the minimum of the two halves
    return min(left_min, right_min)