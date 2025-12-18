"""
QUESTION:
A tree is a connected graph without cycles. A rooted tree has a special vertex called the root. The parent of a vertex $v$ (different from root) is the previous to $v$ vertex on the shortest path from the root to the vertex $v$. Children of the vertex $v$ are all vertices for which $v$ is the parent.

A vertex is a leaf if it has no children. We call a vertex a bud, if the following three conditions are satisfied:

it is not a root,

it has at least one child, and

all its children are leaves.

You are given a rooted tree with $n$ vertices. The vertex $1$ is the root. In one operation you can choose any bud with all its children (they are leaves) and re-hang them to any other vertex of the tree. By doing that you delete the edge connecting the bud and its parent and add an edge between the bud and the chosen vertex of the tree. The chosen vertex cannot be the bud itself or any of its children. All children of the bud stay connected to the bud.

What is the minimum number of leaves it is possible to get if you can make any number of the above-mentioned operations (possibly zero)?


-----Input-----

The input consists of multiple test cases. The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the number of the vertices in the given tree.

Each of the next $n-1$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) meaning that there is an edge between vertices $u$ and $v$ in the tree.

It is guaranteed that the given graph is a tree.

It is guaranteed that the sum of $n$ over all test cases doesn't exceed $2 \cdot 10^5$.


-----Output-----

For each test case print a single integer — the minimal number of leaves that is possible to get after some operations.


-----Examples-----

Input
5
7
1 2
1 3
1 4
2 5
2 6
4 7
6
1 2
1 3
2 4
2 5
3 6
2
1 2
7
7 3
1 5
1 3
4 6
4 7
2 1
6
2 1
2 3
4 5
3 4
3 6
Output
2
2
1
2
1


-----Note-----

In the first test case the tree looks as follows:

Firstly you can choose a bud vertex $4$ and re-hang it to vertex $3$. After that you can choose a bud vertex $2$ and re-hang it to vertex $7$. As a result, you will have the following tree with $2$ leaves:

It can be proved that it is the minimal number of leaves possible to get.

In the second test case the tree looks as follows:

You can choose a bud vertex $3$ and re-hang it to vertex $5$. As a result, you will have the following tree with $2$ leaves:

It can be proved that it is the minimal number of leaves possible to get.
"""

def min_leaves_after_operations(n, edges):
    # Create adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initialize parent, child count, and depth arrays
    par = [-1] * (n + 1)
    child_cnts = [0] * (n + 1)
    depth = [-1] * (n + 1)
    depth[1] = 0
    
    # Perform DFS to fill parent, child count, and depth arrays
    stack = [(1, -1)]
    while stack:
        node, p = stack.pop()
        par[node] = p
        for nex in adj[node]:
            if nex != p:
                child_cnts[node] += 1
                stack.append((nex, node))
                depth[nex] = depth[node] + 1
    
    # Sort nodes by depth in descending order
    node_depths = [(depth[node], node) for node in range(1, n + 1)]
    node_depths.sort(reverse=True)
    
    # Initialize pruned array and bud count
    pruned = [False] * (n + 1)
    bud_cnts = 0
    
    # Process nodes to count buds and update child counts
    for depth, node in node_depths:
        if depth >= 2 and not pruned[node] and not pruned[par[node]]:
            bud_cnts += 1
            two_up = par[par[node]]
            child_cnts[two_up] -= 1
            pruned[par[node]] = True
    
    # Calculate direct leaves and bud contribution
    direct_leaves = child_cnts[1]
    bud_contribution = n - 1 - direct_leaves - bud_cnts * 2
    leaves_without_bud = max(1, direct_leaves)
    
    # Calculate the final answer
    ans = leaves_without_bud + bud_contribution
    return ans