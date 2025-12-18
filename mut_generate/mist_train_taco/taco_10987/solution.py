"""
QUESTION:
Dasha decided to have a rest after solving the problem. She had been ready to start her favourite activity — origami, but remembered the puzzle that she could not solve.  [Image] 

The tree is a non-oriented connected graph without cycles. In particular, there always are n - 1 edges in a tree with n vertices.

The puzzle is to position the vertices at the points of the Cartesian plane with integral coordinates, so that the segments between the vertices connected by edges are parallel to the coordinate axes. Also, the intersection of segments is allowed only at their ends. Distinct vertices should be placed at different points. 

Help Dasha to find any suitable way to position the tree vertices on the plane.

It is guaranteed that if it is possible to position the tree vertices on the plane without violating the condition which is given above, then you can do it by using points with integral coordinates which don't exceed 10^18 in absolute value.


-----Input-----

The first line contains single integer n (1 ≤ n ≤ 30) — the number of vertices in the tree. 

Each of next n - 1 lines contains two integers u_{i}, v_{i} (1 ≤ u_{i}, v_{i} ≤ n) that mean that the i-th edge of the tree connects vertices u_{i} and v_{i}.

It is guaranteed that the described graph is a tree.


-----Output-----

If the puzzle doesn't have a solution then in the only line print "NO".

Otherwise, the first line should contain "YES". The next n lines should contain the pair of integers x_{i}, y_{i} (|x_{i}|, |y_{i}| ≤ 10^18) — the coordinates of the point which corresponds to the i-th vertex of the tree.

If there are several solutions, print any of them. 


-----Examples-----
Input
7
1 2
1 3
2 4
2 5
3 6
3 7
Output
YES
0 0
1 0
0 1
2 0
1 -1
-1 1
0 2
Input
6
1 2
2 3
2 4
2 5
2 6

Output
NO

Input
4
1 2
2 3
3 4
Output
YES
3 3
4 3
5 3
6 3


-----Note-----

In the first sample one of the possible positions of tree is: [Image]
"""

def position_tree_vertices(n, edges):
    def dfs(v, x, y, t, l, pr):
        ans[v] = (x, y)
        p = [(0, 1, 3), (0, 1, 2), (1, 2, 3), (0, 2, 3)][t]
        g[v] = [u for u in g[v] if u != pr]
        for i in range(min(len(p), len(g[v]))):
            newx = x + nx[p[i]][0] * l
            newy = y + nx[p[i]][1] * l
            dfs(g[v][i], newx, newy, p[i], l // 4, v)

    g = [list() for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    root = 1
    for i in range(1, n + 1):
        if len(g[i]) > 4:
            return ("NO",)

    ans = [0] * (n + 1)
    ans[root] = (0, 0)
    inf = 10 ** 18
    l = inf // 4
    nx = ((1, 0), (0, -1), (-1, 0), (0, 1))

    for i in range(len(g[root])):
        dfs(g[root][i], nx[i][0] * l, nx[i][1] * l, i, l // 4, root)

    return ("YES", ans[1:])