"""
QUESTION:
Given a n*m matrix, find the maximum length path (starting from any cell) such that all cells along the path are in strictly increasing order.
We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1).
 
Example 1:
Input: matrix = {{1,2,9},{5,3,8},{4,6,7}}
Output: 7
Explanation: The longest increasing path is
{1,2,3,6,7,8,9}.
Example 2:
Input: matrix = {{3,4,5},{3,2,6},{2,2,1}}
Output: 4
Explanation: The longest increasing path is
{3,4,5,6}.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function longestIncreasingPath() which takes matrix as input parameter and returns the length of the lonest increasing path.
Expected Time Complexity: O(n*m)
Expected Space Comeplxity: O(n*m)
 
Constraints:
1 <= n, m <= 100
1 <= matrix[i][j] <= 10^{4}
"""

def longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    n, m = len(matrix), len(matrix[0])
    dp = [[-1] * m for _ in range(n)]
    
    def dfs(i, j, prev):
        if i < 0 or j < 0 or i >= n or j >= m or matrix[i][j] <= prev:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        count = 1
        count += max(dfs(i + 1, j, matrix[i][j]), 
                     dfs(i - 1, j, matrix[i][j]), 
                     dfs(i, j + 1, matrix[i][j]), 
                     dfs(i, j - 1, matrix[i][j]))
        
        dp[i][j] = count
        return dp[i][j]
    
    max_path_length = 0
    for i in range(n):
        for j in range(m):
            max_path_length = max(max_path_length, dfs(i, j, -1))
    
    return max_path_length