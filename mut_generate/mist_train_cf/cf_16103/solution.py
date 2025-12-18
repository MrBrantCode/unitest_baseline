"""
QUESTION:
Implement a function named `insertion_sort` that takes a list of unique integers `nums` as input, where the length of `nums` is between 1 and 1000. The function should sort the list in ascending order using the insertion sort algorithm and return the sorted list.
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