"""
QUESTION:
Implement a function named `solve` that takes one integer argument `n`, which represents the number of rooks to be placed on an n x n chessboard. The function should return a 2D list representing the final configuration of the board where `n` rooks are placed such that none of them are in the same row or column. If no such configuration is possible, return a message indicating that a solution does not exist.
"""

def isSafe(board, row, column):
    for i in range(column):
        if board[row][i] == 1:
            return False
    return True


def solveNrooks(board, column):
    N = len(board)
    if column >= N:
        return True
    for i in range(N):
        if isSafe(board, i, column):
            board[i][column] = 1
            if solveNrooks(board, column + 1) == True:
                return True
            board[i][column] = 0
    return False


def solve(n):
    board = [[0]*n for _ in range(n)]
    if solveNrooks(board, 0) == False:
        return "Solution does not exist"
    return board