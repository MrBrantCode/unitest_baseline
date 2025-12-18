"""
QUESTION:
For given two segments s1 and s2, print the coordinate of the cross point of them.

s1 is formed by end points p0 and p1, and s2 is formed by end points p2 and p3.

Constraints

* 1 ≤ q ≤ 1000
* -10000 ≤ xpi, ypi ≤ 10000
* p0 ≠ p1 and p2 ≠ p3.
* The given segments have a cross point and are not in parallel.

Input

The entire input looks like:


q (the number of queries)
1st query
2nd query
...
qth query


Each query consists of integer coordinates of end points of s1 and s2 in the following format:


xp0 yp0 xp1 yp1 xp2 yp2 xp3 yp3


Output

For each query, print the coordinate of the cross point. The output values should be in a decimal fraction with an error less than 0.00000001.

Example

Input

3
0 0 2 0 1 1 1 -1
0 0 1 1 0 1 1 0
0 0 1 1 1 0 0 1


Output

1.0000000000 0.0000000000
0.5000000000 0.5000000000
0.5000000000 0.5000000000
"""

def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def find_intersection_point(p0, p1, p2, p3):
    base = p3 - p2
    d1 = abs(cross(base, p0 - p2))
    d2 = abs(cross(base, p1 - p2))
    t = d1 / (d1 + d2)
    intersection = p0 + (p1 - p0) * t
    return (intersection.real, intersection.imag)