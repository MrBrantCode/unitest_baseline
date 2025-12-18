"""
QUESTION:
Implement a `CustomSorter` class that inherits from an abstract parent class and implements a `sort` method with a time complexity of O(n^2), where n is the length of the input list. The implementation should use only constant extra space, and not use any built-in sorting functions or external libraries. The `sort` method should take a list of unique positive integers as input and return the sorted list in descending order.
"""

def custom_sorter(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums