"""
QUESTION:
An L-shape is a figure on gridded paper that looks like the first four pictures below. An L-shape contains exactly three shaded cells (denoted by *), which can be rotated in any way.

You are given a rectangular grid. Determine if it contains L-shapes only, where L-shapes can't touch an edge or corner. More formally:

Each shaded cell in the grid is part of exactly one L-shape, and

no two L-shapes are adjacent by edge or corner.

For example, the last two grids in the picture above do not satisfy the condition because the two L-shapes touch by corner and edge, respectively.


-----Input-----

The input consists of multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 100$) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers $n$ and $m$ ($1 \leq n, m \leq 50$) — the number of rows and columns in the grid, respectively.

Then $n$ lines follow, each containing $m$ characters. Each of these characters is either '.' or '*' — an empty cell or a shaded cell, respectively.


-----Output-----

For each test case, output "YES" if the grid is made up of L-shape that don't share edges or corners, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).


-----Examples-----

Input
10
6 10
........**
.**......*
..*..*....
.....**...
...*.....*
..**....**
6 10
....*...**
.**......*
..*..*....
.....**...
...*.....*
..**....**
3 3
...
***
...
4 4
.*..
**..
..**
..*.
5 4
.*..
**..
....
..**
..*.
3 2
.*
**
*.
2 3
*..
.**
3 2
..
**
*.
3 3
.**
*.*
**.
3 3
..*
.**
..*
Output
YES
NO
NO
NO
YES
NO
NO
YES
NO
NO


-----Note-----

None
"""

def validate_l_shapes(n, m, grid):
    """
    Validates if the given grid contains only valid L-shapes that do not share edges or corners.

    Parameters:
    n (int): Number of rows in the grid.
    m (int): Number of columns in the grid.
    grid (list of list of str): The grid containing '.' (empty cell) and '*' (shaded cell).

    Returns:
    bool: True if the grid contains only valid L-shapes, False otherwise.
    """
    def is_valid_l_shape(i, j):
        """
        Checks if the cell at (i, j) forms a valid L-shape with its neighbors.
        """
        t = 0
        for (a, b) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            if 0 <= i + a < n and 0 <= j + b < m and grid[i + a][j + b] == '*':
                t += 1
        for (a, b) in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
            if 0 <= i + a < n and 0 <= j + b < m and grid[i + a][j + b] == '*':
                t += 1
                if grid[i + a][j] != '*' and grid[i][j + b] != '*':
                    return False
        return t == 2

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                if not is_valid_l_shape(i, j):
                    return False
    return True