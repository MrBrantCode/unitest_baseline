"""
QUESTION:
Write a function `min_sub_matrix(matrix, target)` that finds the smallest submatrix in a given 2D numerical matrix with a sum of elements equal to a target value. The function should return the coordinates of the upper left and lower right corners of the smallest submatrix as a tuple (x1, y1, x2, y2). The function should handle cases where the matrix is empty.
"""

def min_sub_matrix(matrix, target):
    N = len(matrix) 
    if N == 0:
        return (0, 0, 0, 0)
    M = len(matrix[0]) 

    # Precompute prefix sums
    ps = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            ps[i][j] = matrix[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

    ans = None
    for i1 in range(1, N+1):
        for j1 in range(1, M+1):
            for i2 in range(i1, N+1):
                for j2 in range(j1, M+1):
                    total = ps[i2][j2] - ps[i2][j1-1] - ps[i1-1][j2] + ps[i1-1][j1-1]
                    if total == target:
                        if not ans or (i2-i1+1)*(j2-j1+1) < (ans[2]-ans[0]+1)*(ans[3]-ans[1]+1):
                            ans = (i1-1, j1-1, i2-1, j2-1)
    return ans