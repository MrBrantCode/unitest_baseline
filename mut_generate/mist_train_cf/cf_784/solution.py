"""
QUESTION:
Write a function `manhattan_distance(p1, p2)` to calculate the Manhattan distance between two points p1 and p2 in a 3D space. The function should accept the points as strings in the format 'x,y,z' where x, y, and z are decimal numbers. It should return the Manhattan distance rounded to two decimal places. If the input is not in the correct format, the function should return 'Invalid input format. Please enter points as decimal numbers in the format x,y,z.'
"""

def manhattan_distance(p1, p2):
    try:
        x1, y1, z1 = map(float, p1.split(','))
        x2, y2, z2 = map(float, p2.split(','))
        distance = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
        distance = round(distance, 2)
        return distance
    except ValueError:
        return 'Invalid input format. Please enter points as decimal numbers in the format x,y,z.'