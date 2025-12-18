"""
QUESTION:
Write a function named `solve` that takes an array of integers `nums` as input and returns an array where each element at index `i` represents the count of numbers in `nums` that are less than `nums[i]`. The array `nums` contains between 2 and 500 elements, and each element in `nums` is between 0 and 100.
"""

def solve(nums):
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if j != i and nums[j] < nums[i]:
                count += 1
        res.append(count)
    return res