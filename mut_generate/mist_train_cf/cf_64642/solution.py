"""
QUESTION:
Implement the function `solveSudoku(board)` that takes a 9x9 Sudoku board as input, where each cell is a digit, `.` (empty cell), or `*` (locked cell), and fills in the empty cells to form a valid Sudoku solution. The function should modify the input board in-place and should not return anything. The input board has only one solution and is guaranteed to satisfy the constraints: `board.length == 9` and `board[i].length == 9`.
"""

def solveSudoku(board):
    def is_valid(bo, row, col, num):
        for x in range(9):
            if bo[row][x] == num:
                return False
        for x in range(9):
            if bo[x][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if bo[i+start_row][j+start_col] == num:
                    return False
        return True

    def solve(bo):
        for i in range(9):
            for j in range(9):
                if bo[i][j] == ".":
                    for num in "123456789":
                        if is_valid(bo, i, j, num):
                            bo[i][j] = num  
                            if solve(bo):  
                                return True
                            bo[i][j] = "."  
                    return False  
        return True

    solve(board)