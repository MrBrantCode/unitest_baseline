"""
QUESTION:
Create a function called `is_valid_sudoku` that takes a 9x9 Sudoku puzzle as input and returns True if the puzzle is valid, and False otherwise. A valid Sudoku puzzle has the following properties: it is a 9x9 grid, all cells contain numbers from 1 to 9, and each row, column, and 3x3 sub-grid contains unique numbers from 1 to 9.
"""

def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                continue
            
            # Check row
            if val in rows[i]:
                return False
            rows[i].add(val)

            # Check column
            if val in cols[j]:
                return False
            cols[j].add(val)

            # Check box
            box_index = (i // 3) * 3 + j // 3
            if val in boxes[box_index]:
                return False
            boxes[box_index].add(val)

    return True