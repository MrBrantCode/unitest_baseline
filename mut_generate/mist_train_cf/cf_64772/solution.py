"""
QUESTION:
Write a function `search_last(nums, target)` that finds the last position of the `target` element in a sorted array `nums` that may contain duplicate elements, negative numbers, and may be rotated at an unknown pivot. The function should achieve a time complexity of O(log n) and handle large arrays efficiently without using built-in methods. If the `target` is not found in the array, return -1.
"""

def search_last(nums, target):
    if len(nums) == 0:
        return -1

    low = 0
    high = len(nums) - 1

    def binary_search(low, high):
        if low > high:
            return -1
        
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            else:
                return binary_search(mid + 1, high)

        if nums[mid] > target or nums[mid] < nums[low]:
            return binary_search(low, mid - 1)
            
        elif nums[mid] < target or nums[mid] > nums[high]:
            return binary_search(mid + 1, high)
            
        else:
            return binary_search(mid + 1, high)
            
    return binary_search(low, high)