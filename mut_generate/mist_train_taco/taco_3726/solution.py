"""
QUESTION:
There are n points marked on the plane. The points are situated in such a way that they form a regular polygon (marked points are its vertices, and they are numbered in counter-clockwise order). You can draw n - 1 segments, each connecting any two marked points, in such a way that all points have to be connected with each other (directly or indirectly).

But there are some restrictions. Firstly, some pairs of points cannot be connected directly and have to be connected undirectly. Secondly, the segments you draw must not intersect in any point apart from the marked points (that is, if any two segments intersect and their intersection is not a marked point, then the picture you have drawn is invalid).

How many ways are there to connect all vertices with n - 1 segments? Two ways are considered different iff there exist some pair of points such that a segment is drawn between them in the first way of connection, but it is not drawn between these points in the second one. Since the answer might be large, output it modulo 10^9 + 7.


-----Input-----

The first line contains one number n (3 ≤ n ≤ 500) — the number of marked points.

Then n lines follow, each containing n elements. a_{i}, j (j-th element of line i) is equal to 1 iff you can connect points i and j directly (otherwise a_{i}, j = 0). It is guaranteed that for any pair of points a_{i}, j = a_{j}, i, and for any point a_{i}, i = 0.


-----Output-----

Print the number of ways to connect points modulo 10^9 + 7.


-----Examples-----
Input
3
0 0 1
0 0 1
1 1 0

Output
1

Input
4
0 1 1 1
1 0 1 1
1 1 0 1
1 1 1 0

Output
12

Input
3
0 0 0
0 0 1
0 1 0

Output
0
"""

def count_ways_to_connect_vertices(n, edge):
    mod = 10 ** 9 + 7
    dp_f = [[-1] * n for _ in range(n)]
    dp_g = [[-1] * n for _ in range(n)]
    
    for i in range(n):
        dp_f[i][i] = dp_g[i][i] = 1
    
    for i in range(n - 1):
        dp_f[i][i + 1] = dp_g[i][i + 1] = 1 if edge[i][i + 1] else 0
    
    def f(l, r):
        if dp_f[l][r] != -1:
            return dp_f[l][r]
        dp_f[l][r] = g(l, r) if edge[l][r] else 0
        for m in range(l + 1, r):
            if edge[l][m]:
                dp_f[l][r] = (dp_f[l][r] + g(l, m) * f(m, r)) % mod
        return dp_f[l][r]
    
    def g(l, r):
        if dp_g[l][r] != -1:
            return dp_g[l][r]
        dp_g[l][r] = f(l + 1, r)
        for m in range(l + 1, r):
            dp_g[l][r] = (dp_g[l][r] + f(l, m) * f(m + 1, r)) % mod
        return dp_g[l][r]
    
    return f(0, n - 1)