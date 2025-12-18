"""
QUESTION:
Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].
	Matrix [r+1] [c]
	Matrix [r+1] [c-1]
	Matrix [r+1] [c+1]
Starting from any column in row 0 return the largest sum of any of the paths up to row N-1.
NOTE: We can start from any column in zeroth row and can end at any column in (N-1)th row.
Example 1:
Input: N = 2
Matrix = {{348, 391},
          {618, 193}}
Output: 1009
Explaination: The best path is 391 -> 618. 
It gives the sum = 1009.
Example 2:
Input: N = 2
Matrix = {{2, 2},
          {2, 2}}
Output: 4
Explaination: No matter which path is 
chosen, the output is 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function maximumPath() which takes the size N and the Matrix as input parameters and returns the highest maximum path sum.
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N*N)
Constraints:
1 ≤ N ≤ 500
1 ≤ Matrix[i][j] ≤ 1000
"""

def maximum_path_sum(N, Matrix):
    # Helper function to calculate the maximum path sum from a given cell
    def util(a, i, j, n, m):
        nonlocal dp
        if i >= n or i < 0 or j >= m or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = a[i][j] + max(util(a, i + 1, j, n, m), 
                                 util(a, i + 1, j + 1, n, m), 
                                 util(a, i + 1, j - 1, n, m))
        return dp[i][j]
    
    # Initialize the dp array with -1
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    
    # Calculate the maximum path sum starting from each column in the first row
    ans = 0
    for i in range(N):
        ans = max(ans, util(Matrix, 0, i, N, N))
    
    return ans