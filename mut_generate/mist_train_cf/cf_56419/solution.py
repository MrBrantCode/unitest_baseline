"""
QUESTION:
Write a function `isValidSudoku(board)` that takes a 9x9 2D list representing a completed Sudoku puzzle as input and returns `True` if the puzzle is valid according to Sudoku rules (each row, column, and 3x3 sub-grid contains the numbers 1-9 without repetition) and `False` otherwise. The input may contain zeros to represent empty cells, which should be ignored in the validation process.
"""

def isValidSudoku(board):
    rowSet = [set() for _ in range(9)]
    colSet = [set() for _ in range(9)]
    gridSet = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            currentVal = board[i][j]
            if currentVal == 0: 
                continue
            
            # Check row
            if currentVal in rowSet[i]:
                return False
            rowSet[i].add(currentVal)
            
            # Check column
            if currentVal in colSet[j]:
                return False
            colSet[j].add(currentVal)
            
            # check grid
            gridIndex = (i // 3 ) * 3 + j // 3
            if currentVal in gridSet[gridIndex]:
                return False
            gridSet[gridIndex].add(currentVal)
    
    return True