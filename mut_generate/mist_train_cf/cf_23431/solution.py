"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers using the bubble sort algorithm. The function should take a list of integers as input and return the sorted list. The input list should not be empty and should only contain integers.
"""

def bubble_sort(nums):
    """
    Sorts an array of integers using the bubble sort algorithm.

    Args:
        nums (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums