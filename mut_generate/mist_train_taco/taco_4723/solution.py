"""
QUESTION:
Given a binary matrix mat of size n * m, find out the maximum size square sub-matrix with all 1s.
Example 1:
Input: n = 2, m = 2
mat = {{1, 1}, 
       {1, 1}}
Output: 2
Explaination: The maximum size of the square
sub-matrix is 2. The matrix itself is the 
maximum sized sub-matrix in this case.
Example 2:
Input: n = 2, m = 2
mat = {{0, 0}, 
       {0, 0}}
Output: 0
Explaination: There is no 1 in the matrix.
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxSquare() which takes n, m and mat as input parameters and returns the size of the maximum square sub-matrix of given matrix.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
Constraints:
1 ≤ n, m ≤ 50
0 ≤ mat[i][j] ≤ 1
"""

def max_square_submatrix(mat, n, m):
    mx = 0
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            right = dp[i][j + 1]
            diag = dp[i + 1][j + 1]
            down = dp[i + 1][j]
            if mat[i][j] == 1:
                dp[i][j] = 1 + min(right, min(diag, down))
                mx = max(mx, dp[i][j])
            else:
                dp[i][j] = 0
    return mx