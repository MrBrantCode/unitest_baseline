"""
QUESTION:
Write a function named `rectangle_area` that takes a list of four tuples representing the coordinates of the corners of a rectangle on a 2D grid. The rectangle's sides are parallel to the axes of the grid and the coordinates are integers. If the points do not form a valid rectangle, assume they form a parallelogram and calculate its area, then return a message indicating the points do not form a valid rectangle. The function should return the calculated area or the message.
"""

def rectangle_area(corners):
    # Sort corners by x-coordinate first, then y-coordinate
    corners.sort(key=lambda x: (x[0], x[1]))

    # Check if points form a valid rectangle
    if not (corners[0][0] == corners[1][0] and corners[0][1] == corners[2][1] and
            corners[3][0] == corners[2][0] and corners[3][1] == corners[1][1]):
        return "Given points do not form a valid rectangle"

    # Calculate area of rectangle
    length = abs(corners[0][0] - corners[3][0])
    width = abs(corners[0][1] - corners[1][1])

    return length * width