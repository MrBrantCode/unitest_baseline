"""
QUESTION:
Implement a function named `bubble_sort_descending` that sorts a given list of integers in descending order using the bubble sort algorithm, with a time complexity of O(n^2). The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort_descending(nums):
    """
    Sorts a list of integers in descending order using the bubble sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list in descending order.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums