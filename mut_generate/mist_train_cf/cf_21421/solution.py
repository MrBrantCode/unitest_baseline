"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input and sorts the list in ascending order using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubble_sort(nums):
    """
    Sorts a list of integers in ascending order using the Bubble Sort algorithm.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: A sorted list of integers in ascending order.
    """
    n = len(nums)
    
    for i in range(n):
        swapped = False  # Flag to track if any swaps were made in a pass
        
        for j in range(n - i - 1):
            # Compare adjacent elements and swap if they are in the wrong order
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        
        # If no swaps were made in a pass, the array is already sorted
        if not swapped:
            break
    
    return nums