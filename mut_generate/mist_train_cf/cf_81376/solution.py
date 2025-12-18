"""
QUESTION:
Given a tree with `n` nodes (labeled from 0 to `n - 1`) and `n - 1` undirected edges, find the root labels of all minimum height trees (MHTs) that can be formed by selecting any node as the root.

Implement the function `findMinHeightTrees(n, edges)` where `n` is the number of nodes and `edges` is a list of pairs `[ai, bi]` representing the undirected edges between nodes `ai` and `bi`. The function should return a list of root labels of the MHTs.

Constraints: `1 <= n <= 2 * 10^4`, `edges.length == n - 1`, `0 <= ai, bi < n`, `ai != bi`, and all pairs `(ai, bi)` are unique. The input is guaranteed to be a tree with no duplicate edges.
"""

from collections import deque, defaultdict

def findMinHeightTrees(n, edges):
    if n <= 2:
        return [i for i in range(n)]
    
    neighbors = defaultdict(list)
    degrees = [0]*n  # this will store the degree of each node
    
    for i, j in edges:
        neighbors[i].append(j)
        neighbors[j].append(i)
        degrees[i] += 1
        degrees[j] += 1

    first_leaves = deque() 
        
    # The first layer of leaf nodes
    for i in range(n):
        if degrees[i] == 1:
            first_leaves.append(i)
        
    total_nodes_left = n
    while total_nodes_left > 2:
        total_nodes_left -= len(first_leaves)

        next_leaves = deque()

        # remove the leaf nodes of this layer and prepare for the next
        while first_leaves:
            leaf = first_leaves.popleft()
            
            # the only neighbor
            for neighbor in neighbors[leaf]:
                degrees[neighbor] -= 1
                
                if degrees[neighbor] == 1:
                    next_leaves.append(neighbor)
            
        first_leaves = next_leaves
    
    return first_leaves