"""
QUESTION:
Write a function `solve(board)` that takes a 2D list `board` of characters 'X' and 'O' and returns the modified board where all 'O' regions not connected to the border are replaced with 'X'. The board is an `m x n` matrix where `1 <= m, n <= 200` and `board[i][j]` is either 'X' or 'O'.
"""

def solve(board):
    if not board or not board[0]:
        return
    row, col = len(board), len(board[0])

    def dfs(x, y):
        if x < 0 or y < 0 or x >= row or y >= col or board[x][y] != 'O':
            return
        board[x][y] = 'B'
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

    for i in range(row): 
        dfs(i, 0)
        dfs(i, col-1)

    for j in range(col): 
        dfs(0, j)
        dfs(row-1, j)

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'B':
                board[i][j] = 'O'