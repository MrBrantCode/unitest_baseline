"""
QUESTION:
Connected undirected graph without cycles is called a tree. Trees is a class of graphs which is interesting not only for people, but for ants too.

An ant stands at the root of some tree. He sees that there are n vertexes in the tree, and they are connected by n - 1 edges so that there is a path between any pair of vertexes. A leaf is a distinct from root vertex, which is connected with exactly one other vertex.

The ant wants to visit every vertex in the tree and return to the root, passing every edge twice. In addition, he wants to visit the leaves in a specific order. You are to find some possible route of the ant.

Input

The first line contains integer n (3 ≤ n ≤ 300) — amount of vertexes in the tree. Next n - 1 lines describe edges. Each edge is described with two integers — indexes of vertexes which it connects. Each edge can be passed in any direction. Vertexes are numbered starting from 1. The root of the tree has number 1. The last line contains k integers, where k is amount of leaves in the tree. These numbers describe the order in which the leaves should be visited. It is guaranteed that each leaf appears in this order exactly once.

Output

If the required route doesn't exist, output -1. Otherwise, output 2n - 1 numbers, describing the route. Every time the ant comes to a vertex, output it's index.

Examples

Input

3
1 2
2 3
3


Output

1 2 3 2 1 

Input

6
1 2
1 3
2 4
4 5
4 6
5 6 3


Output

1 2 4 5 4 6 4 2 1 3 1 

Input

6
1 2
1 3
2 4
4 5
4 6
5 3 6


Output

-1
"""

def find_ant_route(n, edges, leaf_order):
    # Initialize adjacency lists
    adj = [[] for _ in range(n)]
    adj2 = [[] for _ in range(n)]
    
    # Build the adjacency list from the edges
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    # Map leaf order to a dictionary for quick lookup
    leaf = {}
    for i, leaf_node in enumerate(leaf_order):
        leaf[leaf_node - 1] = i
    
    inf = 200000
    
    def dfs1(v, frm, adj2):
        if len(adj[v]) == 1 and v != 0:
            return (inf if v not in leaf else leaf[v], v)
        best = float('inf')
        for u in adj[v]:
            if u != frm:
                c = dfs1(u, v, adj2)
                adj2[v].append(c)
                best = min(best, c[0])
        return (best, v)
    
    dfs1(0, -1, adj2)
    
    for i in range(n):
        adj2[i].sort()
    
    path = []
    
    def dfs2(v, frm, path):
        path.append(v + 1)
        for _, u in adj2[v]:
            if u != frm:
                dfs2(u, v, path)
        if frm != -1:
            path.append(frm + 1)
    
    dfs2(0, -1, path)
    
    gd = []
    for i in path:
        if i - 1 in leaf:
            gd.append(i)
    
    if gd == leaf_order:
        return path
    else:
        return -1