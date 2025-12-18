"""
QUESTION:
You are given $n$ segments on a Cartesian plane. Each segment's endpoints have integer coordinates. Segments can intersect with each other. No two segments lie on the same line.

Count the number of distinct points with integer coordinates, which are covered by at least one segment.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 1000$) — the number of segments.

Each of the next $n$ lines contains four integers $Ax_i, Ay_i, Bx_i, By_i$ ($-10^6 \le Ax_i, Ay_i, Bx_i, By_i \le 10^6$) — the coordinates of the endpoints $A$, $B$ ($A \ne B$) of the $i$-th segment.

It is guaranteed that no two segments lie on the same line.


-----Output-----

Print a single integer — the number of distinct points with integer coordinates, which are covered by at least one segment.


-----Examples-----
Input
9
0 0 4 4
-1 5 4 0
4 0 4 4
5 2 11 2
6 1 6 7
5 6 11 6
10 1 10 7
7 0 9 8
10 -1 11 -1

Output
42

Input
4
-1 2 1 2
-1 0 1 0
-1 0 0 3
0 3 1 0

Output
7



-----Note-----

The image for the first example: [Image] 

Several key points are marked blue, the answer contains some non-marked points as well.

The image for the second example: [Image]
"""

from math import gcd

def count_distinct_covered_points(segments):
    n = len(segments)
    pts = []
    ans = 0
    
    for i in range(n):
        (a, b, A, B) = segments[i]
        pts.append((a, b, A, B))
        ans += gcd(abs(a - A), abs(b - B)) + 1
    
    m = dict()
    
    for i in range(n):
        for j in range(i + 1, n):
            a1, b1, a2, b2 = pts[i]
            A1, B1, A2, B2 = pts[j]
            
            num1 = (b2 - B2) * (A2 - A1) * (a2 - a1) + A2 * (a2 - a1) * (B2 - B1) - a2 * (A2 - A1) * (b2 - b1)
            den1 = (B2 - B1) * (a2 - a1) - (b2 - b1) * (A2 - A1)
            
            if den1 != 0 and num1 % den1 == 0:
                if a1 == a2:
                    num2 = B2 * (A2 - A1) + (num1 // den1 - A2) * (B2 - B1)
                    den2 = A2 - A1
                    if num2 % den2 == 0:
                        if (num1 // den1 - A2) * (num1 // den1 - A1) <= 0 and (num2 // den2 - B2) * (num2 // den2 - B1) <= 0 and ((num1 // den1 - a2) * (num1 // den1 - a1) <= 0) and ((num2 // den2 - b2) * (num2 // den2 - b1) <= 0):
                            if (num1 // den1, num2 // den2) not in m:
                                m[num1 // den1, num2 // den2] = set()
                            m[num1 // den1, num2 // den2].add(i)
                            m[num1 // den1, num2 // den2].add(j)
                else:
                    num2 = b2 * (a2 - a1) + (num1 // den1 - a2) * (b2 - b1)
                    den2 = a2 - a1
                    if num2 % den2 == 0:
                        if (num1 // den1 - A2) * (num1 // den1 - A1) <= 0 and (num2 // den2 - B2) * (num2 // den2 - B1) <= 0 and ((num1 // den1 - a2) * (num1 // den1 - a1) <= 0) and ((num2 // den2 - b2) * (num2 // den2 - b1) <= 0):
                            if (num1 // den1, num2 // den2) not in m:
                                m[num1 // den1, num2 // den2] = set()
                            m[num1 // den1, num2 // den2].add(i)
                            m[num1 // den1, num2 // den2].add(j)
    
    sum_intersections = 0
    for intersections in m.values():
        sum_intersections += len(intersections) - 1
    
    return ans - sum_intersections