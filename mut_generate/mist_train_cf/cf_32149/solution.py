"""
QUESTION:
Write a function `maxPathSum` that takes two 2D arrays `down` and `right` of size `n x m` and `n x m+1` respectively, where `n` is the number of rows and `m` is the number of columns. The function should return the maximum sum of values that can be obtained by choosing the optimal path from the top-left cell to the bottom-right cell, where the path can only move right or down. The values for moving down and right are given in the `down` and `right` arrays respectively.
"""

def maxPathSum(down, right):
    """
    This function calculates the maximum sum of values that can be obtained by choosing 
    the optimal path from the top-left cell to the bottom-right cell, where the path 
    can only move right or down.

    Parameters:
    down (list): A 2D array of size n x m, where n is the number of rows and m is the 
                 number of columns, representing the values for moving down.
    right (list): A 2D array of size n x m+1, representing the values for moving right.

    Returns:
    int: The maximum sum of values that can be obtained by choosing the optimal path.
    """

    n = len(down)
    m = len(down[0])

    M = [[0] * m for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            if r == 0 and c == 0:
                M[r][c] = 0
            elif r == 0:
                M[r][c] = M[r][c - 1] + right[r][c - 1]
            elif c == 0:
                M[r][c] = M[r - 1][c] + down[r - 1][c]
            else:
                candidate_predecesor_top = M[r - 1][c] + down[r - 1][c]
                candidate_predecesor_left = M[r][c - 1] + right[r][c - 1]
                M[r][c] = max(candidate_predecesor_top, candidate_predecesor_left)

    return M[n - 1][m - 1]