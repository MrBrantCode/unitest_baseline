"""
QUESTION:
Write a function `kWeakestRows` that takes a binary matrix `mat` and an integer `k` as input, and returns a tuple containing the indices of the `k` weakest rows in the matrix ordered from weakest to strongest, and the total number of civilians in the `k` weakest rows.

The matrix `mat` has the following properties:
- `m == mat.length`
- `n == mat[i].length`
- `2 <= n, m <= 100`
- `1 <= k <= m`
- `matrix[i][j]` is either 0 or 1
- The soldiers are positioned in front of the civilians, i.e., all the 1's will appear to the left of all the 0's in each row.

A row `i` is weaker than a row `j` if one of the following is true:
- The number of soldiers in row `i` is less than the number of soldiers in row `j`.
- Both rows have the same number of soldiers and `i < j`.
"""

import heapq

def kWeakestRows(mat, k):
    pq = []
    
    for idx, row in enumerate(mat):
        strength = sum(row)
        heapq.heappush(pq, (strength, idx))
    
    res = []
    total_civilians = 0
    
    for _ in range(k):
        strength, idx = heapq.heappop(pq)
        res.append(idx)
        total_civilians += len(mat[idx]) - strength
    
    return (res, total_civilians)