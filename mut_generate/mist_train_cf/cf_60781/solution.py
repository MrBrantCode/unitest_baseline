"""
QUESTION:
You are given an array of integers `arr` with a length between 2 and 10000, containing integers within the range of -10000 to 10000. Write a function `partition(arr)` that partitions the array into two such that the sum of elements in both partitions is equal. If such a partition is not possible, return an empty array.
"""

def partition(arr):
    totalSum = sum(arr)
    # If total sum is not evenly divisible by 2, no partition is possible
    if totalSum % 2 != 0:
        return []

    n = len(arr)
    # The sum each partition should ideally have
    half = totalSum // 2

    dp = [0] * (half + 1)
    dp[0] = 1
    sums = {0}

    for num in arr:
        sums |= {v + num for v in sums}
        if half in sums:
            return [num]
    return []