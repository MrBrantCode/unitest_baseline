"""
QUESTION:
You are given an n x n integer matrix grid where each value grid[i][j] represents height of the cell (i, j).
You can travel from a cell to another 4-directionally adjacent cell if and only the height of the both cells are at most T. You can travel infinite distances in zero time but you must stay within the boundaries of the grid during your travel.
You are currently at cell (0 , 0) and the value of T is 0.and you wish to go to cell (n-1,m-1).
Find the minimum time it will take to reach the cell (n, m) if the value of T increase by 1 every second.
 
Example 1:
Input:
2
0 2
1 3
Output:
3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When time T is 3, we can swim anywhere inside the grid.
 
Example 2:
Input:
4
0 1 2 4
12 13 14 9
15 5 11 10
3 6 7 8 
Output:
10
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Solve() which takes an integer n denoting no. of rows and columns of the grid and a matrix grid[][] denoting the grid and return the maximum group of connected group of 1s.
 
Constraints:
	1 <= n<= 50
	0 <= grid[i][j] 
	Each values in grid is unique
"""

import heapq

def minimum_time_to_reach_end(n, grid):
    hp = []
    ans = grid[0][0]
    heapq.heappush(hp, [grid[0][0], 0, 0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = set()
    visited.add((0, 0))
    
    while hp:
        (t, i, j) = heapq.heappop(hp)
        ans = max(t, ans)
        if i == n - 1 and j == n - 1:
            return ans
        for (d1, d2) in directions:
            x = i + d1
            y = j + d2
            if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                visited.add((x, y))
                heapq.heappush(hp, [grid[x][y], x, y])
    
    return ans