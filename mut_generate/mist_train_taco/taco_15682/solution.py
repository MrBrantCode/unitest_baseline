"""
QUESTION:
Given is a tree with N vertices numbered 1 to N, and N-1 edges numbered 1 to N-1.
Edge i connects Vertex a_i and b_i bidirectionally and has a length of 1.
Snuke will paint each vertex white or black.
The niceness of a way of painting the graph is \max(X, Y), where X is the maximum among the distances between white vertices, and Y is the maximum among the distances between black vertices.
Here, if there is no vertex of one color, we consider the maximum among the distances between vertices of that color to be 0.
There are 2^N ways of painting the graph. Compute the sum of the nicenesses of all those ways, modulo (10^{9}+7).

-----Constraints-----
 - 2 \leq N \leq 2 \times 10^{5}
 - 1 \leq a_i, b_i \leq N
 - The given graph is a tree.

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 b_1
\vdots
a_{N-1} b_{N-1}

-----Output-----
Print the sum of the nicenesses of the ways of painting the graph, modulo (10^{9}+7).

-----Sample Input-----
2
1 2

-----Sample Output-----
2

 - If we paint Vertex 1 and 2 the same color, the niceness will be 1; if we paint them different colors, the niceness will be 0.
 - The sum of those nicenesses is 2.
"""

from collections import deque

def calculate_niceness_sum(N, edges):
    graph = [[] for _ in range(N + 1)]
    for (a, b) in edges:
        graph[a].append(b)
        graph[b].append(a)
    mod = 10 ** 9 + 7

    def bfs(x):
        q = deque([(0, x, 0)])
        dist = {x: 0}
        while q:
            (step, i, par) = q.popleft()
            dist[i] = step
            for j in graph[i]:
                if j == par:
                    continue
                q.append((step + 1, j, i))
        return [step, i, dist]

    (_, black, _) = bfs(1)
    (maxdist, white, b_dist) = bfs(black)
    (_, _, w_dist) = bfs(white)

    mindls = float('-inf')
    maxdls = [0] * N
    for i in range(1, N + 1):
        if i in (white, black):
            continue
        mindls = max(mindls, min(w_dist[i], b_dist[i]))
        maxdls[max(w_dist[i], b_dist[i])] += 1

    ans = pow(2, N - 1, mod) * maxdist % mod
    pre = 0
    for i in range(1, maxdist + 1):
        if i == maxdist and (not maxdls[i]):
            continue
        maxdls[i] += maxdls[i - 1]
        if mindls > i:
            continue
        ans += (pow(2, maxdls[i], mod) - pre) * i * 2
        ans %= mod
        pre = pow(2, maxdls[i], mod)

    return ans