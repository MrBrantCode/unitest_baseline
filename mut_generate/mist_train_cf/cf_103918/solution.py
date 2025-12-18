"""
QUESTION:
Write a function `binary_search` that takes a sorted list of numbers and a target number as input, and returns `True` if the target number is present in the list and `False` otherwise. The function should use binary search algorithm to achieve this. The input list is guaranteed to be sorted in ascending order.
"""

def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return True
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    
    return False