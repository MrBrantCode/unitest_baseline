"""
QUESTION:
Given a Weighted Directed Acyclic Graph (DAG) and a source vertex s in it, find the longest distances from s to all other vertices in the given graph.
Example 1:
Input:
N=3
M=2
SRC=0
edges[]={{0,2,1},{0,1,1}}
Output:
distance[]={0,1,1}
Explanation:
the shortest distance of vertex 1 from 0 is 1 and that of two is also 1.
 
Example 2:
Input:
N=6
M=10
SRC=1
edges[]={{0,1,5},{0,2,3},{1,3,6},{1,2,2},{2,4,4},{2,5,2},{2,3,7},{3,5,1},{3,4,-1},{4,5,-2}}
Output:
distance[]={INF,0,2,9,8,10}
Explanation:
The vertex zero is not reachable from vertex 1 so its distance is INF, for 2 it is 2, for 3 it is 9, the same goes for 4 and 5.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximumDistance() which takes the edge list edges[] where edges[0] , edges[1] and edges[2] represent u,v and weight, its size M and the number of nodes N as input parameters and returns the distance array in the distance array instead of passing INF you need to have INT_MIN driver will automatically update it to INF.
 
Expected Time Complexity: O(V+E)
Expected Auxiliary Space: O(V)
 
Constraints:
1 <= N <= 10^{3}
1<=M<=N*(N-1)/2
0<=edges[i][0],edges[i][1]
-100<=edges[i][2]<=100.
"""

from typing import List
from collections import defaultdict, deque

def find_longest_distances(N: int, M: int, SRC: int, edges: List[List[int]]) -> List[int]:
    adj = defaultdict(list)
    dist = [-float('inf')] * N
    visited = set()
    topo = []

    def postDfs(node):
        for neib, w in adj[node]:
            if neib not in visited:
                postDfs(neib)
        visited.add(node)
        topo.append(node)

    for u, v, w in edges:
        adj[u].append((v, w))

    for i in range(N):
        if i not in visited:
            postDfs(i)

    dist[SRC] = 0
    while topo:
        node = topo.pop()
        nodeDist = dist[node]
        for neib, w in adj[node]:
            if dist[neib] < nodeDist + w:
                dist[neib] = nodeDist + w

    for i in range(N):
        if dist[i] == float('-inf'):
            dist[i] = 'INF'

    return dist