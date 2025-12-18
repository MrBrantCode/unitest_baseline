"""
QUESTION:
Ikta has an extraordinary feeling for undirected graphs. Ikta likes the undirected graph G and its two-point s, t pair (G, s, t) that has the greatest "beauty". The "beauty" of a pair (G, s, t) is the edge e = \\ {u, v \\} (u and v are two different points of G), and the shortest path from s to t in G. Is the number of things whose length is greater than the length of the shortest path from s to t in the undirected graph with g plus e.

Your job is to write a program that seeks its "beauty" given a pair (G, s, t).



Input

The input is given in the following format.

> N M s t
> x1 y1
> ...
> xi yi
> ...
> xM yM
>

First, the number of vertices, the number of edges, and the integers N, M, s, t representing the two vertices of the undirected graph are input. From the 2nd line to the M + 1th line, two vertices connected by edges are input. (However, let the set of G vertices be \\ {1, ..., N \\}.)

Constraints

Each variable being input satisfies the following constraints.

* 2 ≤ N ≤ 100,000
* 1 ≤ M ≤ 300,000
* 1 ≤ s, t, xi, yi ≤ N
* Different from s and t
* Guaranteed to reach t from s

Output

When the given graph is G, output the "beauty" of the set (G, s, t) in one line.

Examples

Input

3 2 1 3
1 2
2 3


Output

1


Input

9 8 7 8
2 6
4 9
8 6
9 2
3 8
1 8
8 5
7 9


Output

7


Input

4 3 1 4
1 2
3 4
4 1


Output

0


Input

9 7 8 9
9 6
6 5
3 6
3 7
2 5
8 5
1 4


Output

2
"""

from collections import deque, defaultdict

def calculate_beauty(n, m, s, t, edges):
    s -= 1
    t -= 1
    adjacency_list = [[] for _ in range(n)]
    for (x, y) in edges:
        x -= 1
        y -= 1
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    def dist_from(start):
        INF = 10 ** 20
        dist = [INF] * n
        dist[start] = 0
        que = deque()
        que.append((0, start))
        while que:
            (score, node) = que.popleft()
            for to in adjacency_list[node]:
                if dist[to] > score + 1:
                    dist[to] = score + 1
                    que.append((score + 1, to))
        return dist

    dist_from_s = dist_from(s)
    dic1 = defaultdict(set)
    for (i, d) in enumerate(dist_from_s):
        dic1[d].add(i)

    dist_from_t = dist_from(t)
    dic2 = defaultdict(set)
    for (i, d) in enumerate(dist_from_t):
        dic2[d].add(i)

    st_dist = dist_from_s[t]
    ans = 0
    for key in dic1:
        another_key = st_dist - key - 2
        if another_key in dic2:
            add = len(dic1[key]) * len(dic2[another_key])
            for u in dic1[key]:
                for to in adjacency_list[u]:
                    if to in dic2[another_key]:
                        add -= 1
            ans += add

    return ans