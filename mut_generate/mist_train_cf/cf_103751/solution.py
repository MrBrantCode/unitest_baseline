"""
QUESTION:
Implement a function `bubble_sort` that sorts a list of integers in ascending order using the bubble sort algorithm. The function should take a list of integers as input and return a new sorted list.
"""

def bubble_sort(nums):
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: A new sorted list of integers.
    """
    nums_copy = nums.copy()
    n = len(nums_copy)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums_copy[j] > nums_copy[j + 1]:
                nums_copy[j], nums_copy[j + 1] = nums_copy[j + 1], nums_copy[j]
                
    return nums_copy