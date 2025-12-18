"""
QUESTION:
You are given a tree (an undirected connected acyclic graph) consisting of $n$ vertices and $n - 1$ edges. A number is written on each edge, each number is either $0$ (let's call such edges $0$-edges) or $1$ (those are $1$-edges).

Let's call an ordered pair of vertices $(x, y)$ ($x \ne y$) valid if, while traversing the simple path from $x$ to $y$, we never go through a $0$-edge after going through a $1$-edge. Your task is to calculate the number of valid pairs in the tree.


-----Input-----

The first line contains one integer $n$ ($2 \le n \le 200000$) — the number of vertices in the tree.

Then $n - 1$ lines follow, each denoting an edge of the tree. Each edge is represented by three integers $x_i$, $y_i$ and $c_i$ ($1 \le x_i, y_i \le n$, $0 \le c_i \le 1$, $x_i \ne y_i$) — the vertices connected by this edge and the number written on it, respectively.

It is guaranteed that the given edges form a tree.


-----Output-----

Print one integer — the number of valid pairs of vertices.


-----Example-----
Input
7
2 1 1
3 2 0
4 2 1
5 2 0
6 7 1
7 2 1

Output
34



-----Note-----

The picture corresponding to the first example:

[Image]
"""

from collections import deque

def bfs(source, graph, mark, fcount):
    visited = [source]
    q = deque()
    mark[source] = True
    q.append(source)
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not mark[v]:
                mark[v] = True
                visited.append(v)
                q.append(v)
    for u in visited:
        fcount[u] = len(visited)

def count_valid_pairs(n, edges):
    g = [[[] for _ in range(n)] for _ in range(2)]
    cnt = [[0 for _ in range(n)] for _ in range(2)]
    
    for u, v, c in edges:
        g[c][u - 1].append(v - 1)
        g[c][v - 1].append(u - 1)
    
    res = 0
    for link in range(2):
        mark = [False] * n
        for u in range(n):
            if not mark[u] and len(g[link][u]) > 0:
                bfs(u, g[link], mark, cnt[link])
                res += cnt[link][u] * (cnt[link][u] - 1)
    
    for i in range(n):
        if cnt[0][i] > 0 and cnt[1][i] > 1:
            res += (cnt[0][i] - 1) * (cnt[1][i] - 1)
    
    return res