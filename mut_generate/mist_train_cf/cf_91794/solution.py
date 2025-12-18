"""
QUESTION:
Create a function `find_unique_sums(nums)` that takes an array of integers as input and returns all unique possible sums of two numbers in the array, in ascending order. The function should be able to handle arrays containing negative numbers and should not include any duplicate sums in its output.
"""

def find_unique_sums(nums):
    nums.sort()
    sums = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sums.add(nums[i] + nums[j])
    return sorted(list(sums))