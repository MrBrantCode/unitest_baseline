"""
QUESTION:
Geek is in a maze of size N * M (N rows, M columns). Each cell in the maze is made of either '.' or '#'. An empty cell is represented by '.' and an obstacle is represented by '#'. If Geek starts at cell (R, C), find how many different empty cells he can pass through while avoiding the obstacles. He can move in any of the four directions but he can move up at most U times and he can move down atmost D times.
 
 
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
N = 4, M = 3
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
You don't need to read input or print anything. Complete the function numberOfCells() which takes N, M, R, C, U, D and the two dimensional character array mat[][] as input parameters and returns the number of cells geek can visit. 
Constraints:
1 ≤ N*M ≤ 10^{6}
mat[i][j] = '#" or '.'
0 ≤ R ≤ N-1
0 ≤ C ≤ M-1
mat[R][C] = '.'
"""

from collections import deque

def count_reachable_cells(n, m, r, c, u, d, mat):
    def helper(i, j, u, d):
        if j > 0 and (i, j - 1) not in visited:
            visited.add((i, j - 1))
            queue.append((i, j - 1, u, d))
        if j < m - 1 and (i, j + 1) not in visited:
            visited.add((i, j + 1))
            queue.append((i, j + 1, u, d))
        if u > 0 and i > 0 and (i - 1, j) not in visited:
            visited.add((i - 1, j))
            queue.append((i - 1, j, u - 1, d))
        if d > 0 and i < n - 1 and (i + 1, j) not in visited:
            visited.add((i + 1, j))
            queue.append((i + 1, j, u, d - 1))

    if mat[r][c] == '#':
        return 0
    
    visited = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '#':
                visited.add((i, j))
    
    obstacles = len(visited)
    visited.add((r, c))
    queue = deque([(r, c, u, d)])
    
    while queue:
        a, b, u, d = queue.popleft()
        helper(a, b, u, d)
    
    return len(visited) - obstacles