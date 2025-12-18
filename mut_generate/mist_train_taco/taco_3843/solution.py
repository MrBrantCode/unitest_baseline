"""
QUESTION:
Geek is in a maze of size N * M. Each cell in the maze is made of either '.' or '#'. An empty cell is represented by '.' and an obstacle is represented by '#'. If Geek starts at cell (R, C), find how many different empty cells he can pass through while avoiding the obstacles. He can move in any of the four directions but he can move up at most U times and he can move down atmost D times. 
 
Example 1:
Input: 
N = 3, M = 3
R = 1, C = 0
U = 1, D = 1
mat = {{'.', '.', '.'},
       {'.', '#', '.'},
       {'#', '.', '.'}}
Output: 5
Explanation: Geek can reach 
(1, 0), (0, 0), (0, 1), (0, 2), (1, 2) 
Example 2:
Input: 
N = 3, M = 4
R = 1, C = 0
U = 1, D = 2 
mat = {{'.', '.', '.'}, 
       {'.', '#', '.'}, 
       {'.', '.', '.'},
       {'#', '.', '.'}} 
Output: 10
Explanation: Geek can reach all the 
cells except for the obstacles.
 
Your Task:  
You don't need to read input or print anything. Complete the function numberOfCells() which takes N, M, R, C, U, D and the two dimensional character array mat[][] as input parameters and returns the number of cells geek can visit( If he is standing on obstacle he can not move). 
Constraints:
1 ≤ N*M ≤ 10^{6}
mat[i][j] = '#" or '.'
0 ≤ R ≤ N-1
0 ≤ C ≤ M-1
"""

import heapq as hq

def numberOfCells(n, m, r, c, u, d, mat):
    def isValid(row, col):
        return 0 <= row < n and 0 <= col < m

    if mat[r][c] == '#':
        return 0
    
    pque = []
    vis = [[0 for _ in range(m)] for _ in range(n)]
    hq.heappush(pque, ((0, 0), (r, c)))
    vis[r][c] = 1
    
    while pque:
        (up, down) = (pque[0][0][0], pque[0][0][1])
        (x, y) = (pque[0][1][0], pque[0][1][1])
        hq.heappop(pque)
        
        # Move Up
        if isValid(x - 1, y):
            if up + 1 <= u and (not vis[x - 1][y]) and (down <= d) and (mat[x - 1][y] == '.'):
                hq.heappush(pque, ((up + 1, down), (x - 1, y)))
                vis[x - 1][y] = 1
        
        # Move Down
        if isValid(x + 1, y):
            if down + 1 <= d and (not vis[x + 1][y]) and (up <= u) and (mat[x + 1][y] == '.'):
                hq.heappush(pque, ((up, down + 1), (x + 1, y)))
                vis[x + 1][y] = 1
        
        # Move Left
        if isValid(x, y - 1):
            if down <= d and (not vis[x][y - 1]) and (up <= u) and (mat[x][y - 1] == '.'):
                hq.heappush(pque, ((up, down), (x, y - 1)))
                vis[x][y - 1] = 1
        
        # Move Right
        if isValid(x, y + 1):
            if down <= d and (not vis[x][y + 1]) and (up <= u) and (mat[x][y + 1] == '.'):
                hq.heappush(pque, ((up, down), (x, y + 1)))
                vis[x][y + 1] = 1
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 1:
                ans += 1
    
    return ans