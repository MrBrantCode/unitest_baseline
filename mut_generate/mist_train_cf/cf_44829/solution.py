"""
QUESTION:
Write a function `maxSumPath` that takes a 2D list `chessboard` and an integer `k` as input, and returns the maximum sum path of length `k` from the bottom right corner of the `chessboard` to any other cell in the `chessboard`. The path can move in any of the four directions (up, down, left, right) and cannot visit the same cell more than once. If the input `chessboard` is not a list, or if it's not a square, or if the steps `k` is not between 1 and `N*N`, return an error message. The values in the `chessboard` must be between 1 and `N*N`.
"""

def maxSumPath(chessboard, k):
    if not isinstance(chessboard, list):
        return "Error: Chessboard must be a list"
        
    N = len(chessboard)
    if not all(len(row) == N for row in chessboard):
        return "Error: Chessboard must be a square"
    if not 1 <= k <= N*N:
        return "Error: Steps must be between 1 and N*N"

    for row in chessboard:
        for square in row:
            if not 1 <= square <= N*N:
                return "Error: Square values must be between 1 and N*N"

    max_sum = [0]
    max_path = [None]
    visited = [[False]*N for _ in range(N)]

    def next_positions(x, y):
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                yield nx, ny
                
    def dfs(x, y, k, path, path_sum):
        if k == 0:
            if path_sum > max_sum[0]:
                max_sum[0] = path_sum
                max_path[0] = path.copy()
            return
        for nx, ny in next_positions(x, y):
            visited[nx][ny] = True
            path.append(chessboard[nx][ny])
            dfs(nx, ny, k-1, path, path_sum + chessboard[nx][ny])
            visited[nx][ny] = False
            path.pop()

    visited[N-1][N-1] = True
    dfs(N-1, N-1, k-1, [chessboard[N-1][N-1]], chessboard[N-1][N-1])
    
    return max_path[0]