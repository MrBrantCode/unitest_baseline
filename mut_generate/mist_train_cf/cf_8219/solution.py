"""
QUESTION:
Write a function `convert_pyramid` that takes a 2D list `pyramid` as input, representing a pyramid of numbers where each number is either positive or negative. The pyramid may contain up to 100 rows. The function should return the maximum sum from the top to the bottom of the pyramid, following these rules:

- You can only move downwards or diagonally to the left or right.
- You can only move to adjacent numbers on the row below.
- If you move to a number on the row below that is diagonally to the left or right, you must move to the number on the same side in the row below.
"""

def convert_pyramid(pyramid):
    for i in range(len(pyramid)-2, -1, -1):
        for j in range(i+1):
            if j == 0:
                pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])
            elif j == i:
                pyramid[i][j] += max(pyramid[i+1][j-1], pyramid[i+1][j])
            else:
                pyramid[i][j] += max(pyramid[i+1][j-1], pyramid[i+1][j], pyramid[i+1][j+1])
    return pyramid[0][0]