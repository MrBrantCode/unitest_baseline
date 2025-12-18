"""
QUESTION:
### The Problem

Consider a flat board with pegs sticking out of one side. If you stretched a rubber band across the outermost pegs what is the set of pegs such that all other pegs are contained within the shape formed by the rubber band?

![alt text](https://upload.wikimedia.org/wikipedia/commons/b/bc/ConvexHull.png)

More specifically, for this kata you will be given a list of points represented as ```[x,y]``` co-ordinates. Your aim will be to return a sublist containing points that form the perimeter of a polygon that encloses all other points contained within the original list.

### Notes:

The tests may include duplicate and/or co-linear points. Co-linear points are a set of points which fall on the same straight line. Neither should be included in your returned sublist

For simplicity, there will always be at least 3 points

### Help:

Check out wikipedia's page on [convex hulls](https://en.wikipedia.org/wiki/Convex_hull)

```if:python
Note for python users: `scipy` module has been disabled.
```
"""

def compute_convex_hull(points):
    """
    Computes the convex hull of a set of points using the Graham scan algorithm.

    Parameters:
    points (list of list of int/float): A list of points where each point is represented as [x, y].

    Returns:
    list of list of int/float: A sublist of points that form the perimeter of the convex hull.
    """
    def half_hull(sorted_points):
        hull = []
        for p in sorted_points:
            while len(hull) > 1 and (not is_ccw_turn(hull[-2], hull[-1], p)):
                hull.pop()
            hull.append(p)
        hull.pop()
        return hull

    def is_ccw_turn(p0, p1, p2):
        return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1]) > 0

    sorted_points = sorted(points)
    return half_hull(sorted_points) + half_hull(reversed(sorted_points))