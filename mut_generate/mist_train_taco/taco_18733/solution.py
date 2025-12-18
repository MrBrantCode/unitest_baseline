"""
QUESTION:
Consider an n × m grid. Initially all the cells of the grid are colored white. Lenny has painted some of the cells (at least one) black. We call a painted grid convex if one can walk from any black cell to any another black cell using a path of side-adjacent black cells changing his direction at most once during the path. In the figure below, the left grid is convex while the right one is not convex, because there exist two cells which need more than one time to change direction in their path. [Image] 

You're given a painted grid in the input. Tell Lenny if the grid is convex or not.


-----Input-----

The first line of the input contains two integers n and m (1 ≤ n, m ≤ 50) — the size of the grid. Each of the next n lines contains m characters "B" or "W". Character "B" denotes a black cell of the grid and "W" denotes a white cell of the grid.

It's guaranteed that the grid has at least one black cell.


-----Output-----

On the only line of the output print "YES" if the grid is convex, otherwise print "NO". Do not print quotes.


-----Examples-----
Input
3 4
WWBW
BWWW
WWWB

Output
NO

Input
3 1
B
B
W

Output
YES
"""

def is_grid_convex(n, m, grid):
    row_sum = []
    col_sum = []
    black = []
    
    # Calculate row sums
    for i in range(n):
        t = [0]
        for j in range(m):
            t += [t[j] + (grid[i][j] == 'B')]
        row_sum.append(t)
    
    # Calculate column sums
    for i in range(m):
        t = [0]
        for j in range(n):
            t += [t[j] + (grid[j][i] == 'B')]
        col_sum.append(t)
    
    # Identify black cells and their neighbors
    d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'W':
                continue
            w = 0
            for di in d:
                x = i + di[0]
                y = j + di[1]
                if x < 0 or y < 0 or x >= n or y >= m:
                    w += 1
                    continue
                if grid[x][y] == 'W':
                    w += 1
            if w > 0:
                black.append((i, j))
    
    # Helper functions to check rows and columns
    def row_check(r, s, e):
        if s > e:
            s, e = e, s
        return row_sum[r][e + 1] - row_sum[r][s] == e - s + 1
    
    def col_check(c, s, e):
        if s > e:
            s, e = e, s
        return col_sum[c][e + 1] - col_sum[c][s] == e - s + 1
    
    # Check convexity
    res = True
    for i in black:
        for j in black:
            if i <= j:
                continue
            a = row_check(i[0], i[1], j[1]) and col_check(j[1], i[0], j[0])
            b = row_check(j[0], i[1], j[1]) and col_check(i[1], i[0], j[0])
            res = res and (a or b)
    
    return 'YES' if res else 'NO'