"""
QUESTION:
Write a function named `sort_descending` that takes a list of numbers as input, sorts the list in descending order without using any built-in sort function, and returns the sorted list. The list may contain duplicate values and is not guaranteed to be sorted initially.
"""

def sort_descending(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums