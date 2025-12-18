"""
QUESTION:
Implement a `solve_sudoku` function that takes a 2D list representing a Sudoku board as input and returns `True` if the puzzle can be solved, and `False` otherwise. The function should fill in the empty cells (represented by 0) with numbers from 1 to 9 such that each row, column, and 3x3 sub-grid contains each number only once. The function should use backtracking and recursion to solve the puzzle.
"""

def solve_sudoku(board):
    def valid(board, num, pos):
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        square_x = pos[1] // 3
        square_y = pos[0] // 3

        for i in range(square_y*3, square_y*3 + 3):
            for j in range(square_x * 3, square_x*3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False

        return True


    def find_empty(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)  

        return None


    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False