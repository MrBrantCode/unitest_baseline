"""
QUESTION:
Create a function named `find_unique_sums` that takes a list of integers as input and returns all unique sums of two numbers in the list, in ascending order. The function should handle both positive and negative numbers, and exclude duplicates.
"""

def find_unique_sums(nums):
    nums.sort()
    sums = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sums.add(nums[i] + nums[j])
    return sorted(list(sums))