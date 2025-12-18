"""
QUESTION:
Write a function `bubble_sort_descending` that takes a list of integers as input and returns the list sorted in descending order using the Bubble sort technique.
"""

def bubble_sort_descending(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums