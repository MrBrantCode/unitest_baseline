"""
QUESTION:
Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.
Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.
Binary matrix is a matrix with all cells equal to 0 or 1 only.
Zero matrix is a matrix with all cells equal to 0.
 
Example 1:

Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.

Example 2:
Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We don't need to change it.

Example 3:
Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
Output: 6

Example 4:
Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix can't be a zero matrix

 
Constraints:

m == mat.length
n == mat[0].length
1 <= m <= 3
1 <= n <= 3
mat[i][j] is 0 or 1.
"""

from collections import deque
from typing import List

def min_flips_to_zero_matrix(mat: List[List[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    
    # Convert the matrix to an integer representation
    start = sum((val << i * n + j for (i, row) in enumerate(mat) for (j, val) in enumerate(row)))
    
    # Initialize the queue for BFS
    queue = deque([(start, 0)])
    seen = {start}
    
    # Directions for flipping (including the cell itself and its neighbors)
    dirs = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]
    
    while queue:
        current, d = queue.popleft()
        
        # If the current state is a zero matrix, return the number of steps
        if current == 0:
            return d
        
        # Explore all possible flips
        for i in range(m):
            for j in range(n):
                next_state = current
                for dir_ in dirs:
                    new_i = i + dir_[0]
                    new_j = j + dir_[1]
                    if 0 <= new_i < m and 0 <= new_j < n:
                        next_state ^= 1 << new_i * n + new_j
                
                # If the next state has not been seen, add it to the queue
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, d + 1))
    
    # If no zero matrix can be achieved, return -1
    return -1