"""
QUESTION:
Create a function `processMatrix` that takes a two-dimensional matrix and a pattern as arguments. The function should transform the matrix into a one-dimensional list based on the specified pattern. The pattern can be one of the following: 
- 'row': elements are appended row-wise,
- 'zigzag': elements are appended in a zig-zag pattern from top left to bottom right,
- 'even': only even elements are appended, or
- 'column': elements are appended column-wise from right to left.
"""

def processMatrix(matrix, pattern):
    if pattern == 'row':
        return [item for sublist in matrix for item in sublist]

    elif pattern == 'zigzag':
        result = []
        for diagonal in range(len(matrix) * 2 - 1):
            if diagonal % 2 == 0:
                for i in range(max(0, diagonal - len(matrix) + 1), min(diagonal+1, len(matrix))):
                    result.append(matrix[i][diagonal-i])
            else:
                for i in range(max(0, diagonal - len(matrix) + 1), min(diagonal+1, len(matrix))):
                    result.append(matrix[diagonal-i][i])
        return result

    elif pattern == 'even':
        return [item for sublist in matrix for item in sublist if item % 2 == 0]

    elif pattern == 'column':
        transposed = zip(*matrix[::-1])
        return [item for sublist in transposed for item in sublist]