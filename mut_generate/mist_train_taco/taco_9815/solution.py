"""
QUESTION:
Given a matrix containing lower alphabetical characters only of size n*m. We need to count the number of palindromic paths in the given matrix.
A path is defined as a sequence of cells starting from top-left cell and ending at bottom-right cell. We are allowed to move to right and down only from current cell.
 
Example 1:
Input: matrix = {{a,a,a,b},{b,a,a,a},{a,b,b,a}}
Output: 3
Explanation: Number of palindromic paths are 3 
from top-left to bottom-right.
aaaaaa (0, 0) -> (0, 1) -> (1, 1) -> (1, 2) -> 
(1, 3) -> (2, 3)    
aaaaaa (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> 
(1, 3) -> (2, 3)    
abaaba (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
(2, 2) -> (2, 3)
Example 2:
Input: matrix = {{a,b},{c,d}}
Output: 0
Explanation: There is no palindromic paths.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function countPalindromicPaths() which takes the matrix as input parameter and returns the total nuumber of palindromic paths modulo 10^{9} + 7.
 
Expected Time Complexity: O(n^{2}*m^{2})
Space Complexity: O(n*m)
 
Constraints:
1 ≤ n, m ≤ 100
"""

def count_palindromic_paths(matrix):
    def solve(ma, i1, j1, i2, j2, dp):
        n = len(ma)
        m = len(ma[0])
        if i1 >= n or j1 >= m or i2 < 0 or j2 < 0 or i1 > i2 or j1 > j2 or ma[i1][j1] != ma[i2][j2]:
            return 0
        if i1 == i2 and j1 == j2 or (i1 == i2 and j1 + 1 == j2) or (j1 == j2 and i1 + 1 == i2):
            return 1
        x = i1 * n + j1
        y = i2 * n + j2
        if x in dp and y in dp[x]:
            return dp[x][y]
        ans = 0
        ans = (ans + solve(ma, i1 + 1, j1, i2 - 1, j2, dp)) % M
        ans = (ans + solve(ma, i1 + 1, j1, i2, j2 - 1, dp)) % M
        ans = (ans + solve(ma, i1, j1 + 1, i2 - 1, j2, dp)) % M
        ans = (ans + solve(ma, i1, j1 + 1, i2, j2 - 1, dp)) % M
        if x not in dp:
            dp[x] = {}
        dp[x][y] = ans
        return ans

    dp = {}
    n = len(matrix)
    for i in range(n):
        if matrix[i][-1] == ' ':
            matrix[i].pop()
    m = len(matrix[0])
    M = int(1000000000.0 + 7)
    return solve(matrix, 0, 0, n - 1, m - 1, dp)