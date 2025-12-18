"""
QUESTION:
Create a function `isolate_regions(board)` that takes a 2D matrix `board` of size `m x n` containing `'X'`, `'O'`, and `'#'` characters, and modifies the board in-place to isolate regions of `'O'` characters that are completely surrounded by `'X'` and `'#'` characters and do not connect to any `'O'` on the border of the board. The function should not pass through `'#'` characters during this process, and the `'O'` characters on the border are not considered isolated. The function should run in O(m * n) time complexity.
"""

def isolate_regions(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'T'
            for x, y in directions:
                dfs(i + x, j + y)

    # Mark all 'O's connected to the border
    for i in range(m):
        dfs(i, 0)
        dfs(i, n - 1)
    for j in range(n):
        dfs(0, j)
        dfs(m - 1, j)

    # Flip 'O's and 'T's
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'