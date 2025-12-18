"""
QUESTION:
Write a function `isValidSudoku` that takes a 9x9 grid as input and returns `True` if the Sudoku puzzle is valid, and `False` otherwise. A valid Sudoku puzzle is one where each row, each column, and each 3x3 sub-grid contains unique numbers from 1 to 9, inclusive. The function should have a time complexity of O(n^2) and a space complexity of O(n^2).
"""

def isValidSudoku(board):
    """
    This function checks if a Sudoku puzzle is valid.
    
    Args:
    board (list): A 9x9 grid representing the Sudoku puzzle.
    
    Returns:
    bool: True if the Sudoku puzzle is valid, False otherwise.
    """
    
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