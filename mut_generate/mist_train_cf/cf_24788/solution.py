"""
QUESTION:
Write a function `calculate_paths(matrix)` that calculates the number of possible paths from the top-left corner to the bottom-right corner of an NxN grid, where you can only move down or right at any point. The input matrix is a 2D list of size NxN, and all elements in the matrix are ignored. The function should return an integer representing the total number of possible paths.
"""

def calculate_paths(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
  
    dp = [[0 for _ in range(cols)] for _ in range(rows)] 
  
    dp[0][0] = 1
  
    for i in range(rows):
        for j in range(cols): 
            if i-1 >= 0: 
                dp[i][j] = dp[i][j] + dp[i-1][j]
            if j-1 >= 0:
                dp[i][j] = dp[i][j] + dp [i][j-1]
  
    return dp[rows-1][cols-1]