"""
QUESTION:
Given a pyramid of numbers, where each number can be positive or negative, and the pyramid has up to 100 rows, write a function `convert_pyramid` that finds the maximum sum from the top to the bottom of the pyramid. The function can only move downwards or diagonally to the left or right, and can only move to adjacent numbers on the row below. If the function moves to a number on the row below that is diagonally to the left or right, it must move to the number on the same side in the row below.
"""

def convert_pyramid(pyramid):
    for i in range(len(pyramid)-2, -1, -1):
        for j in range(i+1):
            pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])
    return pyramid[0][0]