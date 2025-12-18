"""
QUESTION:
Given is a connected undirected graph with N vertices and M edges. The vertices are numbered 1 to N, and the edges are described by a grid of characters S. If S_{i,j} is `1`, there is an edge connecting Vertex i and j; otherwise, there is no such edge.

Determine whether it is possible to divide the vertices into non-empty sets V_1, \dots, V_k such that the following condition is satisfied. If the answer is yes, find the maximum possible number of sets, k, in such a division.

* Every edge connects two vertices belonging to two "adjacent" sets. More formally, for every edge (i,j), there exists 1\leq t\leq k-1 such that i\in V_t,j\in V_{t+1} or i\in V_{t+1},j\in V_t holds.

Constraints

* 2 \leq N \leq 200
* S_{i,j} is `0` or `1`.
* S_{i,i} is `0`.
* S_{i,j}=S_{j,i}
* The given graph is connected.
* N is an integer.

Input

Input is given from Standard Input in the following format:


N
S_{1,1}...S_{1,N}
:
S_{N,1}...S_{N,N}


Output

If it is impossible to divide the vertices into sets so that the condition is satisfied, print -1. Otherwise, print the maximum possible number of sets, k, in a division that satisfies the condition.

Examples

Input

2
01
10


Output

2


Input

3
011
101
110


Output

-1


Input

6
010110
101001
010100
101000
100000
010000


Output

4
"""

from collections import deque

def max_possible_sets(n, S):
    edge = [[] for _ in range(n)]
    mat = [[1000] * n for _ in range(n)]
    
    # Build the adjacency matrix and edge list
    for i in range(n):
        for j in range(n):
            if S[i][j] == '1':
                mat[i][j] = 1
                if j > i:
                    edge[i].append(j)
                    edge[j].append(i)
    
    # Set the diagonal to 0
    for i in range(n):
        mat[i][i] = 0
    
    # Floyd-Warshall algorithm to find shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
    
    # BFS to check if the graph is bipartite
    dq = deque()
    dist = [-1] * n
    dq.append((0, 0))
    ok = True
    
    while dq:
        v, d = dq.popleft()
        if dist[v] == d:
            continue
        if dist[v] == -1:
            dist[v] = d
        else:
            ok = False
            break
        for item in edge[v]:
            if dist[item] == -1:
                dq.append((item, d + 1))
    
    if ok:
        ans = 0
        for line in mat:
            ans = max(ans, max(line))
        return ans + 1
    else:
        return -1