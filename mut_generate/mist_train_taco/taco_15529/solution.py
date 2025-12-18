"""
QUESTION:
Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i, 0<=i
Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.
 
Example:
Input:
n = 6, m= 7
edge=[[0,1,2],[0,4,1],[4,5,4]
,[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
Output:
0 2 3 6 1 5
 
Your Task:
You don't need to print or input anything. Complete the function shortest path() which takes an integer N as number of vertices, an integer M as number of edges and a 2D Integer array(or vector) edges as the input parameters and returns an integer array(or vector), denoting the list of distance from src to all nodes.
 
Constraint:
	1 <= n,m <= 100
	0 <= edge_{i,0},edge_{i,1} < n
	 
 
Expected Time Complexity: O(N+E), where N is the number of nodes and E is edges
Expected Space Complexity: O(N)
"""

from typing import List
import math
from collections import deque

def shortest_path_from_src(n: int, m: int, edges: List[List[int]]) -> List[int]:
    # Initialize the in-degree dictionary and adjacency list
    ind = {i: 0 for i in range(n)}
    adj = [[] for _ in range(n)]
    
    # Build the adjacency list and update in-degrees
    for u, v, w in edges:
        adj[u].append((v, w))
        ind[v] += 1
    
    # Initialize the queue with vertices of in-degree 0
    q = deque([i for i in ind if ind[i] == 0])
    ans = deque()
    
    # Perform topological sort using Kahn's algorithm
    while q:
        node = q.popleft()
        ans.append(node)
        for nbr, _ in adj[node]:
            ind[nbr] -= 1
            if ind[nbr] == 0:
                q.append(nbr)
    
    # Initialize distances with infinity
    dist = [math.inf] * n
    dist[0] = 0
    
    # Update distances based on the topological order
    while ans:
        node = ans.popleft()
        for nbr, weight in adj[node]:
            if dist[node] + weight < dist[nbr]:
                dist[nbr] = dist[node] + weight
    
    # Convert unreachable vertices to -1
    for i in range(n):
        if dist[i] == math.inf:
            dist[i] = -1
    
    return dist