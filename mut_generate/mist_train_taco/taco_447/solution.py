"""
QUESTION:
Given a N x N matrix such that each of its cells contains some coins. Count the number of ways to collect exactly K coins while moving from top left corner of the matrix to the bottom right. From a cell (i, j), you can only move to (i+1, j) or (i, j+1).
Example 1:
Input:
K = 12, N = 3
arr[] = [[1, 2, 3], 
         [4, 6, 5], 
         [3, 2, 1]]
Output: 2
Explanation: 
There are 2 possible paths 
with exactly K coins, (1 + 2 + 
6 + 2 + 1) and (1 + 2 + 3 + 5 + 1).
Example 2:
Input:
K = 16, N = 3
arr[] = [[1, 2, 3], 
         [4, 6, 5], 
         [9, 8, 7]]
Output: 0 
Explanation: 
There are no possible paths that lead 
to sum=16
Your Task:  
You don't need to read input or print anything. Your task is to complete the function numberOfPath() which takes N, K and 2D matrix arr[][] as input parameters and returns the number of possible paths.
Expected Time Complexity: O(n*n*k)
Expected Auxiliary Space: O(n*n*k)
Constraints:
1 <= K < 100
1 <= N < 100
1 <= arr_{ij} <= 200
"""

def count_paths_with_coins(N, K, arr):
    # Helper function to perform the recursive path counting with memoization
    def util(i, j, k):
        nonlocal dp
        # Base cases
        if i >= N or j >= N or k < 0:
            return 0
        if i == N - 1 and j == N - 1:
            if k - arr[i][j] == 0:
                return 1
            return 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        
        # Recursive calls
        dp[i][j][k] = util(i + 1, j, k - arr[i][j]) + util(i, j + 1, k - arr[i][j])
        return dp[i][j][k]
    
    # Initialize the memoization table
    dp = [[[-1 for _ in range(K + 1)] for _ in range(N)] for _ in range(N)]
    
    # Start the recursive counting from the top-left corner
    return util(0, 0, K)