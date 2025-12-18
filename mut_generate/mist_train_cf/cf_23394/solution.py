"""
QUESTION:
Implement a function called `bubble_sort` that sorts an array of integers in ascending order using the bubble sort algorithm. The function should take one argument, a list of integers, and return the sorted list. The function should modify the input list by swapping adjacent elements if they are in the wrong order.
"""

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums