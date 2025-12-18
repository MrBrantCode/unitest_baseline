"""
QUESTION:
Implement a function named `bubble_sort` that sorts a list of numbers in ascending order using the Bubble Sort algorithm. The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums