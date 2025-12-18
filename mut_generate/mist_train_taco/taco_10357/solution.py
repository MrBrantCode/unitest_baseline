"""
QUESTION:
You have the `radius` of a circle with the center in point `(0,0)`.

Write a function that calculates the number of points in the circle where `(x,y)` - the cartesian coordinates of the points - are `integers`.

Example: for `radius = 2` the result should be `13`.

`0 <= radius <= 1000`

![](http://i.imgur.com/1SMov3s.png)
"""

def count_integer_points_in_circle(radius: int) -> int:
    from math import sqrt
    
    if radius < 0:
        raise ValueError("Radius must be a non-negative integer.")
    
    count = sum(int(sqrt(radius * radius - x * x)) for x in range(0, radius + 1)) * 4 + 1
    return count