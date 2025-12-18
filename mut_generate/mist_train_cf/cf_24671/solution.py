"""
QUESTION:
Write a function `bubble_sort(nums)` that takes a list of integers as input and returns the sorted list using the bubble sort algorithm. The function should sort the list in ascending order.
"""

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums