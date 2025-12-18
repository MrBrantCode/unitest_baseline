"""
QUESTION:
Write a function `maxSumPath(grid, k)` that finds the path with the maximum sum in a given grid, where the path can take at most `k` steps. The allowed moves are up, down, left, and right, and the path can only move to adjacent cells. The function should return the path with the maximum sum.
"""

def maxSumPath(grid, k):
  N = len(grid)
  dp = [[[-float('inf')] * (k + 1) for _ in range(N)] for _ in range(N)]
  moves = [(0, 0), (-1, 0), (0, 1), (0, -1)]

  for i in range(N):
    for j in range(N):
      dp[i][j][0] = grid[i][j]

  for m in range(1, k):
    for x in range(N):
      for y in range(N):
        for dx, dy in moves:
          nx, ny = x + dx, y + dy
          if 0 <= nx < N and 0 <= ny < N:
            dp[nx][ny][m] = max(dp[nx][ny][m], dp[x][y][m - 1] + grid[nx][ny])

  start_x, start_y, max_sum = max(((x, y, dp[x][y][k - 1]) for x in range(N) for y in range(N)), key=lambda item: item[2])

  # backtrack to find the path
  path = [grid[start_x][start_y]]
  remaining_sum = max_sum - grid[start_x][start_y]
  for m in range(k - 1, 0, -1):
    for dx, dy in moves:
      nx, ny = start_x + dx, start_y + dy
      if 0 <= nx < N and 0 <= ny < N and dp[nx][ny][m - 1] == remaining_sum:
        path.append(grid[nx][ny])
        start_x, start_y = nx, ny
        remaining_sum -= grid[nx][ny]
        break
  
  path.reverse()
  return path