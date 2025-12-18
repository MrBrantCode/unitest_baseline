"""
QUESTION:
Write a function `process_image` that takes in two parameters: a 2D list of integers `im` representing an image matrix, and an integer `orientation` representing the orientation for processing (0 for lines, 1 for columns). The function should invert the pixel values in the image matrix by subtracting them from 255, then return a list containing the sum of pixel values along the specified orientation.
"""

def process_image(im, orientation):
    im = [[255 - pixel for pixel in row] for row in im]  # Invert pixel values
    if orientation == 1:
        return [sum(column) for column in zip(*im)]  # Sum along columns
    else:
        return [sum(row) for row in im]  # Sum along lines