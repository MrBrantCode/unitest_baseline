"""
QUESTION:
Write a function `kthLargestValue(matrix, k)` that takes a 2D array `matrix` and an integer `k` as input. The function should return the kth largest value among all coordinates of the matrix. The value of a coordinate `(a, b)` is determined by the XOR operation on all `matrix[i][j]` where `0 <= i <= a < m` and `0 <= j <= b < n` (0-indexed). The function should work under the following constraints: `m == matrix.length`, `n == matrix[i].length`, `1 <= m, n <= 1000`, `0 <= matrix[i][j] <= 10^6`, and `1 <= k <= m * n`.
"""

def kthLargestValue(matrix, k):
    m, n = len(matrix), len(matrix[0])
    xor = [[0] * n for _ in range(m)]
    results = []

    for i in range(m):
        for j in range(n):
            xor[i][j] = matrix[i][j]
            if i: xor[i][j] ^= xor[i-1][j]
            if j: xor[i][j] ^= xor[i][j-1]
            if i and j: xor[i][j] ^= xor[i-1][j-1]
            results.append(xor[i][j])
    
    results.sort(reverse=True)
    return results[k-1]