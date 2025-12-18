"""
QUESTION:
Given a positive integer n, find the sum of the areas of all rectangles with integer coordinates and absolute value ≤ n that have a unique ellipse with smallest area outside the rectangle but touches its sides, where the foci of the ellipse are (√17, 0) and (-√17, 0).
"""

import math

def find_sum_of_areas(n):
    total = 0
    c = math.sqrt(17)
    for y1 in range(-n, n+1):
        x1 = math.sqrt(y1**2 + c**2)
        total += 2 * y1 * x1
    return int(total)