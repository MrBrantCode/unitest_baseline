"""
QUESTION:
Find the area of a rectangle when provided with one diagonal and one side of the rectangle. If the input diagonal is less than or equal to the length of the side, return "Not a rectangle". If the resultant area has decimals round it to two places.

`This kata is meant for beginners. Rank and upvote to bring it out of beta!`
"""

def calculate_rectangle_area(diagonal, side):
    if diagonal <= side:
        return "Not a rectangle"
    else:
        area = side * (diagonal ** 2 - side ** 2) ** 0.5
        return round(area, 2)