"""
QUESTION:
Write a function `maxSize(matrix, constraint)` that takes a binary matrix `matrix` and a constraint matrix `constraint` as input and returns the area of the largest submatrix within `matrix` where every element of the submatrix is `1` after reordering the columns optimally and performing the operation optimally under the given constraints.

The function should be able to handle binary matrices of size `m x n` where `1 <= m * n <= 10^5`, `matrix[i][j]` is `0` or `1`, and `constraint[i][j]` is `0` or `1`. The constraint matrix indicates which columns cannot be moved.
"""

def maxSize(matrix, constraint):
    n, m = len(matrix), len(matrix[0])
    result = 0
    for i in range(n):
        cnt = [0]*m
        for j in range(i, n):
            for k in range(m-1, -1, -1):
                if matrix[j][k]:
                    cnt[k] += 1
                else:
                    cnt[k] = 0
            arr = sorted([(not constraint[i][l], cnt[l]) for l in range(m)], reverse=True)
            total = arr[0][1]
            for p in range(1, m):
                total = min(total, arr[p][1])
                if total == 0:
                    break
                result = max(result, total*(p+1))
    return result