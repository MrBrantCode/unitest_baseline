"""
QUESTION:
Write a function `max_submatrix_sum` that takes a 2D matrix as input and returns the maximum sum of a submatrix with an odd number of rows and an even number of columns. The function should not return the sum of a square matrix.
"""

def max_submatrix_sum(matrix):
    """
    This function calculates the maximum sum of a submatrix with an odd number of rows and an even number of columns.

    Args:
        matrix (list): A 2D list representing the matrix.

    Returns:
        int: The maximum sum of a submatrix with an odd number of rows and an even number of columns.
    """

    numRows = len(matrix)
    numCols = len(matrix[0])
    
    maxSum = float('-inf')
    
    # Iterate through each row
    for rowStart in range(numRows):
        for rowEnd in range(rowStart + 1, numRows):
            # Check if the number of rows is odd
            if (rowEnd - rowStart + 1) % 2 != 0:
                # Iterate through each column
                for colStart in range(numCols - 1):
                    for colEnd in range(colStart + 2, numCols + 1, 2):
                        # Initialize sum for the current submatrix
                        submatrix_sum = 0
                        
                        # Calculate the sum of the submatrix
                        for r in range(rowStart, (rowStart + rowEnd) // 2 + 1):
                            for c in range(colStart, colEnd):
                                submatrix_sum += matrix[r][c]
                                if r != rowEnd - r + rowStart:
                                    submatrix_sum += matrix[rowEnd - r + rowStart][c]
                        
                        # Update maxSum if the current submatrix sum is greater
                        maxSum = max(maxSum, submatrix_sum)
    
    return maxSum