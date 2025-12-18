"""
QUESTION:
Compute the number of triangles with all three vertices within the set $I_r$ that enclose the origin within their interior, where $I_r$ comprises of points $(x,y)$ with integer coordinates that lie within the confines of a circle with radius $r$, centered at the origin. The function `compute_triangles(r)` should calculate this quantity for a given radius `r`, subject to the condition that the coordinates of the points are integers.
"""

def compute_triangles(r):
    num_points = 2*r + 1
    return num_points**2