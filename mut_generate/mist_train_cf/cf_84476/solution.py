"""
QUESTION:
Write a function `count_servers(grid)` that takes as input a 2D grid of integers representing servers, where 1 denotes a server and 0 denotes no server. The function should return a tuple containing the count of servers that can communicate with at least one other server and a list of coordinates of isolated servers. Two servers can communicate if they are on the same row or column, and a server is isolated if it is the only server in its row and column. The input grid has a maximum size of 250x250.
"""

def entance(grid):
    m, n = len(grid), len(grid[0])
    row, col = [0]*m, [0]*n
    isolated = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                row[i] += 1
                col[j] += 1
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if row[i] > 1 or col[j] > 1:
                    count += 1
                else:
                    isolated.append((i, j))
    return count, isolated