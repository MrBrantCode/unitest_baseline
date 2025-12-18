"""
QUESTION:
Given an integer array `nums` with a length between 3 and 1000 (inclusive) and elements between 1 and 10^9 (inclusive), where it is guaranteed that a mountain array can be formed from `nums`, write a function `min_removals(nums)` that determines the smallest number of elements that need to be removed to transform `nums` into a mountain array. A mountain array has a length of at least 3 and there exists an index `i` (0-indexed) where `0 < i < arr.length - 1` such that the elements of the array increase up to `i` and then decrease.
"""

def min_removals(nums):
    n = len(nums)
    lis = [1] * n
    lds = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i]>nums[j]:
                lis[i] = max(lis[i], lis[j]+1)

    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if nums[i]>nums[j]:
                lds[i] = max(lds[i], lds[j]+1)

    max_mountain = 0
    for i in range(1, n-1):
        if lis[i]>1 and lds[i]>1:
            max_mountain = max(max_mountain, min(lis[i], lds[i]))

    return n - (max_mountain*2 - 1)