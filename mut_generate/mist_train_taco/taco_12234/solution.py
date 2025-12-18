"""
QUESTION:
Given a directed graph with N nodes and M edges. A source node and a destination node are also given, we need to find how many edges we need to reverse in order to make at least 1 path from the source node to the destination node.
Note: In case there is no way then return -1.
Example 1:
Input:
N=3
M=2
edges[][]={{1,2},{3,2}}
src=1
dst=3
Output:
1
Explanation:
Reverse the edge 3->2.
Example 2:
Input:
N=4
M=3
edges[][]={{1,2},{2,3},{3,4}}
src=1
dst=4
Output:
0
Explanation;
One path already exists between 1 to 4 it is 1->2->3->4.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minimumEdgeReversal() which takes the edge list edges, N the number of nodes of the graph. src (source), and dst (destination) vertex as input parameters and returns the minimum number of edges to be reversed
Expected Time Complexity: O(M*log(M))
Expected Auxiliary Space: O(N+M)
Constraints:
1 <= N ,M<= 10^{5}
1<=edges[i][0],edges[i][1]<=N
"""

from typing import List, Tuple
import heapq as h
from collections import defaultdict

def minimum_edge_reversal(edges: List[Tuple[int, int]], n: int, src: int, dst: int) -> int:
    adj = defaultdict(list)
    edges = set(edges)
    reversed_edges = set()
    
    # Identify reversed edges
    for edge in edges:
        if (edge[1], edge[0]) not in edges:
            reversed_edges.add((edge[1], edge[0]))
    
    # Build the adjacency list with original and reversed edges
    for edge in edges:
        adj[edge[0]].append((edge[1], 0))
    for edge in reversed_edges:
        adj[edge[0]].append((edge[1], 1))
    
    # Initialize distance array and priority queue
    dist = [float('inf')] * (n + 1)
    dist[src] = 0
    pq = [(0, src)]
    
    # Dijkstra's algorithm
    while pq:
        node_dist, node = h.heappop(pq)
        for neib, neib_dist in adj[node]:
            if node_dist + neib_dist < dist[neib]:
                dist[neib] = node_dist + neib_dist
                h.heappush(pq, (dist[neib], neib))
    
    # Return the result
    return dist[dst] if dist[dst] != float('inf') else -1