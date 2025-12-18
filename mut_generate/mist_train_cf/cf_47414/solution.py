"""
QUESTION:
Given a 3D integer matrix `matrix`, find a valley element (an element that is strictly smaller than its six neighbors: up, down, left, right, front, and back) and return its index. If the matrix contains multiple valleys, return the index to any of the valleys. Assume that `matrix[-1] = matrix[n] = ∞`. The matrix size is constrained to `1 <= matrix.length, matrix[i].length, matrix[i][j].length <= 1000`, and the elements are constrained to `-231 <= matrix[i][j][k] <= 231 - 1`.
"""

def find_valley(matrix):
    def getNeighbors(l, r, c):
        res = []
        if l > 0: res.append(matrix[l-1][r][c])
        if r > 0: res.append(matrix[l][r-1][c])
        if c > 0: res.append(matrix[l][r][c-1])
        if l < len(matrix)-1: res.append(matrix[l+1][r][c])
        if r < len(matrix[0])-1: res.append(matrix[l][r+1][c])
        if c < len(matrix[0][0])-1: res.append(matrix[l][r][c+1])
        
        return res

    def is_valley(l, r, c):
        minn = matrix[l][r][c]
        for v in getNeighbors(l, r, c):
            if v <= minn:
                return False
        return True

    for l in range(len(matrix)):
        for r in range(len(matrix[0])):
            for c in range(len(matrix[0][0])):
                if is_valley(l, r, c):
                    return [l, r, c]
    return None