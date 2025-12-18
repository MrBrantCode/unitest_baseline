"""
QUESTION:
Given an undirected graph with V nodes and E edges. The task is to check if there is any cycle in undirected graph.
Note: Solve the problem using disjoint set union(dsu).
 
Example 1:
Input: 
Output: 1
Explanation: There is a cycle between 0->2->4->0
Example 2:
Input: 
Output: 0
Explanation: The graph doesn't contain any cycle
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function detectCycle() which takes number of vertices in the graph denoting as V and adjacency list denoting as adj and returns 1 if graph contains any cycle otherwise returns 0.
Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
 
Constraints:
1 ≤ V, E ≤ 10^{4}
"""

def detect_cycle_in_undirected_graph(V, adj):
    def find_parent(x, parent):
        if x == parent[x]:
            return x
        else:
            return find_parent(parent[x], parent)

    def compress(x, r, parent):
        if x == parent[x]:
            return x
        else:
            parent[x] = compress(parent[x], r, parent)
            return parent[x]

    def is_connected(x, y, parent):
        return find_parent(x, parent) == find_parent(y, parent)

    def union(x, y, parent, rank):
        x_par = find_parent(x, parent)
        y_par = find_parent(y, parent)
        if x_par == y_par:
            return 0
        if rank[x_par] >= rank[y_par]:
            parent[y_par] = x_par
            rank[x_par] += 1
        else:
            parent[x_par] = y_par
            rank[y_par] += 1
        return 1

    def list_to_edges(G):
        E = []
        for u in range(len(G)):
            for v in G[u]:
                E.append((u, v))
        return E

    if V < 3:
        return 0

    E = list_to_edges(adj)
    parent = [i for i in range(V)]
    rank = [0 for i in range(V)]

    for (u, v) in E:
        if is_connected(u, v, parent):
            return 1
        union(u, v, parent, rank)

    return 0