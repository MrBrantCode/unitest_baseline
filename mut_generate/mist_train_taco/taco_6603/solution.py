"""
QUESTION:
Let's say you have a bunch of points, and you want to round them all up and calculate the area of the smallest polygon containing all of the points (nevermind why, you just want a challenge). What you're looking for is the area of the *convex hull* of these points. Here is an example, delimited in blue :



## Your task

Implement a function that will compute the area covered by the convex hull that can be formed from an array of points, the area being rounded to two decimal places. The points are given as `(x,y)`, like in an orthonormal coordinates system.

```python
points = [(0, 0), (0, 3), (4, 0)]
convex_hull_area(points) == 6.00
```

*Note* : In Python, the scipy module has a [ready made solution](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html) for this. Of course, if you use it here, you are lame.

*P. S.* : If you enjoy this kata, you may also like this one, which asks you to compute a convex hull, without finding its area.
"""

import numpy as np

def slope(p1, p2):
    (dx, dy) = vectorize(p1, p2)
    return dy / dx if dx else float('inf')

def vectorize(p1, p2):
    return [b - a for (a, b) in zip(p1, p2)]

def getArea(p1, p2, p3):
    return np.cross(vectorize(p1, p2), vectorize(p1, p3)) / 2

def isConcave(p1, pivot, p2):
    return getArea(pivot, p1, p2) >= 0

def calculate_convex_hull_area(points):
    if len(points) < 3:
        return 0.0
    
    Z = min(points)
    q = sorted((pt for pt in points if pt != Z), key=lambda pt: (-slope(pt, Z), -np.linalg.norm(vectorize(Z, pt))))
    hull = [Z, q.pop()]
    
    while q:
        pt = q.pop()
        while len(hull) > 1 and isConcave(hull[-2], hull[-1], pt):
            hull.pop()
        hull.append(pt)
    
    area = sum((getArea(Z, hull[i], hull[i + 1]) for i in range(1, len(hull) - 1)))
    return round(area, 2)