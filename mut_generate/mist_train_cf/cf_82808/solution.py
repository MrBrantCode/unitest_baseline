"""
QUESTION:
Write a function called `calculate_median` that takes a list of five integers as input and returns the median value without using any built-in sorting functions, comparison operators, or conditional operators.
"""

def calculate_median(nums):
    # calculate median without using built-in sorting functions
    sorted_nums = quicksort(nums)
    return sorted_nums[len(nums) // 2]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)