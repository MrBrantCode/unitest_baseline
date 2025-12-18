"""
QUESTION:
Write a function called `rank_points` that takes an origin point and a list of points as arguments. The origin and points should be lists of three integers representing coordinates in a 3D space. The function should return a list of tuples, where each tuple contains the Euclidean distance of a point from the origin and its coordinates. The list should be sorted in increasing order by distance. The function should handle exceptions and errors for non-integer inputs by returning a suitable error message.
"""

def rank_points(origin, points):
    if not (isinstance(origin, list) and len(origin) == 3 and all(isinstance(i, int) for i in origin)):
        return "Invalid origin. Origin must be a list of three integers."

    ranked_points = []
    for point in points:
        if not (isinstance(point, list) and len(point) == 3 and all(isinstance(i, int) for i in point)):
            return "Invalid point. All points must be a list of three integers."
        distance = ((point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2 + (point[2] - origin[2]) ** 2) ** 0.5
        ranked_points.append((distance, point))

    ranked_points.sort()
    return ranked_points