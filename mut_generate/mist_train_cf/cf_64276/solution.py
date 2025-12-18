"""
QUESTION:
Implement a function called `insertion_sort` that takes a list of integers as input and returns the sorted list using the Insertion Sort algorithm. The function should have a time complexity of O(n^2) for both average and worst-case scenarios and a space complexity of O(1) for auxiliary space.
"""

def insertion_sort(nums):
    """
    Sorts a list of integers using the Insertion Sort algorithm.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The sorted list of integers.
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums