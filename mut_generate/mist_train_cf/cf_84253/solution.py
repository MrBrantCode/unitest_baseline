"""
QUESTION:
Given an n x n binary matrix image, write a function `flipAndInvertImage` that flips the image horizontally, rotates it 90 degrees clockwise, then inverts it, and returns the resulting image. The input image is a 2D list where each element is either 0 or 1, and 1 <= n <= 20. The function should take the image as input and return the modified image.
"""

def flipAndInvertImage(image):
    image = [i[::-1] for i in image] 
    image = [list(i) for i in zip(*image[::-1])]
    return [[1^i for i in inner] for inner in image]