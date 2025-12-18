"""
QUESTION:
Write a function `generateSpiralMatrix` that takes an integer `n` as input and returns an `n x n` matrix filled with consecutive numbers in a spiral pattern. The spiral pattern starts from the top-left corner and moves in the directions of right, down, left, and up, changing direction to the right whenever the next cell in the current direction is already filled or out of bounds.
"""

def generateSpiralMatrix(n):
    def dirToIndex(x, y, d):
        if d == "r":
            return (x, y + 1, "r") if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
        elif d == "d":
            return (x + 1, y, "d") if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
        elif d == "l":
            return (x, y - 1, "l") if y - 1 >= 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
        else:
            return (x - 1, y, "u") if x - 1 >= 0 and matrix[x - 1][y] == 0 else (x, y + 1, "r")

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num, dir, i, j = 1, "r", 0, 0
    while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
        matrix[i][j] = num
        num += 1
        i, j, dir = dirToIndex(i, j, dir)
    return matrix