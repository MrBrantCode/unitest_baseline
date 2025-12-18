"""
QUESTION:
Implement a function called `insertion_sort` that sorts an array of integers in ascending order using the insertion sort algorithm. The function should take a list of integers as input and return the sorted list.
"""

def insertion_sort(nums):
    for i in range(1,len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = item_to_insert

    return nums