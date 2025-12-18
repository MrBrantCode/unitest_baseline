"""
QUESTION:
Implement a function `bubble_sort` that sorts a list of numbers in non-decreasing order using the bubble sort algorithm, which repeatedly swaps adjacent elements if they are in the wrong order until the entire list is sorted. The function should take a list of integers as input and return the sorted list. The list may contain duplicate elements.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums