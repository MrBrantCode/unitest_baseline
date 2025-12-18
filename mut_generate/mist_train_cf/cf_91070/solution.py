"""
QUESTION:
Create a class with a method named `sort_array` that sorts an array of numbers in increasing order. The method should not use built-in sorting functions. The input will be a list of integers and the output should be the sorted list.
"""

def sort_array(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums