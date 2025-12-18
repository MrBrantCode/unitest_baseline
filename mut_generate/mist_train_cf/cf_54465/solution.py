"""
QUESTION:
Write a function called `bubble_sort` that takes a list of integers and a boolean flag `ascending` as input. The function should implement the bubble sort algorithm to sort the input list in either ascending (if `ascending` is True) or descending (if `ascending` is False) order. The function should be able to handle duplicate numbers and should return the sorted list.
"""

def bubble_sort(nums, ascending=True):
    """
    Sorts the input list in either ascending (if `ascending` is True) or descending (if `ascending` is False) order using the bubble sort algorithm.

    Args:
        nums (list): A list of integers to be sorted.
        ascending (bool): A boolean flag indicating the order of sorting. Defaults to True.

    Returns:
        list: The sorted list of integers.
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if (ascending and nums[i] > nums[i + 1]) or (not ascending and nums[i] < nums[i + 1]): 
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return nums