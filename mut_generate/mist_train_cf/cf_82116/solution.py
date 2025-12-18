"""
QUESTION:
Write a function named `placeRooks` that takes one argument `n` representing the size of an N x N chessboard and places N rooks on the board such that no two rooks are in the same row or column. The function should print all valid placements of rooks on the board.
"""

def placeRooks(n):
    def canPlace(board, occupiedRows, considerRow):
        for i in range(occupiedRows):
            if board[i] == considerRow or \
                board[i] - i == considerRow - occupiedRows or \
                board[i] + i == considerRow + occupiedRows:
                return False
        return True

    def placeRook(board, occupiedRows):
        if occupiedRows == n:
            print(board)
            print("\n")
            return
        for i in range(n):
            if canPlace(board, occupiedRows, i):
                board[occupiedRows] = i
                placeRook(board, occupiedRows + 1)

    board = [-1]*n
    placeRook(board, 0)