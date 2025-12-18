"""
QUESTION:
Given an array `rectangles` where `rectangles[i] = [xi, yi, ai, bi]` represents an axis-aligned rectangle with bottom-left point `(xi, yi)` and top-right point `(ai, bi)`, write a function `isRectangleCover(rectangles)` that returns `true` if all the rectangles together form an exact cover of a rectangular region, and the coordinates of the bottom-left and top-right points of the perfect rectangle. If the rectangles do not form a perfect rectangle, return an empty array. The rectangles may be rotated by a multiple of 90 degrees.

Constraints: 
1 <= rectangles.length <= 2 * 10^4
rectangles[i].length == 4
-10^5 <= xi, yi, ai, bi <= 10^5
"""

def isRectangleCover(rectangles):
    corners = set()
    area = 0
    xi, yi, ai, bi = float('inf'), float('inf'), float('-inf'), float('-inf')
    for x1, y1, x2, y2 in rectangles:
        xi, yi, ai, bi = min(xi,x1), min(yi,y1), max(ai,x2), max(bi,y2)
        area += (x2-x1)*(y2-y1)
        corners ^= {(x1,y1),(x1,y2),(x2,y1),(x2,y2)}
    if len(corners) != 4 or corners != {(xi,yi),(xi,bi),(ai,yi),(ai,bi)}:
        return []
    if area != (ai-xi)*(bi-yi):
        return []
    return [xi,yi,ai,bi]