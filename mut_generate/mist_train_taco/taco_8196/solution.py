"""
QUESTION:
Given a N x M grid. Find All possible paths from top left to bottom right.From each cell you can either move only to right or down.
Example 1:
Input: 1 2 3
       4 5 6
Output: 1 4 5 6
        1 2 5 6 
        1 2 3 6
Explanation: We can see that there are 3 
paths from the cell (0,0) to (1,2).
Example 2:
Input: 1 2
       3 4
Output: 1 2 4
        1 3 4
Your Task:
You don't need to read input or print anything. Your task is to complete the function findAllPossiblePaths() which takes two integers n,m and grid[][]  as input parameters and returns all possible paths from the top left cell to bottom right cell in a 2d array.
Expected Time Complexity: O(2^N*M)
Expected Auxiliary Space: O(N)
Constraints:
1 <= n,m <= 10^{ }
1 <= grid[i][j] <= n*m
n * m < 20
"""

from typing import List

def find_all_possible_paths(n: int, m: int, grid: List[List[int]]) -> List[List[int]]:
    def recur(temp, inx, i, j):
        if i + 1 < n and j < m:
            temp[inx] = grid[i + 1][j]
            recur(temp, inx + 1, i + 1, j)
        if i < n and j + 1 < m:
            temp[inx] = grid[i][j + 1]
            recur(temp, inx + 1, i, j + 1)
        if i == n - 1 and j == m - 1:
            paths.append(temp.copy())
            return

    paths = []
    temp = [0] * (m + n - 1)
    temp[0] = grid[0][0]
    temp[-1] = grid[-1][-1]
    recur(temp, 1, 0, 0)
    return paths