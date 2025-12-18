"""
QUESTION:
Implement a function called `insertion_sort` that takes a list of integers as input and returns the sorted list in ascending order using the insertion sort algorithm. The function should sort the list in-place.
"""

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i -1
        while j >=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums