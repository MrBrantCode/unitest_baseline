"""
QUESTION:
Create a class with a method `bubble_sort` that takes a list of numbers as input and returns the sorted list in increasing order. The method should implement a sorting algorithm with a time complexity of O(n^2) and cannot use the built-in sorting functions `sorted()` or `sort()`.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums