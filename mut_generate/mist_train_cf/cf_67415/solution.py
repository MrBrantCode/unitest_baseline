"""
QUESTION:
Write a function `spiralOrder3D(matrix3d)` that takes a 3D matrix as input, where each element is a 2D matrix. The function should return a one-dimensional array containing all the elements of the 3D matrix in spiral order. The input 3D matrix can be empty, have a single row or column, or contain negative numbers, and the function should handle these edge cases efficiently.
"""

def spiralOrder3D(matrix3d):
    def spiralOrder(matrix):
        result = []
        if len(matrix) == 0:
            return result
        
        rowBegin = 0
        rowEnd = len(matrix)-1
        colBegin = 0
        colEnd = len(matrix[0])-1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            
            for i in range(colBegin, colEnd+1):
                result.append(matrix[rowBegin][i])
            rowBegin += 1
            if rowBegin <= rowEnd:
                for i in range(rowBegin, rowEnd+1):
                    result.append(matrix[i][colEnd])
                colEnd -= 1
            if rowBegin <= rowEnd and colBegin <= colEnd:
                for i in range(colEnd, colBegin-1, -1):
                    result.append(matrix[rowEnd][i])
                rowEnd -= 1
            if rowBegin <= rowEnd and colBegin <= colEnd:
                for i in range(rowEnd, rowBegin-1, -1):
                    result.append(matrix[i][colBegin])
                colBegin += 1
        return result

    res = []
    for mat in matrix3d:
        res.extend(spiralOrder(mat))
    return res