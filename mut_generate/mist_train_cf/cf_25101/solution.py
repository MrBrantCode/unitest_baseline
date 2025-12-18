"""
QUESTION:
Write a function `maximum_square_submatrix(matrix, n)` that takes a 2D array `matrix` of size `n x n` containing only 0s and 1s, and returns the area of the largest square sub-matrix composed entirely of 1s. The function should use dynamic programming to achieve this.
"""

def maximum_square_submatrix(matrix, n):
    # answer stores the maximum size of the square
    ans = 0

    # dp array of size n+1 x n+1
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            # if the element is 1
            if matrix[i-1][j-1] == 1:
                # find the minimum of the elements on its left, top and diagonal
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                # update the answer
                ans = max(ans, dp[i][j])

    # return the answer
    return ans * ans