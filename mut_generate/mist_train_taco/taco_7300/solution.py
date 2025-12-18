"""
QUESTION:
Find articulation points of a given undirected graph G(V, E).

A vertex in an undirected graph is an articulation point (or cut vertex) iff removing it disconnects the graph.

Constraints

* 1 ≤ |V| ≤ 100,000
* 0 ≤ |E| ≤ 100,000
* The graph is connected
* There are no parallel edges
* There are no self-loops

Input


|V| |E|
s0 t0
s1 t1
:
s|E|-1 t|E|-1


, where |V| is the number of vertices and |E| is the number of edges in the graph. The graph vertices are named with the numbers 0, 1,..., |V|-1 respectively.

si and ti represent source and target verticess of i-th edge (undirected).

Output

A list of articulation points of the graph G ordered by name.

Examples

Input

4 4
0 1
0 2
1 2
2 3


Output

2


Input

5 4
0 1
1 2
2 3
3 4


Output

1
2
3
"""

def find_articulation_points(num_vertices, edges):
    # Initialize the graph adjacency list
    G = [[] for _ in range(num_vertices)]
    for s, t in edges:
        G[s].append(t)
        G[t].append(s)

    # Initialize variables for DFS
    used = [False] * num_vertices
    ord = [0] * num_vertices
    low = [float('inf')] * num_vertices
    is_articulation = [False] * num_vertices

    def dfs(v, prev, k):
        if used[v]:
            return k
        used[v] = True
        k += 1
        ord[v] = k
        low[v] = ord[v]
        cnt = 0
        for u in G[v]:
            if not used[u]:
                cnt += 1
                k = dfs(u, v, k)
                low[v] = min(low[v], low[u])
                if prev >= 0 and ord[v] <= low[u]:
                    is_articulation[v] = True
            elif u != prev:
                low[v] = min(low[v], ord[u])
        if prev == -1 and cnt >= 2:
            is_articulation[v] = True
        return k

    # Start DFS from vertex 0
    dfs(0, -1, 0)

    # Collect articulation points
    articulation_points = [i for i in range(num_vertices) if is_articulation[i]]
    return articulation_points