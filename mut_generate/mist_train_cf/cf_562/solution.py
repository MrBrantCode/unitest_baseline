"""
QUESTION:
Implement a function called `binary_search` that performs a recursive binary search on a given sorted list of integers to find the index of the target element. The list is sorted in ascending order and may contain duplicate numbers. If the target element is not present in the list, return -1. The time complexity should be O(log n), where n is the number of elements in the list.
"""

def binary_search(nums, target):
    def recursive_binary_search(start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return recursive_binary_search(start, mid - 1)
        else:
            return recursive_binary_search(mid + 1, end)

    return recursive_binary_search(0, len(nums) - 1)