"""
QUESTION:
Write a function `minSubMatrixSum` that takes a 2D list of integers `nums` as input and returns the minimum sum of any non-empty sub-matrix of `nums`. The input matrix `nums` has at least one row and one column.
"""

def minSubMatrixSum(nums):
    H, W = len(nums), len(nums[0])
    
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    ans = float('inf')
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            # Calculating prefix sum
            dp[i][j] = nums[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            # Now for each (i,j) we find the minimum submatrix sum.
            for h in range(i):
                for w in range(j):
                    ans = min(ans, dp[i][j] - dp[h][j] - dp[i][w] + dp[h][w])
    
    # Returning the minimum sum of sub-matrix
    return ans