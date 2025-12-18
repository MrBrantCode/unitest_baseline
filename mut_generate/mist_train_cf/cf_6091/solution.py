"""
QUESTION:
Design a function named `searchSortedMatrix` that takes as input a two-dimensional array `matrix` and a target `target` to search for in the matrix. The matrix is sorted both row-wise and column-wise in non-decreasing order, and may contain duplicate elements. The function should return `True` if the target is found in the matrix, and `False` otherwise. The function must have a time complexity of O(log n), where n is the total number of elements in the matrix.
"""

def searchSortedMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rowMin, rowMax = 0, len(matrix) - 1
    colMin, colMax = 0, len(matrix[0]) - 1
    
    while rowMin <= rowMax and colMin <= colMax:
        row = (rowMin + rowMax) // 2
        col = (colMin + colMax) // 2
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            rowMin = row + 1
        else:
            rowMax = row - 1

    return False