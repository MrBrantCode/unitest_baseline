"""
QUESTION:
Implement a function `isValidSudoku` to determine if a given Sudoku puzzle is valid, with a time complexity of O(n^2) and a space complexity of O(n^2), where n is the size of the puzzle. The input will be a 2D array representing the Sudoku puzzle, where 0 represents an empty cell and numbers 1-9 represent filled cells. The function should return a boolean value indicating whether the Sudoku puzzle is valid.
"""

def isValidSudoku(board):
    n = 9
    rows = [[False] * n for _ in range(n)]
    columns = [[False] * n for _ in range(n)]
    boxes = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            value = board[i][j]
            if value == 0:
                continue
            if not 1 <= value <= n:
                return False
            box_index = (i // 3) * 3 + j // 3
            if rows[i][value - 1] or columns[j][value - 1] or boxes[box_index][value - 1]:
                return False
            rows[i][value - 1] = columns[j][value - 1] = boxes[box_index][value - 1] = True
    
    return True