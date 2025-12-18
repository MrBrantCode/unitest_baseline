"""
QUESTION:
For this kata, you are given three points ```(x1,y1,z1)```, ```(x2,y2,z2)```, and ```(x3,y3,z3)``` that lie on a straight line in 3-dimensional space.
You have to figure out which point lies in between the other two.

Your function should return 1, 2, or 3 to indicate which point is the in-between one.
"""

def find_middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    # Create tuples for each point with their respective indices
    points = [
        (x1, y1, z1, 1),
        (x2, y2, z2, 2),
        (x3, y3, z3, 3)
    ]
    
    # Sort the points based on their coordinates
    sorted_points = sorted(points)
    
    # Return the index of the middle point
    return sorted_points[1][3]