"""
QUESTION:
Given the function `maxPoints`, write a function to determine the highest count of points that are positioned on the same straight line. The function should take an array of points, where each point `points[i] = [xi, yi]` signifies a point on the Cartesian plane. The function should return the maximum count of points on the same line. 

The constraints are as follows:
- The length of `points` should be within the range of `1 <= points.length <= 300`.
- Each `points[i]` should have a length of 2.
- The values of `xi` and `yi` should fall within the range of `-10^4 <= xi, yi <= 10^4`.
- All the `points` in the array should be unique.
"""

import collections
import math

def maxPoints(points):
    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)

    if not points: 
        return 0
    n = len(points)
    res = 0
    for i in range(n):
        line_map = collections.defaultdict(int)
        duplicates = 1
        for j in range(i+1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            if dx == 0 and dy == 0:
                duplicates += 1
                continue
            gcd_val = gcd(dx, dy)
            dx //= gcd_val
            dy //= gcd_val
            line_map[(dx, dy)] += 1
        res = max(res, (max(line_map.values()) if line_map else 0) + duplicates)
    return res