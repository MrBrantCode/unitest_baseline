"""
QUESTION:
Implement a function `quicksort(nums)` that takes a list of integers as input and returns the sorted list using the quicksort algorithm. The list can contain duplicate values. The function should be able to handle lists of any length, but it must use the first element as the pivot.
"""

def entance(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        return entance(less) + [pivot] + entance(greater)