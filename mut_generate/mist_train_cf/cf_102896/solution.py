"""
QUESTION:
Implement a function named `selection_sort` that sorts a list of integers in ascending order using the selection sort algorithm. The function should not use any built-in sorting functions or libraries. It should take a list of integers as input and return the sorted list.
"""

def selection_sort(nums):
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    for i in range(len(nums)):
        # Assume the first element is the minimum
        min_index = i
        
        # Find the minimum element in the unsorted part of the list
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element
        nums[i], nums[min_index] = nums[min_index], nums[i]
    
    return nums