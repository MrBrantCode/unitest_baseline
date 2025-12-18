"""
QUESTION:
Write a function `maxSumPath(grid, k)` that finds the maximum sum of numbers taken from a 2D grid of integers, such that the chosen numbers lie on a path and are at most 'k' steps away from the previous chosen number. Each step in the path can be either a 'Right' move, a 'Down' move, a 'Left' move or an 'Up' move. 

Restrictions: 
1. It's not allowed to visit any cell more than once.
2. It's not allowed to end at any cell except for grid[0][0] when all k steps are done.

The function should return the digits that were chosen to form the maximum sum, in the order they were chosen.
"""

def maxSumPath(grid, k):
    N = len(grid)
    if  N == 0:
        return []

    # Initialize dp array
    dp = [[[-1 for _ in range(k+1)] for _ in range(N)] for _ in range(N)]

    # Initialize offsets array for possible steps 
    offsets = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    # Recursively get max sum from all possible steps
    def getMaxSum(r, c, k):
        if r < 0 or c < 0 or r >= N or c >= N or k <= 0:
            return 0

        if dp[r][c][k] != -1:
            return dp[r][c][k]

        res = 0
        for offset in offsets:
            rr, cc = r + offset[0], c + offset[1]
            res = max(res, grid[r][c] + getMaxSum(rr, cc, k-1))

        dp[r][c][k] = res
        return res

    # Traverse and get max sum of k values, and trace back steps
    max_sum, max_steps = 0, []
    for r in range(N):
        for c in range(N):
            temp_sum = getMaxSum(r, c, k)
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_steps = [grid[r][c]]
                temp_k = k
                while temp_k > 1:
                    for offset in offsets:
                        rr, cc = r + offset[0], c + offset[1]
                        if rr >= 0 and cc >= 0 and rr < N and cc < N and dp[rr][cc][temp_k-1] + grid[r][c] == dp[r][c][temp_k]:
                            max_steps.append(grid[rr][cc])
                            r, c, temp_k = rr, cc, temp_k - 1
                            break
    return max_steps[::-1]