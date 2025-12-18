"""
QUESTION:
Given an n x n binary matrix, implement a function `flipAndInvertImage` that flips the image horizontally, rotates it 90 degrees clockwise, and inverts it. The function should return the resulting image. The image is represented as a 2D list of 0s and 1s, where n is the number of rows (and columns) and 1 <= n <= 20.
"""

def flipAndInvertImage(image):
    flipped = [row[::-1] for row in image] # flip horizontally
    rotated = list(map(list, zip(*flipped[::-1]))) # rotate clockwise
    inverted = [[1 - pixel for pixel in row] for row in rotated] # invert
    return inverted