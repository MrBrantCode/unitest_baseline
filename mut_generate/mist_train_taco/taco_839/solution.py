"""
QUESTION:
Given a path in the form of a rectangular matrix having few landmines arbitrarily placed (marked as 0), calculate length of the shortest safe route possible from any cell in the first column to any cell in the last column of the matrix. We have to avoid landmines and their four adjacent cells (left, right, above and below) as they are also unsafe. We are allowed to move to only adjacent cells which are not landmines. i.e. the route cannot contains any diagonal moves.
 
Example 1:
Input:
[1 0 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 0 1]
[1 1 1 1 0]
Output: 6
Explanation: 
We can see that length of shortest
safe route is 13 (Highlighted in Bold).
[1 0 1 1 1]
[1 1 1 1 1] 
[1 1 1 1 1]
[1 1 1 0 1] 
[1 1 1 1 0]
Example 2:
Input:
[1 1 1 1 1]
[1 1 0 1 1]
[1 1 1 1 1]
Output: -1
Explanation: There is no possible path from
first column to last column.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findShortestPath() which takes matrix as input parameter and return an integer denoting the shortest path. If there is no possible path, return -1. 
Expected Time Complexity: O(R * C)
Expected Auxiliary Space: O(1)
Constraints:
1 <= R,C <= 10^{3}
"""

from typing import List

def find_shortest_safe_path(matrix: List[List[int]]) -> int:
    (n, m) = (len(matrix), len(matrix[0]))
    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def out_of_bounds(i, j):
        return i < 0 or i >= n or j < 0 or j >= m

    def is_safe(i, j):
        if out_of_bounds(i, j) or matrix[i][j] == 0:
            return False
        for d in dr:
            (x, y) = (i + d[0], j + d[1])
            if not out_of_bounds(x, y) and matrix[x][y] == 0:
                return False
        return True

    def rec(i, j):
        if memo[i][j] != -1 and memo[i][j] != float('inf'):
            return memo[i][j]
        if j == m - 1:
            return 1
        visited.add((i, j))
        min_ = float('inf')
        for d in dr:
            if d == (0, -1):
                continue
            (x, y) = (i + d[0], j + d[1])
            if (x, y) not in visited and is_safe(x, y):
                min_ = min(min_, 1 + rec(x, y))
        memo[i][j] = min_
        visited.remove((i, j))
        return memo[i][j]

    visited = set()
    memo = [[-1 for _ in range(m)] for _ in range(n)]
    min_ = float('inf')
    for i in range(n):
        if is_safe(i, 0):
            min_ = min(min_, rec(i, 0))
    return -1 if min_ == float('inf') else min_