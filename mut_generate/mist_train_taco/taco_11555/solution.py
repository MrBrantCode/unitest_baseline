"""
QUESTION:
Given a matrix with n rows and m columns. Your task is to find the length of the longest increasing path in matrix, here increasing path means that the value in the specified path increases. For example if a path of length k has values a_{1}, a_{2}, a_{3}, .... a_{k } , then for every i from [2,k] this condition must hold a_{i }> a_{i-1}.  No cell should be revisited in the path.
From each cell, you can either move in four directions: left, right, up, or down. You are not allowed to move diagonally or move outside the boundary.
Example 1:
Input:
n = 3, m = 3
matrix[][] = {{1 2 3},
              {4 5 6},
              {7 8 9}}
Output: 
5
Explanation: 
The longest increasing path is 
{1, 2, 3, 6, 9}. 
Example 2:
Input:
n = 3, m = 3
matrix[][] = {{3 4 5},
              {6 2 6},
              {2 2 1}}
Output: 
4
Explanation:
The longest increasing path is
{3, 4, 5, 6}.
Your Task:
You only need to implement the given function longestIncreasingPath() which takes the two integers n and m and the matrix matrix as input parameters, and returns the length of the longest increasing path in matrix.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
Constraints:
1 ≤ n,m ≤ 1000
0 ≤ matrix[i] ≤ 2^{30}
"""

def longest_increasing_path(matrix, n, m):
    def dfs(matrix, dummy, i, j, n, m):
        if dummy[i][j] != 0:
            return dummy[i][j]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        res = 1
        for k in range(4):
            p = i + dx[k]
            q = j + dy[k]
            if 0 <= p < n and 0 <= q < m and matrix[i][j] < matrix[p][q]:
                res = max(res, 1 + dfs(matrix, dummy, p, q, n, m))
        dummy[i][j] = res
        return res
    
    dummy = [[0] * m for _ in range(n)]
    maxi = 0
    for i in range(n):
        for j in range(m):
            maxi = max(maxi, dfs(matrix, dummy, i, j, n, m))
    return maxi