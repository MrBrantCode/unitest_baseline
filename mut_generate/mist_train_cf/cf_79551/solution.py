"""
QUESTION:
Given a rectangular grid where grid[i][j] = 1 represents land, grid[i][j] = 0 represents water, and grid[i][j] = 2 represents a bridge, determine the perimeter of the island including the bridges. Bridges do not contribute to the perimeter, but the land cells they connect do. The island does not have "lakes" and is completely surrounded by water. The grid has a maximum width and height of 100, and row == grid.length, col == grid[i].length. Implement a function islandPerimeter(grid) to solve this problem.
"""

def island_perimeter(grid):
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    q = []
    visited = set()
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] in (1,2):
                q.append((i,j))
                visited.add((i,j))
                break
        else:
            continue
        break

    cnt = 0
    while(q):
        i, j = q.pop(0)
        for x, y in dirs:
            ni, nj = i + x, j + y
            if ni < 0 or ni == m or nj < 0 or nj == n or grid[ni][nj] == 0:
                cnt += 1
            elif grid[ni][nj] in (1,2) and (ni,nj) not in visited:
                visited.add((ni,nj))
                q.append((ni,nj))

    return cnt