"""
QUESTION:
Given a 2-D grid where 0 represents uninfected cells, 1 represents infected cells, and 2 represents cells immune to the virus, contain the spread of the virus by installing walls between adjacent cells. Each day, install walls around the affected area that threatens the most uninfected cells the following night. Return the total number of walls required to contain the virus or the number of walls used if the world becomes fully infected.

The grid size will be in the range [1, 50] with each cell being either 0, 1, or 2. Implement the function `containVirus` that takes the grid as input and returns the total number of walls required.
"""

def containVirus(grid):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    viruses = []
    walls = [0]
    while True:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        viruses = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    cells = []
                    perimeter = 0
                    stack = [(i,j)]
                    visited[i][j] = 1
                    while stack:
                        x, y = stack.pop()
                        cells.append((x, y))
                        for di, dj in d:
                            ni, nj = x+di, y+dj
                            if 0<=ni<len(grid) and 0<=nj<len(grid[0]):
                                if grid[ni][nj] == 1 and visited[ni][nj] == 0:
                                    stack.append((ni, nj))
                                    visited[ni][nj] = 1
                                elif grid[ni][nj] == 0:
                                    perimeter += 1
                            else:
                                perimeter += 1
                    viruses.append((cells, perimeter))
        if not viruses:
            return walls[0]
        max_virus = max(viruses, key=lambda x: x[1])
        viruses.remove(max_virus)
        walls[0] += max_virus[1]
        for i, j in max_virus[0]:
            grid[i][j] = -1
        for i, j in [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]:
            for di, dj in d:
                ni, nj = i+di, j+dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 0:
                    grid[ni][nj] = 1