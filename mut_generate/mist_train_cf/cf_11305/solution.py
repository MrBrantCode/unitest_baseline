"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input, sorts the list in ascending order using the Bubble Sort algorithm with a time complexity of O(n^2), and returns the sorted list. The function should not use any built-in sorting methods.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums