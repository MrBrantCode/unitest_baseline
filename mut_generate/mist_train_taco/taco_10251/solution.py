"""
QUESTION:
Suppose that P1 is an infinite-height prism whose axis is parallel to the z-axis, and P2 is also an infinite-height prism whose axis is parallel to the y-axis. P1 is defined by the polygon C1 which is the cross section of P1 and the xy-plane, and P2 is also defined by the polygon C2 which is the cross section of P2 and the xz-plane.

Figure I.1 shows two cross sections which appear as the first dataset in the sample input, and Figure I.2 shows the relationship between the prisms and their cross sections.

<image>


Figure I.1: Cross sections of Prisms

<image>


Figure I.2: Prisms and their cross sections

<image>


Figure I.3: Intersection of two prisms

Figure I.3 shows the intersection of two prisms in Figure I.2, namely, P1 and P2.

Write a program which calculates the volume of the intersection of two prisms.



Input

The input is a sequence of datasets. The number of datasets is less than 200.

Each dataset is formatted as follows.

m n
x11 y11
x12 y12
.
.
.
x1m y1m
x21 z21
x22 z22
.
.
.
x2n z2n


m and n are integers (3 ≤ m ≤ 100, 3 ≤ n ≤ 100) which represent the numbers of the vertices of the polygons, C1 and C2, respectively.

x1i, y1i, x2j and z2j are integers between -100 and 100, inclusive. (x1i, y1i) and (x2j , z2j) mean the i-th and j-th vertices' positions of C1 and C2 respectively.

The sequences of these vertex positions are given in the counterclockwise order either on the xy-plane or the xz-plane as in Figure I.1.

You may assume that all the polygons are convex, that is, all the interior angles of the polygons are less than 180 degrees. You may also assume that all the polygons are simple, that is, each polygon's boundary does not cross nor touch itself.

The end of the input is indicated by a line containing two zeros.

Output

For each dataset, output the volume of the intersection of the two prisms, P1 and P2, with a decimal representation in a line.

None of the output values may have an error greater than 0.001. The output should not contain any other extra characters.

Example

Input

4 3
7 2
3 3
0 2
3 1
4 2
0 1
8 1
4 4
30 2
30 12
2 12
2 2
15 2
30 8
13 14
2 8
8 5
13 5
21 7
21 9
18 15
11 15
6 10
6 8
8 5
10 12
5 9
15 6
20 10
18 12
3 3
5 5
10 3
10 10
20 8
10 15
10 8
4 4
-98 99
-99 -99
99 -98
99 97
-99 99
-98 -98
99 -99
96 99
0 0


Output

4.708333333333333
1680.0000000000005
491.1500000000007
0.0
7600258.4847715655
"""

def calculate_intersection_volume(M, N, P, Q):
    def calc(x):
        y_ma = -100
        y_mi = 100
        for i in range(M):
            (x0, y0) = P[i - 1]
            (x1, y1) = P[i]
            if x0 <= x <= x1 or x1 <= x <= x0:
                if x0 == x1:
                    y_ma = max(y_ma, max(y1, y0))
                    y_mi = min(y_mi, min(y1, y0))
                else:
                    y = (x - x0) * (y1 - y0) / (x1 - x0) + y0
                    y_ma = max(y_ma, y)
                    y_mi = min(y_mi, y)
        if not y_mi <= y_ma:
            return 0
        z_ma = -100
        z_mi = 100
        for i in range(N):
            (x0, z0) = Q[i - 1]
            (x1, z1) = Q[i]
            if x0 <= x <= x1 or x1 <= x <= x0:
                if x0 == x1:
                    z_ma = max(z_ma, max(z1, z0))
                    z_mi = min(z_mi, min(z1, z0))
                else:
                    z = (x - x0) * (z1 - z0) / (x1 - x0) + z0
                    z_ma = max(z_ma, z)
                    z_mi = min(z_mi, z)
        if not z_mi <= z_ma:
            return 0
        return (z_ma - z_mi) * (y_ma - y_mi)

    xs = set()
    xs.update((x for (x, y) in P))
    xs.update((x for (x, z) in Q))
    X = sorted(xs)

    ans = 0
    L = len(X)
    for i in range(L - 1):
        x0 = X[i]
        x1 = X[i + 1]
        s0 = calc(x0)
        s1 = calc((x0 + x1) / 2)
        s2 = calc(x1)
        if s1 > 0:
            ans += (x1 - x0) * (s0 + s2 + 4 * s1) / 6

    return ans