"""
QUESTION:
Implement a `bubble_sort` function that takes a list of integers as input and returns a new list sorted in ascending order using the Bubble Sort algorithm. The input list will not exceed 1000 integers in the range of -1000 to 1000, inclusive. The function should not modify the original list and have a time complexity of O(n^2), where n is the length of the list.
"""

def bubble_sort(nums):
    """
    Sorts a list of integers in ascending order using the Bubble Sort algorithm.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A new list sorted in ascending order.
    """
    # Create a copy of the input list to avoid modifying it
    nums_copy = nums.copy()
    
    # Get the length of the list
    n = len(nums_copy)
    
    # Iterate through the list multiple times
    for i in range(n):
        # Initialize a flag to track if any swaps were made
        swapped = False
        
        # Iterate through the list from the first element to the (n-i-1)th element
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if nums_copy[j] > nums_copy[j + 1]:
                nums_copy[j], nums_copy[j + 1] = nums_copy[j + 1], nums_copy[j]
                swapped = True
        
        # If no swaps were made in the inner loop, the list is already sorted
        if not swapped:
            break
    
    return nums_copy