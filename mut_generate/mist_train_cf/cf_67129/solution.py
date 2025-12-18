"""
QUESTION:
Write a function `longest_consecutive_ones(matrix)` that takes a 2D list of 0s and 1s as input and returns the length of the longest line of consecutive ones in the matrix along with its start and end coordinates. The line can be horizontal, vertical, diagonal, or anti-diagonal. The function must have a time complexity of O(m*n) where m and n are the number of rows and columns in the matrix, and it should not use any built-in functions or libraries.
"""

def longest_consecutive_ones(matrix):
    if not matrix:
        return 0, (0, 0), (0, 0)
    
    row, col = len(matrix), len(matrix[0])
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
                # For Horizontal Line
                dpHorizontal[i][j] = dpHorizontal[i-1][j] + 1 if i > 0 else 1
                # For Vertical Line
                dpVertical[i][j] = dpVertical[i][j-1] + 1 if j > 0 else 1
                # For Diagonal Line
                dpDiagonal[i][j] = dpDiagonal[i-1][j-1] + 1 if i > 0 and j > 0 else 1
                # For Anti-Diagonal Line
                dpAntiDiagonal[i][j] = dpAntiDiagonal[i-1][j+1] + 1 if i > 0 and j < col-1 else 1
                
                # Update maximum length and its indices
                temp_maxLen = max(dpHorizontal[i][j], dpVertical[i][j], dpDiagonal[i][j], dpAntiDiagonal[i][j])
                if maxLen < temp_maxLen:
                    maxLen = temp_maxLen
                    if dpHorizontal[i][j] == maxLen:
                        start = (i - maxLen + 1, j)
                    elif dpVertical[i][j] == maxLen:
                        start = (i, j - maxLen + 1)
                    elif dpDiagonal[i][j] == maxLen:
                        start = (i - maxLen + 1, j - maxLen + 1)
                    else:
                        start = (i - maxLen + 1, j + maxLen - 1)
                    end = (i, j)
    
    return maxLen, start, end