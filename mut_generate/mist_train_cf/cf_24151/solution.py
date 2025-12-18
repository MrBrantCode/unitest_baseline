"""
QUESTION:
Implement a function named `bubble_sort` to sort a list of integers in ascending order using the bubble sort algorithm, which rearranges the list by comparing adjacent elements and swapping them if they are out of order, repeating this process until the list is sorted.
"""

def bubble_sort(nums):
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums