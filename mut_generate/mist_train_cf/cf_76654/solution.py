"""
QUESTION:
Create a function called `bubbleSort` that sorts a given list of integers in ascending order using the Bubble Sort algorithm. The function should not use any built-in sorting functions and should be able to handle lists of varying lengths.
"""

def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums