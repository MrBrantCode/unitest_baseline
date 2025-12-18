"""
QUESTION:
Implement a function called `rotated_binary_search` that takes a rotated sorted array `nums` and a target integer `target` as input. The function should return the index of the target if it exists in the array and -1 if it doesn't exist. The array may contain duplicates. The function should have a time complexity of O(log n) to efficiently handle large inputs.
"""

from typing import List

def rotated_binary_search(nums: List[int], target: int) -> int:
    def findPivot(left, right):
        if nums[left] < nums[right]:
            return 0
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1

    def binarySearch(left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

    n = len(nums)
    if n == 0:
        return -1
    if n == 1:
        return 0 if nums[0] == target else -1
   
    pivot = findPivot(0, n - 1)

    if nums[pivot] == target:
        return pivot
    if pivot == 0:
        return binarySearch(0, n - 1)
    if target < nums[0]:
        return binarySearch(pivot, n - 1)
    return binarySearch(0, pivot)