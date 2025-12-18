"""
QUESTION:
canMouseWin function: Determine if the mouse can win in the Cat and Mouse game.

Given a rows x cols matrix grid, where each element is a wall, floor, player (Cat, Mouse), food, or a trap, and two integers catJump and mouseJump representing the maximum lengths Cat and Mouse can jump at a time, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.

Restrictions: 
- rows == grid.length
- cols = grid[i].length
- 1 <= rows, cols <= 8
- grid[i][j] consist only of characters 'C', 'M', 'F', '.', '#', and 'T'.
- There is only one of each character 'C', 'M', and 'F' in grid.
- 1 <= catJump, mouseJump <= 8
"""

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def canMouseWin(grid, catJump, mouseJump):
    rows, cols = len(grid), len(grid[0])
    cat, mouse, food = None, None, None
    dp = [[[[[None for _ in range(2)] for _ in range(cols)] for _ in range(rows)] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'C':
                cat = (i, j)
            elif grid[i][j] == 'M':
                mouse = (i, j)
            elif grid[i][j] == 'F':
                food = (i, j)
    queue = []
    for i in range(rows):
        for j in range(cols):
            for k in range(2):
                dp[i][j][food[0]][food[1]][k] = False
                queue.append((i, j, food[0], food[1], k))
                if grid[i][j] != '#':
                    dp[i][j][i][j][1-k] = True
                    queue.append((i, j, i, j, 1-k))
    while queue:
        i, j, x, y, k = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + k*dx, y + k*dy
            nk = 1-k
            if not (0 <= nx < rows and 0 <= ny < cols):
                continue
            if k == 0 and max(abs(nx-x), abs(ny-y)) > catJump:
                continue
            if k == 1 and max(abs(nx-x), abs(ny-y)) > mouseJump:
                continue
            if dp[nx][ny][i][j][nk] is None and grid[nx][ny] != '#':
                dp[nx][ny][i][j][nk] = not dp[i][j][x][y][k]
                queue.append((nx, ny, i, j, nk))
                if nx == i and ny == j and dp[nx][ny][nx][ny][nk] and dp[nx][ny][nx][ny][1-nk] is None:
                    dp[nx][ny][nx][ny][1-nk] = not dp[nx][ny][nx][ny][nk]
                    queue.append((nx, ny, nx, ny, 1-nk))
    return dp[mouse[0]][mouse[1]][cat[0]][cat[1]][1] if dp[mouse[0]][mouse[1]][cat[0]][cat[1]][1] is not None else False