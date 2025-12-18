"""
QUESTION:
Create a function named "IsInPolygon" that takes two arguments: a tuple of two floats representing the coordinates of a point in a 2D plane, and a list of lists where each sublist represents the coordinates of a vertex of a polygon with holes in a 2D plane. The first sublist in the list represents the outer polygon, and the rest of the sublists represent the holes. The function should return a boolean value indicating whether the point is inside the outer polygon and outside all the holes.
"""

def IsInPolygon(point, polygon):
    outer_polygon = polygon[0]
    holes = polygon[1:]

    # Check if the point is inside the outer polygon
    count = 0
    for i in range(len(outer_polygon)):
        p1 = outer_polygon[i]
        p2 = outer_polygon[(i+1)%len(outer_polygon)]
        if ((p1[1] > point[1]) != (p2[1] > point[1])) and \
            (point[0] < (p2[0] - p1[0]) * (point[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]):
            count += 1
    if count % 2 == 0:
        return False
    
    # Check if the point is outside any of the holes
    for hole in holes:
        count = 0
        for i in range(len(hole)):
            p1 = hole[i]
            p2 = hole[(i+1)%len(hole)]
            if ((p1[1] > point[1]) != (p2[1] > point[1])) and \
                (point[0] < (p2[0] - p1[0]) * (point[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]):
                count += 1
        if count % 2 != 0:
            return False
            
    # The point is inside the polygon and outside all the holes
    return True