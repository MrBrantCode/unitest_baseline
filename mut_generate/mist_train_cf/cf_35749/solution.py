"""
QUESTION:
Write a function `count_logo_pixels` that takes a 2D array of characters as input where each character represents a color ('N' for navy, 'G' for green, and 'R' for red) and returns the count of non-navy ('G' and 'R') pixels. The input array represents an 8x8 grid of pixels.
"""

from typing import List

def count_logo_pixels(logo: List[List[str]]) -> int:
    count = 0
    for row in logo:
        for pixel in row:
            if pixel != 'N':
                count += 1
    return count