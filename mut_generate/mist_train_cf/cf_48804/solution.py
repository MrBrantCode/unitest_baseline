"""
QUESTION:
Implement a function named `DDA` that takes four integers `x1`, `y1`, `x2`, and `y2` representing two points in a 2D plane. The function should return a list of coordinates (x, y) representing the pixels that make up the line from point `(x1, y1)` to `(x2, y2)` using the Digital Differential Analyzer (DDA) line drawing algorithm. The coordinates should be integers, so any floating-point values should be rounded to the nearest integer. The function should handle both horizontal and vertical lines, as well as lines with slopes between 0 and infinity.
"""

def DDA(x1, y1, x2, y2):
    """Returns a list of coordinates (x, y) representing the pixels that make up the line from point (x1, y1) to (x2, y2) using the Digital Differential Analyzer (DDA) line drawing algorithm."""
    
    dx = x2 - x1
    dy = y2 - y1
    
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
        
    xInc = dx / steps
    yInc = dy / steps

    x = x1
    y = y1
    
    coordinates = []
    
    for _ in range(steps + 1):  # Include the end point
        coordinates.append((round(x), round(y)))
        x += xInc
        y += yInc
 
    return coordinates