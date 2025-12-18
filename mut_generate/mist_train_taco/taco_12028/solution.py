"""
QUESTION:
Nowadays all circuses in Berland have a round arena with diameter 13 meters, but in the past things were different.

In Ancient Berland arenas in circuses were shaped as a regular (equiangular) polygon, the size and the number of angles could vary from one circus to another. In each corner of the arena there was a special pillar, and the rope strung between the pillars marked the arena edges.

Recently the scientists from Berland have discovered the remains of the ancient circus arena. They found only three pillars, the others were destroyed by the time.

You are given the coordinates of these three pillars. Find out what is the smallest area that the arena could have.

Input

The input file consists of three lines, each of them contains a pair of numbers –– coordinates of the pillar. Any coordinate doesn't exceed 1000 by absolute value, and is given with at most six digits after decimal point.

Output

Output the smallest possible area of the ancient arena. This number should be accurate to at least 6 digits after the decimal point. It's guaranteed that the number of angles in the optimal polygon is not larger than 100.

Examples

Input

0.000000 0.000000
1.000000 1.000000
0.000000 1.000000


Output

1.00000000
"""

from math import acos, fmod, hypot, pi, sin

def gcd(x, y):
    if y < 0.001:
        return x
    else:
        return gcd(y, fmod(x, y))

def calculate_smallest_arena_area(p1, p2, p3):
    (x1, y1) = p1
    (x2, y2) = p2
    (x3, y3) = p3
    
    a = hypot(x1 - x2, y1 - y2)
    b = hypot(x1 - x3, y1 - y3)
    c = hypot(x2 - x3, y2 - y3)
    
    A = acos((b * b + c * c - a * a) / (2 * b * c))
    B = acos((c * c + a * a - b * b) / (2 * c * a))
    C = acos((a * a + b * b - c * c) / (2 * a * b))
    
    R = a / (2 * sin(A))
    u = 2 * gcd(A, gcd(B, C))
    
    return round(R * R * pi / u * sin(u), 7)