"""
QUESTION:
Write a function named `same_color_cells` that takes four integers as input representing the row and column numbers of two cells on a standard 8x8 chessboard. The function should return a string indicating whether the two cells have the same color. The row and column numbers are between 1 and 8 (inclusive).
"""

def entrance(row1, col1, row2, col2):
    if not (1 <= row1 <= 8 and 1 <= col1 <= 8 and 1 <= row2 <= 8 and 1 <= col2 <= 8):
        return "Invalid cell coordinates for a Chessboard!"

    if (row1 + col1) % 2 == (row2 + col2) % 2:
        return "YES, The two given cells have the SAME color."
    else:
        return "NO, The two given cells are NOT the same color."