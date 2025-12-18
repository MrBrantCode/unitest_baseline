"""
QUESTION:
Calculate the area of multiple rectangles with integer coordinates without overlapping. Given an array of rectangles where each rectangle contains exactly 4 values [x1, y1, x2, y2], (x1, y1) is the bottom left corner and (x2, y2) is the top right corner of a rectangle. The function should return the total covered area by all rectangles without counting overlaps multiple times. The rectangles may not be entirely contained within other rectangles. Write a function named `calculate_area` to solve this problem.
"""

def calculate_area(coordinates):
    points = set()

    for rectangle in coordinates:
        # Iterate over every x and y in the rectangle
        for x in range(rectangle[0], rectangle[2]):
            for y in range(rectangle[1], rectangle[3]):
                # Add every point of the rectangle to the set
                points.add((x, y))

    # Return the size of the set (i.e., the number of unique points)
    return len(points)