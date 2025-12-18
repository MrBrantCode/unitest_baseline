"""
QUESTION:
Write a function called `binary_search_closest` that takes a sorted array of integers and a target integer as input, and returns the element in the array that is closest to the target value. The function should use binary search to achieve a time complexity of O(log n).
"""

def binary_search_closest(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if right < 0:
        return nums[0]
    elif left >= len(nums):
        return nums[-1]
    else:
        if abs(nums[left] - target) <= abs(nums[right] - target):
            return nums[left]
        else:
            return nums[right]