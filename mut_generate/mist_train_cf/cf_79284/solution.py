"""
QUESTION:
Write a function `findKthNumber(m, n, k)` that finds the `k-th` smallest number in a multiplication table of size `m x n`. The function should take three parameters: the height `m` of the table, the length `n` of the table, and the position `k` of the number to find. The function should return the `k-th` smallest number in the table. The inputs `m` and `n` will be in the range [1, 30000] and `k` will be in the range [1, m * n].
"""

def findKthNumber(m, n, k):
    low, high = 1, m * n
    while low < high:
        mid = (low + high) // 2
        # if the count is less than k, that means we need to increase the range
        if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
            low = mid + 1
        # else we decrease the range
        else:
            high = mid
    return low