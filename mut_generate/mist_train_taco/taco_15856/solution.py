"""
QUESTION:
Given is a directed graph G with N vertices and M edges.

The vertices are numbered 1 to N, and the i-th edge is directed from Vertex A_i to Vertex B_i.

It is guaranteed that the graph contains no self-loops or multiple edges.
Determine whether there exists an induced subgraph (see Notes) of G such that the in-degree and out-degree of every vertex are both 1. If the answer is yes, show one such subgraph.

Here the null graph is not considered as a subgraph.

-----Notes-----
For a directed graph G = (V, E), we call a directed graph G' = (V', E') satisfying the following conditions an induced subgraph of G:
 - V' is a (non-empty) subset of V.
 - E' is the set of all the edges in E that have both endpoints in V'.

-----Constraints-----
 - 1 \leq N \leq 1000
 - 0 \leq M \leq 2000
 - 1 \leq A_i,B_i \leq N
 - A_i \neq B_i
 - All pairs (A_i, B_i) are distinct.
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N M
A_1 B_1
A_2 B_2
:
A_M B_M

-----Output-----
If there is no induced subgraph of G that satisfies the condition, print -1.
Otherwise, print an induced subgraph of G that satisfies the condition, in the following format:
K
v_1
v_2
:
v_K

This represents the induced subgraph of G with K vertices whose vertex set is \{v_1, v_2, \ldots, v_K\}. (The order of v_1, v_2, \ldots, v_K does not matter.)
If there are multiple subgraphs of G that satisfy the condition, printing any of them is accepted.

-----Sample Input-----
4 5
1 2
2 3
2 4
4 1
4 3

-----Sample Output-----
3
1
2
4

The induced subgraph of G whose vertex set is \{1, 2, 4\} has the edge set \{(1, 2), (2, 4), (4, 1)\}. The in-degree and out-degree of every vertex in this graph are both 1.
"""

from collections import deque

def find_shortest_cycle(G, s):
    dq = deque()
    N = len(G)
    INF = float('inf')
    dist = [INF] * N
    dist[s] = 0
    parent = [-1] * N
    ans_last = None
    dq.append(s)
    while dq and ans_last is None:
        v = dq.popleft()
        d = dist[v]
        for n in G[v]:
            if dist[n] == 0:
                ans_last = v
                parent[n] = v
                break
            elif dist[n] == INF:
                dist[n] = d + 1
                parent[n] = v
                dq.append(n)
    if ans_last:
        g = ans_last
        route = [g]
        while g != s:
            g = parent[g]
            route.append(g)
        return list(reversed(route))
    return None

def find_induced_subgraph(N, M, edges):
    G = [[] for _ in range(N + 1)]
    for a, b in edges:
        G[a].append(b)
    
    min_route = None
    for s in range(1, N + 1):
        route = find_shortest_cycle(G, s)
        if route:
            if min_route is None or len(route) < len(min_route):
                min_route = route
    
    if min_route:
        return len(min_route), min_route
    else:
        return -1