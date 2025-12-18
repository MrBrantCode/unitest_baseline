"""
QUESTION:
Given a matrix mat of size N x M where every element is either O or X.
Replace all O with X that are surrounded by X.
A O (or a set of O) is considered to be surrounded by X if there are X at locations just below, just above, just left and just right of it.
Example 1:
Input: n = 5, m = 4
mat = {{'X', 'X', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Output: ans = {{'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'O', 'O'}}
Explanation: Following the rule the above 
matrix is the resultant matrix. 
Your Task:
You do not need to read input or print anything. Your task is to complete the function fill() which takes n, m and mat as input parameters ad returns a 2D array representing the resultant matrix.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
Constraints:
1 ≤ n, m ≤ 500
"""

def replace_surrounded_O_with_X(n, m, mat):
    def dfs(row, col, visited, mat, r, c):
        visited[row][col] = 1
        for i in range(4):
            nrow = row + r[i]
            ncol = col + c[i]
            if 0 <= nrow < n and 0 <= ncol < m and visited[nrow][ncol] != 1 and mat[nrow][ncol] == 'O':
                dfs(nrow, ncol, visited, mat, r, c)
    
    r = [-1, 0, 1, 0]
    c = [0, 1, 0, -1]
    visited = [[0] * m for _ in range(n)]
    
    # DFS from the boundary 'O's
    for i in range(m):
        if visited[0][i] != 1 and mat[0][i] == 'O':
            dfs(0, i, visited, mat, r, c)
        if visited[n - 1][i] != 1 and mat[n - 1][i] == 'O':
            dfs(n - 1, i, visited, mat, r, c)
    for i in range(n):
        if visited[i][0] != 1 and mat[i][0] == 'O':
            dfs(i, 0, visited, mat, r, c)
        if visited[i][m - 1] != 1 and mat[i][m - 1] == 'O':
            dfs(i, m - 1, visited, mat, r, c)
    
    # Replace 'O's that are not visited (i.e., surrounded by 'X') with 'X'
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 1 and mat[i][j] == 'O':
                mat[i][j] = 'X'
    
    return mat