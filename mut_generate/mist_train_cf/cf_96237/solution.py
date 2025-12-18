"""
QUESTION:
Write a function called `fill_matrix_with_zeros` that fills a given matrix with zeros in a spiral pattern, starting from the top left corner and moving clockwise, without using any extra space or modifying the input matrix directly. The function should take a 2D list (matrix) as input and return the modified matrix. The function must run in constant time and space complexity.
"""

def fill_matrix_with_zeros(matrix):
    M = len(matrix)
    N = len(matrix[0])

    startRow = 0
    endRow = M - 1
    startCol = 0
    endCol = N - 1

    num = 1

    while startRow <= endRow and startCol <= endCol:
        # Fill top row
        for col in range(startCol, endCol + 1):
            matrix[startRow][col] = 0
            num += 1
        startRow += 1

        # Fill rightmost column
        for row in range(startRow, endRow + 1):
            matrix[row][endCol] = 0
            num += 1
        endCol -= 1

        # Fill bottom row
        if startRow <= endRow:
            for col in range(endCol, startCol - 1, -1):
                matrix[endRow][col] = 0
                num += 1
            endRow -= 1

        # Fill leftmost column
        if startCol <= endCol:
            for row in range(endRow, startRow - 1, -1):
                matrix[row][startCol] = 0
                num += 1
            startCol += 1

    return matrix