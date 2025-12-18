"""
QUESTION:
Tree is a connected graph without cycles. A leaf of a tree is any vertex connected with exactly one other vertex.

You are given a tree with n vertices and a root in the vertex 1. There is an ant in each leaf of the tree. In one second some ants can simultaneously go to the parent vertex from the vertex they were in. No two ants can be in the same vertex simultaneously except for the root of the tree.

Find the minimal time required for all ants to be in the root of the tree. Note that at start the ants are only in the leaves of the tree.

Input

The first line contains integer n (2 ≤ n ≤ 5·105) — the number of vertices in the tree.

Each of the next n - 1 lines contains two integers xi, yi (1 ≤ xi, yi ≤ n) — the ends of the i-th edge. It is guaranteed that you are given the correct undirected tree.

Output

Print the only integer t — the minimal time required for all ants to be in the root of the tree.

Examples

Input

12
1 2
1 3
1 4
2 5
2 6
3 7
3 8
3 9
8 10
8 11
8 12


Output

6


Input

2
2 1


Output

1
"""

def find_minimal_time_for_ants(n, edges):
    # Build the graph and tree structure
    graph = [[] for _ in range(n)]
    tree = [0] * n
    
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
        tree[u - 1] += 1
        tree[v - 1] += 1
    
    # Initialize the answer
    ans = 0
    
    # Process each child of the root
    for x in graph[0]:
        depth = []
        stack = [(x, 0, 1)]
        
        # Perform DFS to find depths of leaves
        while stack:
            v, par, d = stack.pop()
            if tree[v] == 1:
                depth.append(d)
            else:
                for dest in graph[v]:
                    if dest != par:
                        stack.append((dest, v, d + 1))
        
        # Sort depths and calculate the maximum depth required
        depth.sort()
        for i in range(1, len(depth)):
            depth[i] = max(depth[i], depth[i - 1] + 1)
        
        # Update the answer with the maximum depth found
        ans = max(ans, depth[-1])
    
    return ans