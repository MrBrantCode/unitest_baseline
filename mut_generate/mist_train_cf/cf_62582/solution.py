"""
QUESTION:
Implement a function `get_positive_and_sort` that takes a list of integers as input, filters out the negative numbers, and returns the positive ones in a new list sorted in increasing order. Additionally, create a function `bubble_sort` to facilitate a customized sorting mechanism. The solution should not use Python's built-in `sort()` and `sorted()` functions.
"""

def get_positive_and_sort(lst):
    positives = []
    for num in lst:
        if num > 0:
            positives.append(num)

    return bubble_sort(positives)

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums