"""
QUESTION:
Implement the insertion sort algorithm in a function named `insertion_sort` that takes a list of integers as input and returns the sorted list. The function should sort the list in ascending order.
"""

def insertion_sort(nums):
    """
    Sorts a list of integers in ascending order using the Insertion Sort algorithm.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: The sorted list of integers.
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums