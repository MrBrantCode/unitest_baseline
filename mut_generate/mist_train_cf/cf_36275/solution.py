"""
QUESTION:
Write a function `longestWhitePixelSequence` that takes a 2D array of image data as input, where 0 represents a white pixel and 1 represents a black pixel, and returns the length of the longest contiguous sequence of white pixels. The function should iterate through each pixel in the 2D array.
"""

from typing import List

def longestWhitePixelSequence(image: List[List[int]]) -> int:
    max_length = 0
    current_length = 0

    for row in image:
        for pixel in row:
            if pixel == 0:  # white pixel
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0

    return max_length