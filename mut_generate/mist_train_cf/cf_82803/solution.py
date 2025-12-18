"""
QUESTION:
Develop a function `trilinear_interpolation` that performs multivariable linear interpolation between multiple given points in a 3D space. The function should take as input a 3D list `c` where the outermost list represents x-axis values, the mid-list represents y-axis values, and the innermost list represents z-axis values, all in the format of `[x0, x1], [y0, y1], [z0, z1]`. The function should also take three float values `x`, `y`, `z` as interpolation coordinates, which should be normalized if not in the range [0, 1]. The function should return the interpolation result.
"""

def lerp(a, b, t): 
    # helper function to linearly interpolate between a and b
    return a*(1-t) + b*t

def trilinear_interpolation(c, x, y, z):
    """
    Perform trilinear interpolation.
    
    Parameters:
    c (list(list(list))): Outermost list is for x-axis values, mid-list is for y-axis, innermost for z-axis.
                          Should be in [x0, x1], [y0, y1], [z0, z1] format. 
    x, y, z (float): interpolation coordinates. Should be normalized if not in [0, 1].
    
    Returns:
    result (float): interpolation result.
    """
    x0y0 = lerp(c[0][0][0], c[1][0][0], x)
    x1y0 = lerp(c[0][1][0], c[1][1][0], x)
    x0y1 = lerp(c[0][0][1], c[1][0][1], x)
    x1y1 = lerp(c[0][1][1], c[1][1][1], x)
    y0 = lerp(x0y0, x1y0, y)
    y1 = lerp(x0y1, x1y1, y)
    result = lerp(y0, y1, z)
    return(result)