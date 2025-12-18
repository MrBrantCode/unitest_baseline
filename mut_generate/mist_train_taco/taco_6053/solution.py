"""
QUESTION:
Given a N*M matrix of ones and zeros, return how many square submatrices have all ones.
Example 1:
Input:
N = 3
M = 4
matrix [ ][ ] =
                      [ [0, 1, 1, 1],
                        [1, 1, 1, 1], 
                        [0, 1, 1, 1] ]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There are 1 squares of side 3.
Total number of squares = 10 + 4 + 1 =15
 
Example 2:
Input:
N = 3
M = 3
matrix [ ][ ] =
                        [ [1, 0, 1],
                        [1, 1, 0], 
                        [1, 1, 0] ]
Output: 7
Explanation: 
There are 6 squares of side 1.
There are 1 squares of side 2.
Total number of squares = 6  + 1 =7
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countSquares() which takes the interger N, integer M and 2D integer array matrix[ ][ ] as parameters and returns the number of square submatrices have all ones.
Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N,M ≤  3*10^{3}
0 ≤ matrix [ i ][ j ] ≤ 1
"""

def count_squares(N, M, matrix):
    su = 0
    dp = [[0] * M for _ in range(N)]
    
    # Initialize the first column of dp
    for i in range(N):
        dp[i][0] = matrix[i][0]
    
    # Initialize the first row of dp
    for j in range(M):
        dp[0][j] = matrix[0][j]
    
    # Fill the dp array
    for i in range(1, N):
        for j in range(1, M):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = 0
    
    # Sum up all values in dp to get the total number of square submatrices
    for i in range(N):
        su += sum(dp[i])
    
    return su