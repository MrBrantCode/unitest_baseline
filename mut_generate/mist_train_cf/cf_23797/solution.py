"""
QUESTION:
Implement a function `solve` that takes a 2D list `bo` representing a Sudoku board as input and returns `True` if the Sudoku puzzle can be solved using backtracking, and `False` otherwise. The board is represented as a 9x9 grid, where zeros indicate empty cells. The function should fill in the empty cells with numbers from 1 to 9 such that each row, column, and 3x3 box contains each number exactly once.
"""

def solve(bo):
    """
    Solves a Sudoku puzzle using backtracking.

    Args:
    bo (list): A 2D list representing a Sudoku board.

    Returns:
    bool: True if the Sudoku puzzle can be solved, False otherwise.
    """
    def valid(num, pos):
        # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty():
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col

    find = find_empty()
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False