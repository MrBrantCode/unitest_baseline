"""
QUESTION:
You are given an `m x n` matrix, initially filled with `0`'s. A 2D array `indices` is provided, where each `indices[i] = [ri, ci]` signifies a 0-indexed location in the matrix where increment operations are to be performed.

For each location `indices[i]`, increment all the cells in row `ri` and all the cells in column `ci`. Return the count of odd-valued cells in the matrix after performing the increment operations at all locations specified in `indices` and the final state of the matrix.

Constraints are as follows:
`1 &lt;= m, n &lt;= 50`
`1 &lt;= indices.length &lt;= 100`
`0 &lt;= ri &lt; m`
`0 &lt;= ci &lt; n`
"""

def oddCells(m, n, indices):
    matrix = [[0]*n for _ in range(m)]
    odd_count = 0
    rows = [0] * m
    cols = [0] * n
    
    for r, c in indices:
        rows[r] += 1
        cols[c] += 1
        
    for i in range(m):
        for j in range(n):
            matrix[i][j] = rows[i] + cols[j]
            if matrix[i][j] % 2 == 1:
                odd_count += 1
                
    return odd_count