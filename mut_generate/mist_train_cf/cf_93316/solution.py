"""
QUESTION:
Write a function `convert_pyramid` that takes a 2D list `pyramid` representing a pyramid of numbers as input. The function should return a single number which is the maximum sum of the numbers from top to bottom in the pyramid, where each step can only move either left or right one step. The function should not modify the original pyramid.
"""

def convert_pyramid(pyramid):
    new_pyramid = [row[:] for row in pyramid]
    for i in range(len(pyramid)-2, -1, -1):
        for j in range(i+1):
            new_pyramid[i][j] += max(new_pyramid[i+1][j], new_pyramid[i+1][j+1])
    return new_pyramid[0][0]