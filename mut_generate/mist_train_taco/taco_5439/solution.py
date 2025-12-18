"""
QUESTION:
Read problems statements [Mandarin] , [Bengali] , [Hindi] , [Russian] and [Vietnamese] as well.

You are given a grid with $N$ rows and $M$ columns; each cell of this grid is either empty or contains an obstacle. Initially, all cells are colorless.

You may perform the following operation an arbitrary number of times (including zero): choose a $2\times 2$ square in the grid and color all four of its cells. Each cell may be colored any number of times.

You want all empty cells to be colored and all cells containing obstacles to be colorless. Find out if this state can be achieved.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $M$. 
The following $N$ lines describe the grid. Each of these lines contains a string with length $M$ containing only characters '.' (denoting an empty cell) and '#' (denoting a cell with an obstacle).

------  Output ------
For each test case, print a single line containing the string "YES" if it possible to color the grid in the required way or "NO" if it is impossible (without quotes).

------  Constraints ------
$1 ≤ T ≤ 10,000$
$2 ≤ N, M ≤ 10^{3}$
the sum of $N\cdot M$ over all test cases does not exceed $5,000,000$

------  Subtasks ------
Subtask #1 (30 points): only the first row of the grid may contain obstacles

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
2

3 3

..#

...

...

3 3

...

.#.

...
----- Sample Output 1 ------ 
YES

NO
"""

def can_color_grid(grid, n, m):
    marked = [[0] * m for _ in range(n)]
    
    # Mark all cells that can be colored in a 2x2 square
    for i in range(n - 1):
        for j in range(m - 1):
            if (grid[i][j] == '.' and grid[i + 1][j] == '.' and
                grid[i][j + 1] == '.' and grid[i + 1][j + 1] == '.'):
                marked[i][j] = 1
                marked[i + 1][j] = 1
                marked[i][j + 1] = 1
                marked[i + 1][j + 1] = 1
    
    # Check if all empty cells are marked
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and marked[i][j] == 0:
                return "NO"
    
    return "YES"