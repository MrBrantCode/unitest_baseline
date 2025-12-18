"""
QUESTION:
Implement the `bubble_sort` function, which sorts a list of integers in ascending order using the bubble sort algorithm. The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort(nums):
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums