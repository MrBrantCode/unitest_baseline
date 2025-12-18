"""
QUESTION:
Given a pyramid of up to 100 rows, where each number is either positive or negative, find the maximum sum from the top to the bottom. The movement is restricted to downwards or diagonally to the left or right to adjacent numbers on the row below, with the additional rule that if moving diagonally, you must move to the number on the same side in the row below. Implement the function `convert_pyramid(pyramid)` to calculate this maximum sum, where the input `pyramid` is a list of lists representing the pyramid.
"""

def entrance(pyramid):
    for i in range(len(pyramid)-2, -1, -1):
        for j in range(i+1):
            if pyramid[i+1][j] > pyramid[i+1][j+1]:
                pyramid[i][j] += pyramid[i+1][j]
            else:
                pyramid[i][j] += pyramid[i+1][j+1]
    return pyramid[0][0]