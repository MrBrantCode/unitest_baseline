"""
QUESTION:
Write a function `calculateDeterminant(matrix)` that calculates the determinant of a given square matrix using a recursive algorithm. The matrix is guaranteed to be a square matrix of size n x n, where n is a positive integer. The function should have a time complexity of O(n!) and a space complexity of O(n^2).
"""

def calculateDeterminant(matrix):
    n = len(matrix)
    
    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]
    
    det = 0
    
    for j in range(n):
        # Create sub-matrix by excluding first row and current column
        subMatrix = []
        for i in range(1, n):
            subMatrix.append(matrix[i][0:j] + matrix[i][j+1:])
        
        # Calculate sub-matrix determinant recursively
        subDet = calculateDeterminant(subMatrix)
        
        # Add/subtract current element multiplied by sub-matrix determinant
        det += ((-1) ** j) * matrix[0][j] * subDet
    
    return det