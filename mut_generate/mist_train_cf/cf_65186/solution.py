"""
QUESTION:
Write a function `findBlackPixel(picture, N)` that finds the number of black pixels located at some specific row R and column C in a given 2D char array `picture` consisting of 'B' and 'W' (black and white pixels respectively), that align with the following rules:
- Row R and column C both contain exactly N black pixels.
- For all columns that have a black pixel at row R, they should be exactly the same as column C.
The input `picture` is a 2D array with a size between 1x1 and 200x200, and N is a positive integer.
"""

def findBlackPixel(picture, N):
    m, n = len(picture), len(picture[0])

    rows = [0]*m
    cols = {}

    for r in range(m):
        count = 0
        for c in range(n):
            if picture[r][c] == 'B':
                count += 1
        if count == N:
            rows[r] = 1

    for c in range(n):
        col = ""
        for r in range(m):
            col += picture[r][c]
        if col.count('B') == N:
            cols[col] = cols.get(col, 0) + 1

    count = 0
    for r in range(m):
        if rows[r] == 1:
            for c in range(n):
                if picture[r][c] == 'B':
                    col = ""
                    for k in range(m):
                        col += picture[k][c]
                    count += cols.get(col, 0)

    return count