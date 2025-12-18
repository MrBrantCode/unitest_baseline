"""
QUESTION:
We are given a sequence of coplanar points and see all the possible triangles that may be generated which all combinations of three points.

We have the following list of points with the cartesian coordinates of each one:
```
Points [x, y]
   A   [1, 2]
   B   [3, 3]
   C   [4, 1]
   D   [1, 1]
   E   [4, -1]
```
With these points we may have the following triangles: ```ABC, ABD, ABE, ACD, ACE, ADE, BCD, BCE, BDE, CDE.``` There are three special ones: ```ABC, ACD and CDE```, that have an angle of 90°. All is shown in the picture below:



We need to count all the rectangle triangles that may be formed by a given list of points.

The case decribed above will be:
```python
count_rect_triang([[1, 2],[3, 3],[4, 1],[1, 1],[4, -1]]) == 3
```

Observe this case:
```python
count_rect_triang([[1, 2],[4, -1],[3, 3],[4, -1],[4, 1],[1, 1],[4, -1], [4, -1], [3, 3], [1, 2]]) == 3
```
If no rectangle triangles may be generated the function will output ```0```.

Enjoy it!
"""

from itertools import combinations

def is_right_triangle(a, b, c):
    # Calculate the squared distances between the points
    distances = sorted([
        (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2,
        (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2,
        (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2
    ])
    # Check if the sum of the squares of the two shorter sides equals the square of the longest side
    return distances[0] + distances[1] == distances[2]

def count_right_triangles(points):
    # Use combinations to generate all possible sets of three points
    right_triangle_count = 0
    for triangle in combinations(points, 3):
        if is_right_triangle(*triangle):
            right_triangle_count += 1
    return right_triangle_count