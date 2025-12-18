"""
QUESTION:
Implement a function `min_rectangles(points)` that takes a list of unique points as input, where each point is a tuple of two integers representing the x and y coordinates. The function should return the minimum number of rectangles needed to cover all the points, where each rectangle is defined by its bottom-left and top-right coordinates.
"""

def min_rectangles(points):
    x_set = set()
    y_set = set()
    
    for x, y in points:
        x_set.add(x)
        y_set.add(y)
    
    return len(x_set) * len(y_set)