"""
QUESTION:
Implement a function named `insertion_sort` that takes a list of unique integers as input and returns the sorted list in ascending order. The length of the list will be between 1 and 1000, and the function should have a time complexity of O(n^2).
"""

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums