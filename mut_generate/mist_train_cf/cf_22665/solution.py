"""
QUESTION:
Design a function `convert_pyramid(pyramid)` to find the maximum sum from the top to the bottom of a pyramid of numbers, where each number is either positive or negative, and the pyramid has up to 100 rows. The function should follow these rules: 
- Only move downwards or diagonally to the left or right.
- Only move to adjacent numbers on the row below.
- If moving to a number on the row below that is diagonally to the left or right, move to the number on the same side in the row below.
"""

def convert_pyramid(pyramid):
    for i in range(len(pyramid)-2, -1, -1):
        for j in range(i+1):
            pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])
    return pyramid[0][0]