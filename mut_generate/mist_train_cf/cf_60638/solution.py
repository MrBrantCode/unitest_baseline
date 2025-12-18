"""
QUESTION:
Write a function named `countNumbers` that takes a list of integers `nums` as input, where `1 <= len(nums) <= 105` and `-104 <= nums[i] <= 104`. The function should return two lists, `counts` and `countsNeg`, of the same length as `nums`. The value at index `i` in `counts` should be the number of elements in `nums` to the right of index `i` that are smaller than `nums[i]`, and the value at index `i` in `countsNeg` should be the number of negative numbers in `nums` to the right of index `i`.
"""

def countNumbers(nums):
    counts = [0] * len(nums)
    countsNeg = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                counts[i] += 1
            if nums[j] < 0:
                countsNeg[i] += 1
    return counts, countsNeg