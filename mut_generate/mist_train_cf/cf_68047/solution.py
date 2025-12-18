"""
QUESTION:
Design an efficient algorithm to solve the generalized N-rooks problem where rooks can attack diagonally. Implement a function `N_queen(n, board)` that takes two parameters: an integer `n` representing the number of rooks and a 2D array `board` of size `n x n` representing the chessboard. The function should return `True` if a solution is found and `False` otherwise. The function should also modify the `board` to represent the solution, where `1` represents a rook and `0` represents an empty space. Ensure that no two rooks are in the same row, column, or diagonal.
"""

def N_queen(n, board):
    N = n
    def is_attack(i, j, board):
        for k in range(0,N):
            if board[i][k]==1 or board[k][j]==1:
                return True
        for k in range(0,N):
            for l in range(0,N):
                if (k+l==i+j) or (k-l==i-j):
                    if board[k][l]==1:
                        return True
        return False

    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_attack(i,j,board))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queen(n-1,board)==True:
                    return True
                board[i][j] = 0
    return False