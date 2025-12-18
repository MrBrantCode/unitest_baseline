"""
QUESTION:
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
 
Example 1:
Input: A = [[0,1],[1,0]]
Output: 1
Example 2:
Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:
Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

 
Constraints:

2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""

from collections import deque
from typing import List

def shortest_bridge_distance(A: List[List[int]]) -> int:
    (m, n) = (len(A), len(A[0]))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    boundary = set()
    found = False
    
    # Step 1: Identify the first island and mark its boundary
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                A[i][j] = 2
                queue.append((i, j))
                while queue:
                    (ci, cj) = queue.popleft()
                    for (di, dj) in dirs:
                        (ni, nj) = (ci + di, cj + dj)
                        if 0 <= ni < m and 0 <= nj < n:
                            if A[ni][nj] == 1:
                                A[ni][nj] = 2
                                queue.append((ni, nj))
                            elif A[ni][nj] == 0:
                                boundary.add((ci, cj))
                found = True
                break
        if found:
            break
    
    # Step 2: Use BFS from the boundary to find the shortest path to the second island
    queue = deque(boundary)
    steps = 0
    while queue:
        for _ in range(len(queue)):
            (i, j) = queue.popleft()
            for (di, dj) in dirs:
                (ni, nj) = (i + di, j + dj)
                if 0 <= ni < m and 0 <= nj < n:
                    if A[ni][nj] == 0:
                        A[ni][nj] = 2
                        queue.append((ni, nj))
                    elif A[ni][nj] == 1:
                        return steps
        steps += 1