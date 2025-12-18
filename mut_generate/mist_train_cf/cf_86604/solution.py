"""
QUESTION:
Compute the Manhattan distance between two points p1 and p2 in a 3D space. The function manhattan_distance should take two strings of the format 'x,y,z' where x, y, and z are decimal numbers and return the Manhattan distance rounded to two decimal places. The function should handle invalid input formats and return an error message.
"""

import math

def manhattan_distance(p1, p2):
    try:
        x1, y1, z1 = map(float, p1.split(','))
        x2, y2, z2 = map(float, p2.split(','))
        
        distance = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
        
        distance = round(distance, 2)
        
        return distance
    except ValueError:
        return 'Invalid input format. Please enter points as decimal numbers in the format x,y,z.'