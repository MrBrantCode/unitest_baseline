"""
QUESTION:
Given a 4D matrix where each sub-matrix is a 2D array of the same size, write a function `spiralTraverse4D` that traverses the 4D matrix in a spiral (helical) order across all dimensions. The function should be able to handle any size of 4D matrix as long as each 2D sub-matrix is of the same size.
"""

def spiralTraverse4D(matrix, index=0):
    if index == len(matrix):
        return []
    # Traverse Layers
    result = []
    for i in matrix[index]:
        # Traverse individual 2D Matrix
        result += spiralTraverse2D(i)
    result += spiralTraverse4D(matrix, index=index+1)
    return result

def spiralTraverse2D(matrix):
    res = []
    while matrix:
        # Traverse Right
        for x in matrix.pop(0):
            res.append(x)
        if matrix and matrix[0]:
            # Traverse Down
            for row in matrix:
                res.append(row.pop())
        if matrix:
            # Traverse Left
            for x in matrix.pop()[::-1]:
                res.append(x)
        if matrix and matrix[0]:
            # Traverse Up
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res