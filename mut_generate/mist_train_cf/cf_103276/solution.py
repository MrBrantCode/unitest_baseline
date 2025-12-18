"""
QUESTION:
Implement a function called `bubble_sort` that manually sorts a given list of numbers in ascending order without using any built-in sorting functions. The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort(nums):
    """
    This function manually sorts a given list of numbers in ascending order using the bubble sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                # Swap nums[j] and nums[j + 1]
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums