"""
QUESTION:
Develop a function named `identify_polygon` that takes a list of side lengths as input and returns the type of polygon based on the number of sides. The function should be able to identify polygons with 3 to 7 sides as 'Triangle', 'Quadrilateral', 'Pentagon', 'Hexagon', and 'Heptagon', respectively. For polygons with more than 7 sides, the function should return 'Polygon'.
"""

def identify_polygon(sides):
    if len(sides) == 3:
        return 'Triangle'
    elif len(sides) == 4:
        return 'Quadrilateral'
    elif len(sides) == 5:
        return 'Pentagon'
    elif len(sides) == 6:
        return 'Hexagon'
    elif len(sides) == 7:
        return 'Heptagon'
    else:
        return 'Polygon'