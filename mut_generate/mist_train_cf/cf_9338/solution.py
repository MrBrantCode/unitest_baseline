"""
QUESTION:
Write a function `selection_sort_unique` that sorts a list of integers in ascending order using the selection sort algorithm and removes any duplicate values from the list. The function should return the sorted list of unique integers.
"""

def selection_sort_unique(nums):
    nums = list(set(nums))  # Remove duplicates by converting to set and back to list
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums