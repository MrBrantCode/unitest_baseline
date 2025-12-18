"""
QUESTION:
Implement functions for Insertion Sort and Bubble Sort algorithms, and compare their time complexity, space complexity, and stability. The functions should take a list of integers as input and return the sorted list.
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
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

def bubble_sort(nums):
    """
    Sorts a list of integers using the Bubble Sort algorithm.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: The sorted list of integers.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums