"""
QUESTION:
Implement a function named `insertion_sort` that takes a list of unique integers as input, sorts the list in ascending order using the insertion sort algorithm, and returns the sorted list. The length of the input list will be between 1 and 1000, and the time complexity of the algorithm should be O(n^2).
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