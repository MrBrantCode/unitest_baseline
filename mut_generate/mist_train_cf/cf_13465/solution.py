"""
QUESTION:
Create a function called "solveNQueens" that takes an integer N as input, representing the size of an N×N chessboard. Implement a backtracking algorithm to place N queens on the board such that no two queens share the same row, column, or diagonal. The function should return the board configuration as a solution if one exists; otherwise, it should indicate that no solution exists.
"""

def solveNQueens(N):
    def isSafe(board, row, col):
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True

    def placeQueen(col, board):
        if col == N:
            return True
        for row in range(N):
            if isSafe(board, row, col):
                board[row][col] = 'Q'
                if placeQueen(col + 1, board):
                    return True
                board[row][col] = '.'
        return False

    board = [['.' for _ in range(N)] for _ in range(N)]
    if placeQueen(0, board):
        return board
    else:
        return None