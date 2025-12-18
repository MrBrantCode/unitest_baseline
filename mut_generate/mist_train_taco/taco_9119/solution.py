"""
QUESTION:
Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).
Note: You can only move left, right, up and down, and only through cells that contain 1.
Example 1:
Input:
N=3
M=4
A=[[1,0,0,0], 
[1,1,0,1],[0,1,1,1]]
X=2
Y=3 
Output:
5
Explanation:
The shortest path is as follows:
(0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(2,3).
Example 2:
Input:
N=3
M=4
A=[[1,1,1,1],
[0,0,0,1],[0,0,0,1]]
X=0
Y=3
Output:
3
Explanation:
The shortest path is as follows:
(0,0)->(0,1)->(0,2)->(0,3).
Your Task:
You don't need to read input or print anything. Your task is to complete the function shortestDistance() which takes the integer N, M, X, Y, and the 2D binary matrix A as input parameters and returns the minimum number of steps required to go from (0,0) to (X, Y).If it is impossible to go from (0,0) to (X, Y),then function returns -1. If value of the cell (0,0) is 0 (i.e  A[0][0]=0) then return -1.
Expected Time Complexity:O(N*M)
Expected Auxillary Space:O(N*M)
 
Constraints:
1 <= N,M <= 250
0 <= X < N
0 <= Y < M
0 <= A[i][j] <= 1
"""

from collections import deque

def shortest_path_in_matrix(N, M, A, X, Y):
    if A[0][0] == 0:
        return -1
    
    directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = set()
    visited.add((0, 0))
    
    while queue:
        row, col, steps = queue.popleft()
        
        if row == X and col == Y:
            return steps
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < N and 0 <= new_col < M and 
                A[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))
    
    return -1