"""
QUESTION:
Write a function named `search_insert` that takes two parameters: `nums` (a sorted array of integers) and `target` (the number to be searched). Return the index of the first occurrence of the target in the array if it exists; otherwise, return the index where the target should be inserted to maintain the sorted order. The function should be able to handle edge cases, including empty or single-element arrays, and should be optimized for large arrays with up to 10^6 elements. The function should also handle negative integers and zero.
"""

def search_insert(nums, target):
    if not nums or nums[0] > target:
        return 0
    if nums[-1] < target:
        return len(nums)
    
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left