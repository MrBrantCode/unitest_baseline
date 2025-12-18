"""
QUESTION:
There is a chain consisting of multiple circles on a plane. The first (last) circle of the chain only intersects with the next (previous) circle, and each intermediate circle intersects only with the two neighboring circles.

Your task is to find the shortest path that satisfies the following conditions.

* The path connects the centers of the first circle and the last circle.
* The path is confined in the chain, that is, all the points on the path are located within or on at least one of the circles.

Figure E-1 shows an example of such a chain and the corresponding shortest path.

<image>

Figure E-1: An example chain and the corresponding shortest path


Input

The input consists of multiple datasets. Each dataset represents the shape of a chain in the following format.

> n
>  x1 y1 r1
>  x2 y2 r2
>  ...
>  xn yn rn
>

The first line of a dataset contains an integer n (3 ≤ n ≤ 100) representing the number of the circles. Each of the following n lines contains three integers separated by a single space. (xi, yi) and ri represent the center position and the radius of the i-th circle Ci. You can assume that 0 ≤ xi ≤ 1000, 0 ≤ yi ≤ 1000, and 1 ≤ ri ≤ 25.

You can assume that Ci and Ci+1 (1 ≤ i ≤ n−1) intersect at two separate points. When j ≥ i+2, Ci and Cj are apart and either of them does not contain the other. In addition, you can assume that any circle does not contain the center of any other circle.

The end of the input is indicated by a line containing a zero.

Figure E-1 corresponds to the first dataset of Sample Input below. Figure E-2 shows the shortest paths for the subsequent datasets of Sample Input.

<image>

Figure E-2: Example chains and the corresponding shortest paths


Output

For each dataset, output a single line containing the length of the shortest chain-confined path between the centers of the first circle and the last circle. The value should not have an error greater than 0.001. No extra characters should appear in the output.

Sample Input


10
802 0 10
814 0 4
820 1 4
826 1 4
832 3 5
838 5 5
845 7 3
849 10 3
853 14 4
857 18 3
3
0 0 5
8 0 5
8 8 5
3
0 0 5
7 3 6
16 0 5
9
0 3 5
8 0 8
19 2 8
23 14 6
23 21 6
23 28 6
19 40 8
8 42 8
0 39 5
11
0 0 5
8 0 5
18 8 10
8 16 5
0 16 5
0 24 5
3 32 5
10 32 5
17 28 8
27 25 3
30 18 5
0


Output for the Sample Input


58.953437
11.414214
16.0
61.874812
63.195179






Example

Input

10
802 0 10
814 0 4
820 1 4
826 1 4
832 3 5
838 5 5
845 7 3
849 10 3
853 14 4
857 18 3
3
0 0 5
8 0 5
8 8 5
3
0 0 5
7 3 6
16 0 5
9
0 3 5
8 0 8
19 2 8
23 14 6
23 21 6
23 28 6
19 40 8
8 42 8
0 39 5
11
0 0 5
8 0 5
18 8 10
8 16 5
0 16 5
0 24 5
3 32 5
10 32 5
17 28 8
27 25 3
30 18 5
0


Output

58.953437
11.414214
16.0
61.874812
63.195179
"""

from math import acos
from cmath import phase, rect, pi

def find_shortest_path_length(circles):
    n = len(circles)
    if n == 0:
        return 0
    
    P = []
    (x, y, r1) = circles[0]
    c1 = x + y * 1j
    P.append(c1)
    
    for i in range(1, n):
        (x, y, r2) = circles[i]
        c2 = x + y * 1j
        base = c2 - c1
        d = abs(base)
        a = acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
        t = phase(base)
        cp1 = c1 + rect(r1, t + a)
        cp2 = c1 + rect(r1, t - a)
        P.append(cp1)
        P.append(cp2)
        (c1, r1) = (c2, r2)
    
    lim = 5000
    dist = [lim] * (2 * n)
    dist[0] = 0
    goal = c1
    g_idx = 2 * n - 1
    
    indices = ((i + i % 2 + 1, i + i % 2 + 2) for i in range(g_idx))
    for (tpl_idx, cp, d) in zip(indices, P, dist):
        (j, k) = tpl_idx
        s1 = None
        s2 = None
        p_s1 = None
        p_s2 = None
        for (l, cp1, cp2) in zip(range(j, g_idx, 2), P[j::2], P[k::2]):
            t_s1 = cp1 - cp
            t_s2 = cp2 - cp
            if s1 is None or phase(s1 / t_s1) >= 0:
                s1 = t_s1
            if s2 is None or phase(s2 / t_s2) <= 0:
                s2 = t_s2
            if phase(s1 / s2) < 0:
                break
            if p_s1 != s1:
                dist[l] = min(dist[l], d + abs(s1))
                p_s1 = s1
            if p_s2 != s2:
                dist[l + 1] = min(dist[l + 1], d + abs(s2))
                p_s2 = s2
        else:
            gs = goal - cp
            if s1 is None and s2 is None or (phase(s1 / gs) >= 0 and phase(s2 / gs) <= 0):
                dist[g_idx] = min(dist[g_idx], d + abs(gs))
    
    return dist[g_idx]