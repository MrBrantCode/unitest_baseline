"""
QUESTION:
Write a function `containsDuplicate(nums, k)` that takes an array of integers `nums` and an integer `k` as input, and returns `True` if there are two distinct indices `i` and `j` in the array such that `nums[i] = nums[j]` and the absolute difference between `i` and `j` is at most `k`, and `False` otherwise. The function should have a time complexity of O(n log n) and should not use any additional data structures or modify the input array.
"""

def containsNearbyDuplicate(nums, k):
    sorted_nums = sorted(nums) 

    for i in range(len(nums)):
        if binary_search(sorted_nums, sorted_nums[i], i + 1, min(i + k, len(nums) - 1)):
            return True
    
    return False

def binary_search(nums, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False