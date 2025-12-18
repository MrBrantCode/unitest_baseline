"""
QUESTION:
Given the dimensions of a Multiplication Matrix (m x n), find the k-th least number in the matrix. The function should be named `findKthNumber` and take three parameters: `m`, `n`, and `k`, where `1 <= m, n <= 30000` and `1 <= k <= m * n`.
"""

def findKthNumber(m, n, k):
    low, high = 1, m * n
    while low < high:
        mid = low + (high - low) // 2
        if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
            low = mid + 1
        else:
            high = mid
    return low