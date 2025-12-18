"""
QUESTION:
You are given a graph with N vertices (numbered 1 to N) and M bidirectional edges, which doesn't contain multiple edges or self-loops — that is, the given graph is a simple undirected graph.

For each pair of vertices a, b such that 1 ≤ a, b ≤ N, it is possible to add a new edge between vertices a and b to the graph, with a cost of (a - b)^2.

Find the minimum cost of adding edges so that vertex N is reachable from vertex 1.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains 2 space-separated integers, N and M.
- The i^{th} of the next M lines contains 2 space-separated integers u_{i} and v_{i}, denoting a bidirectional edge between vertex u_{i} and vertex v_{i} in the graph.

------ Output Format ------ 

For each test case, output the answer in a single line.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$2 ≤ N ≤ 2 \cdot 10^{5}$
$0 ≤ M ≤ 2 \cdot 10^{5}$
$1 ≤ u_{i}, v_{i} ≤ N$
- The graph doesn't contain self-loops or multiple edges
- Sum of $N$ over all testcases is no more than $2 \cdot 10^{5}$.
- Sum of $M$ over all testcases is no more than $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
2 0
5 4
3 2
1 4
5 3
4 2
6 3
1 2
3 2
1 3

----- Sample Output 1 ------ 
1
0
3

----- explanation 1 ------ 
Test Case $1$: Add an edge between vertices $1$ and $2$, with cost $(1-2)^2 = 1$.

Test Case $2$: Vertices $1$ and $5$ are already connected, so no edges need to be added.
"""

import heapq

def find_min_cost_to_reach_n(N, M, edges):
    # Create adjacency list
    adj = [[] for _ in range(N + 1)]
    
    # Add given edges to adjacency list with cost 0
    for u, v in edges:
        adj[u].append([v, 0])
        adj[v].append([u, 0])
    
    # Add additional edges with cost (a - b)^2
    for i in range(1, N):
        adj[i].append([i + 1, 1])
        adj[i + 1].append([i, 1])
    
    # Dijkstra's algorithm to find minimum cost to reach N from 1
    cost = [float('inf')] * (N + 1)
    cost[1] = 0
    flag = [False] * (N + 1)
    start = [[0, 1]]
    
    while start:
        _, p = heapq.heappop(start)
        if flag[p]:
            continue
        flag[p] = True
        for e in adj[p]:
            if cost[e[0]] > cost[p] + e[1]:
                cost[e[0]] = cost[p] + e[1]
                heapq.heappush(start, [cost[e[0]], e[0]])
    
    return cost[N]