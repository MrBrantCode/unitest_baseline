"""
QUESTION:
containVirus function: Calculate the number of walls required to quarantine the infected area by installing walls around the region that threatens the most uninfected cells.

Input: 
- grid: a 3-D array of cells, where 0 represents uninfected cells, 1 represents cells contaminated with the virus, and 2 represents cells that are immune to the virus.

Restrictions: 
- The number of rows, columns and depth of grid will each be in the range [1, 50].
- Each grid[i][j][k] will be either 0, 1 or 2.
- Throughout the described process, there is always a contiguous viral region that will infect strictly more uncontaminated squares in the next round.
"""

def containVirus(grid):
    m, n, p = len(grid), len(grid[0]), len(grid[0][0])
    d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    def dfs(i, j, k, visited, temp, walls, vul):
        visited.add((i, j, k))
        temp.append((i, j, k))
        if grid[i][j][k] == 0:
            vul.append((i, j, k))
        for di, dj, dk in d:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < m and 0 <= nj < n and 0 <= nk < p and grid[ni][nj][nk] != 2 and (ni, nj, nk) not in visited:
                if grid[ni][nj][nk] == 1:
                    dfs(ni, nj, nk, visited, temp, walls, vul)
                else:
                    walls.append((ni, nj, nk))
    res = 0
    while True:
        visited = set()
        regions = []
        walls = []
        vul = []
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    if grid[i][j][k] == 1 and (i, j, k) not in visited:
                        temp = []
                        w = []
                        v = []
                        dfs(i, j, k, visited, temp, w, v)
                        regions.append(temp)
                        walls.append(w)
                        vul.append(v)
        if not regions:
            break
        idx = walls.index(max(walls, key=len))
        res += len(walls[idx])
        for i, j, k in regions[idx]:
            grid[i][j][k] = 2
        for i, j, k in vul[idx]:
            grid[i][j][k] = 1
    return res