"""
QUESTION:
Write a function named `find_line` that takes a 2D binary matrix as input and returns the start and end coordinates of the longest line (horizontal, vertical, diagonal, or anti-diagonal) of consecutive 1s in the matrix. The function should return the coordinates in the format (row, column). The longest line can be horizontal, vertical, diagonal, or anti-diagonal. If there are multiple longest lines, return the one that appears first from top to bottom and left to right. The matrix is 0-indexed.
"""

def find_line(matrix):
    """
    This function finds the longest line (horizontal, vertical, diagonal, or anti-diagonal) 
    of consecutive 1s in a given 2D binary matrix and returns its start and end coordinates.

    Args:
        matrix (list): A 2D binary matrix.

    Returns:
        tuple: The start and end coordinates of the longest line.
    """

    row = len(matrix)
    col = len(matrix[0])

    # Initialize dp tables to store lengths of lines
    dpHorizontal = [[0]*col for _ in range(row)]
    dpVertical = [[0]*col for _ in range(row)]
    dpDiagonal = [[0]*col for _ in range(row)]
    dpAntiDiagonal = [[0]*col for _ in range(row)]

    maxLen = 0
    start = (0, 0)
    end = (0, 0)

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                # For Horizontal line
                dpHorizontal[i][j] = dpHorizontal[i-1][j] + 1 if i > 0 else 1
                
                # For Vertical Line
                dpVertical[i][j] = dpVertical[i][j-1] + 1 if j > 0 else 1
                
                # For Diagonal Line
                dpDiagonal[i][j] = dpDiagonal[i-1][j-1] + 1 if i > 0 and j > 0 else 1
                
                # For Anti-Diagonal Line
                dpAntiDiagonal[i][j] = dpAntiDiagonal[i-1][j+1] + 1 if i > 0 and j < col-1 else 1
                
                # Update maximum length and its indices
                maxList = [dpHorizontal[i][j], dpVertical[i][j], dpDiagonal[i][j], dpAntiDiagonal[i][j]]
                if maxLen < max(maxList):
                    maxLen = max(maxList)
                    
                    if dpHorizontal[i][j] == maxLen:
                        start = (i - maxLen + 1, j)
                    elif dpVertical[i][j] == maxLen:
                        start = (i, j - maxLen + 1)
                    elif dpDiagonal[i][j] == maxLen:
                        start = (i - maxLen + 1, j - maxLen + 1)
                    elif dpAntiDiagonal[i][j] == maxLen:
                        start = (i - maxLen + 1, j + maxLen - 1)
                    
                    end = (i, j)

    return start, end