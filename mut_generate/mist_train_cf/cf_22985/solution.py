"""
QUESTION:
Write a function `manhattan_distance` that takes two parameters: a list of points (x, y) and an origin point. The function should return a list of Manhattan distances between the origin point and each point in the set. The Manhattan distance is calculated using the formula: |x2 - x1| + |y2 - y1|, where (x1, y1) is the origin point and (x2, y2) is each point in the set.
"""

def manhattan_distance(points, origin):
    """
    Calculate the Manhattan distance between the origin point and each point in the set.
    
    Parameters:
    points (list): A list of points (x, y).
    origin (tuple): The origin point (x, y).
    
    Returns:
    list: A list of Manhattan distances between the origin point and each point in the set.
    """
    return [abs(x - origin[0]) + abs(y - origin[1]) for x, y in points]