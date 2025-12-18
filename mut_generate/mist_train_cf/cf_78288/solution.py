"""
QUESTION:
Write a function `find_valley(matrix)` that finds a prime valley element in a given 3D integer matrix `matrix`. A valley element is an element that is strictly smaller than its six neighbors (up, down, left, right, front, and back) and is a prime number. If the matrix contains multiple valleys, return the index to any of the valleys. If no such prime valley element is found, return `-1`. Assume that `matrix[-1] = matrix[n] = ∞` and all elements in the matrix are unique.

Constraints: `1 <= matrix.length, matrix[i].length, matrix[i][j].length <= 1000` and `-2^31 <= matrix[i][j][k] <= 2^31 - 1`.
"""

def find_valley(matrix):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    directions = [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                if is_prime(matrix[i][j][k]):
                    is_valley = True
                    for d in directions:
                        ni, nj, nk = i + d[0], j + d[1], k + d[2]
                        if ni >= 0 and nj >= 0 and nk >= 0 and ni < len(matrix) and nj < len(matrix[0]) and nk < len(matrix[0][0]) and matrix[ni][nj][nk] <= matrix[i][j][k]:
                            is_valley = False
                            break
                    if is_valley:
                        return (i, j, k)
    return -1