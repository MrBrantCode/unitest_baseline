"""
QUESTION:
Write a function `findPeak(matrix)` that finds the peak in a 3D matrix. A peak is an element with all its neighbors less than or equal to it. The function should return the position of the peak as `(i, r, c)`, where `i` is the index of the 2D sub-matrix, `r` is the row index, and `c` is the column index. If no peak exists, return `(-1, -1, -1)`. Assume the input matrix is non-empty and all sub-matrices have the same dimensions.
"""

def findPeak(matrix):
    def getNeighbors(i, r, c):
        res = []
        if i > 0: res.append(matrix[i-1][r][c])
        if r > 0: res.append(matrix[i][r-1][c])
        if c > 0: res.append(matrix[i][r][c-1])
        if i < len(matrix)-1: res.append(matrix[i+1][r][c])
        if r < len(matrix[0])-1: res.append(matrix[i][r+1][c])
        if c < len(matrix[0][0])-1: res.append(matrix[i][r][c+1])
        return res

    l = 0
    r = len(matrix) - 1
    while(l != r):
        mid = (l + r) // 2
        max_val = maxR = maxC = float('-inf')
        for row in range(0, len(matrix[mid])):
            for col in range(0, len(matrix[mid][row])):
                if(matrix[mid][row][col] > max_val):
                    maxR = row
                    maxC = col
                    max_val = matrix[mid][row][col]

        left = min(getNeighbors(mid, maxR, maxC)[:3]) if mid > 0 else float('-inf')
        right = min(getNeighbors(mid, maxR, maxC)[3:]) if mid < len(matrix)-1 else float('inf')

        if(max_val < max(left,right)):
            if(left > right):
                r = mid - 1
            else:
                l = mid + 1 
        else:
            return (mid, maxR, maxC)
    return (-1, -1, -1)