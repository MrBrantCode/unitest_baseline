"""
QUESTION:
Given an N x N matrix, mat[N][N] of integers. The task is to find the maximum value of mat(c, d) mat(a, b) over all choices of indexes such that both c > a and d > b.
Example 1:
Input:
mat[N][N] = {{ 1, 2, -1, -4, -20 },
             { -8, -3, 4, 2, 1 }, 
             { 3, 8, 6, 1, 3 },
             { -4, -1, 1, 7, -6 },
             { 0, -4, 10, -5, 1 }};
Output: 18
Explanation: The maximum value is 18 as mat[4][2] 
- mat[1][0] = 18 has maximum difference.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findMaxValue() which takes a matrix mat and returns an integer as output.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
1 <= N <= 10^{3}
-10^{3}<= mat[i][j] <=10^{3}
"""

from typing import List

def find_max_value(mat: List[List[int]], n: int) -> int:
    if n == 1:
        return 0
    
    ans = -10 ** 10
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    dp[0][0] = mat[0][0]
    
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], mat[i][0])
        dp[0][i] = min(dp[0][i - 1], mat[0][i])
    
    for i in range(1, n):
        for j in range(1, n):
            temp = mat[i][j]
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], mat[i][j])
            ans = max(ans, temp - dp[i - 1][j - 1])
    
    return ans