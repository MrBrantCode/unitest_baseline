"""
QUESTION:
Create a function named bubble_sort that takes a list of numbers as input and returns the sorted list in ascending order. The function should implement the bubble sort algorithm, which repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The function should only use nested loops to achieve this and should not use any built-in sorting functions. The input list is not guaranteed to be sorted and may contain duplicate elements.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:  
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums