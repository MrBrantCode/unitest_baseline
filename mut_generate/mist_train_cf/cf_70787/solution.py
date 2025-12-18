"""
QUESTION:
Write a function `find_last_position` that takes a sorted array `nums` and a target number `target` as input, and returns the last index of the target number in the array. The array may contain duplicate elements and negative numbers, and the function should have a time complexity better than O(n). Implement this function without using built-in methods.
"""

def find_last_position(nums, target):
    start, end = 0, len(nums) - 1
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            ans = mid
            start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return ans