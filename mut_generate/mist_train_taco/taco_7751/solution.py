"""
QUESTION:
For given n points in metric space, find the distance of the closest points.

Constraints

* 2 ≤ n ≤ 100,000
* -100 ≤ x, y ≤ 100

Input


n
x0 y0
x1 y1
:
xn-1 yn-1


The first integer n is the number of points.

In the following n lines, the coordinate of the i-th point is given by two real numbers xi and yi. Each value is a real number with at most 6 digits after the decimal point.

Output

Print the distance in a line. The output values should be in a decimal fraction with an error less than 0.000001.

Examples

Input

2
0.0 0.0
1.0 0.0


Output

1.000000


Input

3
0.0 0.0
2.0 0.0
1.0 1.0


Output

1.41421356237
"""

import sys
from operator import itemgetter
from itertools import permutations
from math import sqrt

def find_closest_points_distance(points: list) -> float:
    def solve(a: list):
        length = len(a)
        if length <= 3:
            return min((sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) for (p1, p2) in permutations(a, 2)))
        x_set_len = len(set((x for (x, _) in a)))
        axis = 0 if x_set_len > length / 2 else 1
        a.sort(key=itemgetter(axis))
        mid_index = length // 2
        (left, right) = (a[:mid_index], a[mid_index:])
        delta = min(solve(left), solve(right))
        median = a[mid_index][axis]
        m_a = []
        append = m_a.append
        for p in left[::-1]:
            if p[axis] < median - delta:
                break
            append(p)
        for p in right:
            if p[axis] > median + delta:
                break
            append(p)
        m_a.sort(key=itemgetter(not axis))
        for (i, p1) in enumerate(m_a):
            ub = p1[not axis] + delta
            for (j, p2) in enumerate(m_a[i + 1:]):
                if p2[not axis] > ub:
                    break
                dist = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                if dist < delta:
                    delta = dist
        return delta
    
    return solve(points)