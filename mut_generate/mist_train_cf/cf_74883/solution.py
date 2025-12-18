"""
QUESTION:
Create a function `maxNumEdgesToRemove` that takes two parameters: `n` and `edges`, where `n` is the number of nodes and `edges` is an array of arrays representing the edges in the graph. Each edge is represented as `[typei, ui, vi]`, where `typei` is the type of edge (1 for Alice-only, 2 for Bob-only, and 3 for both), and `ui` and `vi` are the nodes connected by the edge.

The function should return the maximum number of edges that can be removed while still ensuring the graph remains fully traversable by both Alice and Bob. If it is not possible to make the graph fully traversable, return `-1`.

Constraints:
- `1 <= n <= 10^5`
- `1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)`
- `edges[i].length == 3`
- `1 <= edges[i][0] <= 3`
- `1 <= edges[i][1] < edges[i][2] <= n`
- All tuples `(typei, ui, vi)` are distinct.
"""

def maxNumEdgesToRemove(n, edges):
    # Initialize union-find sets for Alice and Bob
    alice_parent = list(range(n + 1))
    bob_parent = list(range(n + 1))
    alice_redundant_edges = 0
    bob_redundant_edges = 0
    common_redundant_edges = 0

    # Function to find the parent of a node
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    # Function to union two nodes
    def union(parent, x, y):
        parent[find(parent, y)] = find(parent, x)

    # Process type 3 edges
    for edge in edges:
        if edge[0] == 3:
            u, v = edge[1:]
            if find(alice_parent, u) == find(alice_parent, v):
                common_redundant_edges += 1
            else:
                union(alice_parent, u, v)
                union(bob_parent, u, v)

    # Process type 1 and 2 edges
    for edge in edges:
        if edge[0] == 1:
            u, v = edge[1:]
            if find(alice_parent, u) == find(alice_parent, v):
                alice_redundant_edges += 1
            else:
                union(alice_parent, u, v)
        elif edge[0] == 2:
            u, v = edge[1:]
            if find(bob_parent, u) == find(bob_parent, v):
                bob_redundant_edges += 1
            else:
                union(bob_parent, u, v)

    # Check if the graph is fully traversable
    alice_components = len(set([find(alice_parent, i) for i in range(1, n + 1)]))
    bob_components = len(set([find(bob_parent, i) for i in range(1, n + 1)]))

    if alice_components > 1 or bob_components > 1:
        return -1
    else:
        return alice_redundant_edges + bob_redundant_edges + common_redundant_edges