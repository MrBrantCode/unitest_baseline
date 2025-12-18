"""
QUESTION:
Write a function `selection_sort` to sort an array of integers in ascending order using the selection sort algorithm, which has a time complexity of O(n^2). The function should take a list of integers as input and return the sorted list.
"""

def selection_sort(nums):
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The sorted list of integers.
    """

    # Traverse through all array elements
    for i in range(len(nums)):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted part
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        
    return nums