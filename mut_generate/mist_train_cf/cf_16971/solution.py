"""
QUESTION:
Implement a function called `selection_sort` that takes a list of integers as input and sorts the list in ascending order using the selection sort algorithm. The function should have a time complexity of O(n^2) and must not use any built-in sorting functions, libraries, or additional data structures. The sorting should be performed in-place, without recursion, and without using mathematical operations or bit manipulation tricks to optimize the algorithm.
"""

def selection_sort(nums):
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """

    # Iterate over the list
    for i in range(len(nums)):
        # Initialize the index of the smallest element found so far to the current index
        smallest_idx = i
        
        # Iterate through the remaining elements in the list
        for j in range(i + 1, len(nums)):
            # If the current element is smaller, update the index of the smallest element found so far
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        
        # Swap the smallest element found with the current element
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    
    return nums