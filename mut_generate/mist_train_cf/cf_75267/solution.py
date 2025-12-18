"""
QUESTION:
Design a function `solve_n_rooks(n)` to solve the N-Rooks problem where you have to place N rooks on an N x N chessboard such that no two rooks can attack each other. The function should take an integer `n` as input representing the size of the chess board and print the possible configurations if a solution exists. The function should return `True` if a solution exists and `False` otherwise.
"""

def solve_n_rooks(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        return True

    def solve_n_rooks_util(board, col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve_n_rooks_util(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    board = [[0]*n for _ in range(n)]
    if not solve_n_rooks_util(board, 0):
        print ("Solution does not exist")
        return False
    print("Solution exists and the possible configurations are:")
    for i in range(n):
        for j in range(n):
            print (board[i][j], end = " ")
        print()
    return True