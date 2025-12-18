"""
QUESTION:
For a new 3D game that will be released, a team of programmers needs an easy function. (Then it will be processed as a method in a Class, forget this concept for Ruby)

We have an sphere with center O, having in the space the coordinates `[α, β, γ]` and radius `r`  and a list of points, `points_list`, each one with coordinates `[x, y, z]`. Select the biggest triangle (or triangles) that has (have) all its (their) 3 vertice(s) as interior points of the sphere (not even in the sphere contour). You should consider that a point P is interior if its distance to center O, d, is such that:


d < r

and 

(d - r) / r| > 10^(-10)


Let's see the situation with the following points in the image posted below:
```python
A = [1,2,-4]; B = [-3, 2, 4]; C = [7, 8, -4]; D = [2, 3, 5]; E = [-2, -1, 1]
```

The sphere has the following features:
```
O = [1, 2, -2] (Center of the sphere)
radius = 8
```



As C is the only exterior point of the sphere, the possible triangles that have their vertices interior to the sphere are: 

```
ABD, ABE, ADE, BDE
```

Let's see which is the biggest one:

```python
Triangle    Triangle with its points         Area
ABD        [[1,2,-4],[-3,2,4],[2,3,5]]    22.44994432064
ABE        [[1,2,-4],[-3,2,4],[-2,-1,1]]  13.56465996625
ADE        [[1,2,-4],[2,3,5],[-2,-1,1]]   22.62741699796 <---- biggest triangle
BDE        [[-3,2,4],[2,3,5],[-2,-1,1]]   11.31370849898
```

Our function ```biggest_triang_int()``` (javascript: ```biggestTriangInt()```should output for this case:

```python
points_list = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1]]
sphere_center = [1, 2, -2]
radius = 8
biggest_triang_int(points_list, sphere_center, radius) == [4, 22.62741699796,  [[1,2,-4],[2,3,5],[-2,-1,1]]]
```

That means that with the given points list we may generate 4 triangles with all their vertices as interior points of the sphere, the biggest triangle has an area of 22.62741699796 (the units does not matter and the values for the area should not be rounded) and finally, there is only one triangle with this maximum value.
Every triangle should be output having the same order of its vertices than in the given list of points. B = [-3,2,4], comes before than D =[2,3,5] and the last one E = [-2,-1,1]
If in the result we have only one triangle, the function should output a list of three points.

Let'see the next case:

```python
points_list = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1],
              [3, 2, 6], [1, 4, 0], [-4, -5, -6], [4, 5, 6], [-2, -3, -5],
              [-1, -2, 4], [-3, -2, -6], [-1, -4, 0], [2, 1, -1]]
sphere_center = [0, 0, 0]
radius = 8
biggest_triang_int(points_list, sphere_center, radius) == [165, 33.645207682521445, [[[1, 2, -4], [3, 2, 6], [-1, -4, 0]], [[1, 4, 0], [-1, -2, 4], [-3, -2, -6]]]]
```

Now there are a total of 165 triangles with their vertices in the sphere, the biggest triangle has an area of 33.645207682521445 but we have two triangles with this area value. The vertices of each triangle respect the order of the points list as we expressed before but the additional detail is that the triangles are sorted by the values of the coordinates of their points. Let's compare the coordinates of the first point

```
First point   x  y  z
Triangle1     1  2 -4  <--- this triangle is first in the result
Triangle2     1  4  0
              |  |
              |  y1 < y2 (2, 4)
              |
              x1 = x2     (1 = 1)
```

In the case that all the given points are exterior to the sphere the function should output the empty list.

The points in the list are all valid and each one occurs once.

Remember that if three points are collinear do not form a triangle. For practical purposes you may consider that if the area of a triangle is lower than 10^(-8), the points are aligned.

Enjoy it!
"""

from collections import defaultdict
from itertools import combinations

def norme(vect):
    return sum((v ** 2 for v in vect)) ** 0.5

def vectorize(pt1, pt2):
    return [b - a for (a, b) in zip(pt1, pt2)]

def isInCircle(d, r):
    return d < r and (r - d) / r > 1e-10

def crossProd(v1, v2):
    return [v1[0] * v2[1] - v1[1] * v2[0], v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2]]

def find_largest_interior_triangles(points_list, sphere_center, radius):
    filteredPts = [pt for pt in points_list if isInCircle(norme(vectorize(pt, sphere_center)), radius)]
    dctTriangles = defaultdict(list)
    
    for threePts in combinations(filteredPts, 3):
        area = abs(norme(crossProd(vectorize(*threePts[:2]), vectorize(*threePts[1:]))) / 2.0)
        if area > 1e-08:
            dctTriangles[area].append(list(threePts))
    
    if not dctTriangles:
        return []
    
    maxArea = max(dctTriangles.keys())
    largestTriangles = sorted(dctTriangles[maxArea])
    
    return [sum(map(len, dctTriangles.values())), maxArea, largestTriangles if len(largestTriangles) > 1 else largestTriangles[0]]