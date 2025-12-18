"""
QUESTION:
Given a list of points in the plane, implement the function `make_circle` that returns the radius of the smallest circle that can enclose all the points. The input list `points` will contain 3 to 50 points with no duplicates, where each point's coordinates are integers between -50 and 50. The output should be accurate within 10^-6 of the true value.
"""

from math import sqrt

def make_circle(points):
    # Convert to float and find bounding box.
    converted = [(float(x), float(y)) for x, y in points]
    minimal_x = min(x for x, y in converted)
    maximal_x = max(x for x, y in converted)
    minimal_y = min(y for x, y in converted)
    maximal_y = max(y for x, y in converted)

    # Start with the midpoint of bounding box. Add one third of bounding box size to radius.
    center_x = minimal_x + (maximal_x - minimal_x) / 2.0
    center_y = minimal_y + (maximal_y - minimal_y) / 2.0
    radius = max(max(abs(x - center_x), abs(y - center_y)) for (x, y) in converted)
    radius *= 1.0 + 1.0/3.0

    # Make multiple passes to improve the result.
    for _ in range(3):
        average_x = sum(x for x, y in converted if sqrt((x - center_x)**2 + (y - center_y)**2) <= radius) / len(converted)
        average_y = sum(y for x, y in converted if sqrt((x - center_x)**2 + (y - center_y)**2) <= radius) / len(converted)
        radius = max(sqrt((x - average_x)**2 + (y - average_y)**2) for (x, y) in converted)
        center_x, center_y = average_x, average_y
    
    return radius