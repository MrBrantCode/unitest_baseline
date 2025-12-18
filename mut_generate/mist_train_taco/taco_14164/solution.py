"""
QUESTION:
Given  a grid of n*m consisting of O's and X's. The task is to find the number of 'X' total shapes.
Note: 'X' shape consists of one or more adjacent X's (diagonals not included).
 
Example 1:
Input: grid = {{X,O,X},{O,X,O},{X,X,X}}
Output: 3
Explanation: 
The grid is-
X O X
O X O
X X X
So, X with same colour are adjacent to each 
other vertically for horizontally (diagonals 
not included). So, there are 3 different groups 
in the given grid.
Example 2:
Input: grid = {{X,X},{X,X}}
Output: 1
Expanation: 
The grid is- 
X X
X X
So, X with same colour are adjacent to each
other vertically for horizontally (diagonals
not included). So, there is only 1 group
in the given grid.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function xShape() which takes grid as input parameter and returns the count of total X shapes.
 
Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
 
Constraints:
1 ≤ n, m ≤ 100
"""

def count_x_shapes(grid):
    def solver(x, y):
        if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 'O':
            return
        grid[x][y] = 'O'
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            solver(x + dx, y + dy)

    row, col = len(grid), len(grid[0])
    area = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 'X':
                solver(i, j)
                area += 1
    return area