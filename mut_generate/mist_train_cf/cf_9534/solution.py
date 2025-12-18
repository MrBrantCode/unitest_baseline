"""
QUESTION:
Implement a function named bubble_sort that takes a list of integers as input and returns the sorted list using the bubble sort algorithm. The function should also minimize the number of comparisons by stopping early if no swaps are made during a pass.
"""

def bubble_sort(nums):
    """
    Sorts a list of integers using the bubble sort algorithm.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The sorted list of integers.
    """
    n = len(nums)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums