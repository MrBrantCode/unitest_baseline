"""
QUESTION:
Given a matrix `mat` of size `m x n` where `m == mat.length` and `n == mat.length[i]`, and `k`, return the `k`th smallest sum of an array formed by choosing one element from each row and column of the matrix. The rows and columns of the matrix are sorted in non-decreasing order. The constraints are `1 <= m, n <= 40`, `1 <= k <= min(200, n ^ m)`, and `1 <= mat[i][j] <= 5000`. Write a function `kthSmallest(mat, k)` that satisfies these conditions.
"""

import heapq

def kthSmallest(mat, k):
    m, n = len(mat), len(mat[0])
    heap = [(sum(row[0] for row in mat), [0]*m)]
    visited = set()

    for _ in range(k):
        curr_sum, indices = heapq.heappop(heap)
        if _ == k - 1:
            return curr_sum
        for i in range(m):
            if indices[i] + 1 < n:
                new_indices = list(indices)
                new_indices[i] += 1
                new_tuple = (curr_sum - mat[i][indices[i]] + mat[i][new_indices[i]], new_indices)
                if tuple(new_indices) not in visited:
                    visited.add(tuple(new_indices))
                    heapq.heappush(heap, new_tuple)