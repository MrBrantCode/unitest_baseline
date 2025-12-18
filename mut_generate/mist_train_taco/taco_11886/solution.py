"""
QUESTION:
You are given set of n points in 5-dimensional space. The points are labeled from 1 to n. No two points coincide.

We will call point a bad if there are different points b and c, not equal to a, from the given set such that angle between vectors <image> and <image> is acute (i.e. strictly less than <image>). Otherwise, the point is called good.

The angle between vectors <image> and <image> in 5-dimensional space is defined as <image>, where <image> is the scalar product and <image> is length of <image>.

Given the list of points, print the indices of the good points in ascending order.

Input

The first line of input contains a single integer n (1 ≤ n ≤ 103) — the number of points.

The next n lines of input contain five integers ai, bi, ci, di, ei (|ai|, |bi|, |ci|, |di|, |ei| ≤ 103) — the coordinates of the i-th point. All points are distinct.

Output

First, print a single integer k — the number of good points.

Then, print k integers, each on their own line — the indices of the good points in ascending order.

Examples

Input

6
0 0 0 0 0
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1


Output

1
1


Input

3
0 0 1 2 0
0 0 9 2 0
0 0 5 9 0


Output

0

Note

In the first sample, the first point forms exactly a <image> angle with all other pairs of points, so it is good.

In the second sample, along the cd plane, we can see the points look as follows:

<image>

We can see that all angles here are acute, so no points are good.
"""

def find_good_points(points):
    def dot_product(v1, v2):
        return sum(x * y for x, y in zip(v1, v2))
    
    def vector_length(v):
        return sum(x ** 2 for x in v) ** 0.5
    
    def is_acute_angle(v1, v2):
        return dot_product(v1, v2) > 0
    
    n = len(points)
    good_indices = []
    
    for k in range(n):
        is_good = True
        for i in range(n):
            for j in range(n):
                if i != k and j != k and i != j:
                    v1 = [points[i][d] - points[k][d] for d in range(5)]
                    v2 = [points[j][d] - points[k][d] for d in range(5)]
                    if is_acute_angle(v1, v2):
                        is_good = False
                        break
            if not is_good:
                break
        if is_good:
            good_indices.append(k + 1)
    
    return len(good_indices), good_indices