"""
QUESTION:
Write a function `binary_search(nums, target)` that finds the index of the first occurrence of the `target` in a sorted array `nums`. If the `target` does not exist in the array, return the index where it should be inserted while maintaining the sorted order. The function should be able to handle edge cases where the array is empty or contains only one element and should be optimized for large arrays.
"""

def binary_search(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target: left = mid + 1
        else: right = mid
    
    if left == len(nums) or nums[left] != target: return left
    else: return left