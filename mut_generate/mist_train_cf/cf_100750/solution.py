"""
QUESTION:
Create a function named "IsInPolygon" that takes two arguments: a tuple of two floats "point" representing the coordinates (x,y) of a point in a 2D plane, and a list of lists "polygon" where each sublist represents the coordinates of a vertex of a polygon with holes in a 2D plane. The function should return a boolean value indicating whether the point is inside the outer polygon and outside all the holes.
"""

def IsInPolygon(point, polygon):
    def is_inside(point, poly):
        count = 0
        for i in range(len(poly)):
            p1 = poly[i]
            p2 = poly[(i+1)%len(poly)]
            if ((p1[1] > point[1]) != (p2[1] > point[1])) and \
                (point[0] < (p2[0] - p1[0]) * (point[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]):
                count += 1
        return count % 2 != 0

    # Check if the point is inside the outer polygon
    if not is_inside(point, polygon[0]):
        return False
    
    # Check if the point is outside any of the holes
    for hole in polygon[1:]:
        if is_inside(point, hole):
            return False
            
    # The point is inside the polygon and outside all the holes
    return True