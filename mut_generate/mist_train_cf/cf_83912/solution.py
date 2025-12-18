"""
QUESTION:
Write a function `findLonelyPixel` that takes an `m x n` 2D list `picture` consisting of characters 'B', 'W', and 'R', where 'B' and 'R' represent black and red pixels respectively, and 'W' represents a white pixel. Return the number of black lonely pixels and red lonely pixels. A black or red lonely pixel is a character 'B' or 'R' that located at a specific position where the same row and same column don't have any other black or red pixels respectively. The input constraints are `1 <= m, n <= 500` and `picture[i][j]` is 'W', 'B', or 'R'.
"""

from collections import Counter

def findLonelyPixel(picture):
    m, n = len(picture), len(picture[0])
    rows, cols = [0]*m, [0]*n

    for i in range(m):
        rows[i] = Counter(picture[i])
    for j in range(n):
        cols[j] = Counter(picture[i][j] for i in range(m))

    return sum(1 for i in range(m) for j in range(n) if picture[i][j] in ('B', 'R') and rows[i][picture[i][j]] == 1 and cols[j][picture[i][j]] == 1)