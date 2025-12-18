"""
QUESTION:
Write a function called `find_extreme_points` that takes two parameters: 
- `image`: a NumPy array representing the input image
- `contour`: a list of points representing the contour in the image

The function should return a list of tuples, where each tuple contains the (x, y) coordinates of an extreme point of the contour (topmost, bottommost, leftmost, and rightmost points).
"""

import numpy as np

def find_extreme_points(image, contour):
    # Find the extreme points of the contour
    leftmost = tuple(contour[contour[:, 0].argmin()])
    rightmost = tuple(contour[contour[:, 0].argmax()])
    topmost = tuple(contour[contour[:, 1].argmin()])
    bottommost = tuple(contour[contour[:, 1].argmax()])
    
    extreme_points = [leftmost, rightmost, topmost, bottommost]
    
    return extreme_points