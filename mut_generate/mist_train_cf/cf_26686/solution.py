"""
QUESTION:
Write a function named `generate_magic_square` that takes an integer `n` as input and outputs a magic square of order `n`, where the sum of each row, column, and both main diagonals is the same. The function should not take any other input and should output the magic square directly.
"""

def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic_square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    return magic_square