"""
QUESTION:
Create a class with a method `sort_array` that sorts an array of numbers in increasing order without using the built-in sorting functions (e.g., `sorted()` or `.sort()`). The method should take an array of numbers as input and return the sorted array.
"""

def sort_array(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums