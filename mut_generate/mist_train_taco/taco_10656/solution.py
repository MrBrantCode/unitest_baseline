"""
QUESTION:
Given an undirected tree, let the distance between vertices u and v be the number of edges on the simple path from u to v. The diameter of a tree is the maximum among the distances between any two vertices. We will call a tree good if and only if its diameter is at most K.

You are given an undirected tree with N vertices numbered 1 through N. For each i (1≦i≦N-1), there is an edge connecting vertices A_i and B_i.

You want to remove zero or more vertices from the tree, so that the resulting tree is good. When a vertex is removed, all incident edges will also be removed. The resulting graph must be connected.

Find the minimum number of vertices that you need to remove in order to produce a good tree.

Constraints

* 2≦N≦2000
* 1≦K≦N-1
* 1≦A_i≦N, 1≦B_i≦N
* The graph defined by A_i and B_i is a tree.

Input

The input is given from Standard Input in the following format:


N K
A_1 B_1
A_2 B_2
:
A_{N-1} B_{N-1}


Output

Print the minimum number of vertices that you need to remove in order to produce a good tree.

Examples

Input

6 2
1 2
3 2
4 2
1 6
5 6


Output

2


Input

6 5
1 2
3 2
4 2
1 6
5 6


Output

0
"""

def min_vertices_to_remove(N, K, edges):
    from collections import deque

    # Build the graph
    graph = [[] for _ in range(N + 1)]
    for (a, b) in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    ans = N
    rad = K // 2
    
    for center in range(1, N + 1):
        stack = [center]
        dep = [[-1, -1] for _ in range(N + 1)]
        dep[center] = [0, 0]
        
        while stack:
            x = stack.pop()
            for (i, y) in enumerate(graph[x]):
                if x == center:
                    dep[y] = [1, i + 1]
                    stack.append(y)
                elif dep[y][0] == -1:
                    stack.append(y)
                    dep[y][0] = dep[x][0] + 1
                    dep[y][1] = dep[x][1]
        
        anstmp = 0
        bonus = [0] * (len(graph[center]) + 1)
        
        for i in range(1, N + 1):
            if dep[i][0] <= rad:
                anstmp += 1
            if dep[i][0] == rad + 1:
                bonus[dep[i][1]] += 1
        
        if K % 2:
            anstmp += max(bonus)
        
        ans = min(N - anstmp, ans)
    
    return max(ans, 0)