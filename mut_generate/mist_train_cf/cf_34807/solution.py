"""
QUESTION:
Implement the function `total_length_of_line_segments(line_segments)` that takes a list of line segments as input, where each line segment is a list of two tuples representing the coordinates of the start and end points. The function should return the total length of all the line segments combined.
"""

import math

def total_length_of_line_segments(line_segments):
    total_length = 0
    for segment in line_segments:
        start_x, start_y = segment[0]
        end_x, end_y = segment[1]
        length = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)
        total_length += length
    return total_length