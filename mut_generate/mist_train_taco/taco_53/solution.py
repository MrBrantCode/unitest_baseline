"""
QUESTION:
Given an undirected graph and a starting node, determine the lengths of the shortest paths from the starting node to all other nodes in the graph.  If a node is unreachable, its distance is -1.  Nodes will be numbered consecutively from $1$ to $n$, and edges will have varying distances or lengths.

For example, consider the following graph of 5 nodes:

Begin	End	Weight
1	2	5
2	3	6
3	4	2
1	3	15

Starting at node $1$, the shortest path to $2$ is direct and distance $5$.  Going from $1$ to $3$, there are two paths: $1\rightarrow2\rightarrow3$ at a distance of $5+6=11$ or $1\rightarrow3$ at a distance of $15$.  Choose the shortest path, $\mbox{11}$.  From $1$ to $4$, choose the shortest path through $3$ and extend it: $1\to2\to3\to4$ for a distance of $11+2=13$  There is no route to node $5$, so the distance is $-1$.

The distances to all nodes in increasing node order, omitting the starting node, are 5 11 13 -1.

Function Description  

Complete the shortestReach function in the editor below.  It should return an array of integers that represent the shortest distance to each node from the start node in ascending order of node number.  

shortestReach has the following parameter(s):  

n: the number of nodes in the graph  
edges: a 2D array of integers where each $\textit{edges}[i]$ consists of three integers that represent the start and end nodes of an edge, followed by its length  
s: the start node number  

Input Format

The first line contains $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each test case is as follows: 

- The first line contains two space-separated integers $n$ and $m$, the number of nodes and edges in the graph. 

- Each of the next $m$ lines contains three space-separated integers $\boldsymbol{x}$, $y$, and $\textbf{r}$, the beginning and ending nodes of an edge, and the length of the edge. 

- The last line of each test case has an integer $\boldsymbol{\mathrm{~S~}}$, denoting the starting position.  

Constraints

$1\leq t\leq10$ 

$2\leq n\leq3000$ 

$1\leq m\leq\frac{N\times(N-1)}{2}$ 

$1\leq x,y,s\leq N$ 

$1\leq r\leq10^5$  

If there are edges between the same pair of nodes with different weights, they are to be considered as is, like multiple edges.

Output Format

For each of the $\boldsymbol{\boldsymbol{t}}$ test cases, print a single line consisting $n-1$ space separated integers denoting the shortest distance to the $n-1$ nodes from starting position $\boldsymbol{\mathrm{~S~}}$ in  increasing order of their labels, excluding $\boldsymbol{\mathrm{~S~}}$. 

For unreachable nodes, print $-1$.

Sample Input
1
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1

Sample Output
24 3 15

Explanation

The graph given in the test case is shown as :

* The lines are weighted edges where weight denotes the length of the edge.

The shortest paths followed for the three nodes 2, 3 and 4 are as follows :

1/S->2 - Shortest Path Value : $24$

1/S->3 - Shortest Path Value : $3$

1/S->3->4 - Shortest Path Value : $15$
"""

import heapq

def shortest_reach(n, edges, start_node):
    # Initialize the adjacency list
    graph = [{} for _ in range(n)]
    
    # Build the graph from the edges list
    for (x, y, r) in edges:
        x -= 1  # Convert to 0-based index
        y -= 1  # Convert to 0-based index
        if y not in graph[x]:
            graph[x][y] = r
        else:
            graph[x][y] = min(graph[x][y], r)
        if x not in graph[y]:
            graph[y][x] = r
        else:
            graph[y][x] = min(graph[y][x], r)
    
    # Initialize distance and visited arrays
    dist = [-1] * n
    visited = [False] * n
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, start_node - 1)]  # Convert start_node to 0-based index
    dist[start_node - 1] = 0
    
    while pq:
        (mindist, minv) = heapq.heappop(pq)
        if not visited[minv]:
            for neighbor, weight in graph[minv].items():
                if dist[neighbor] == -1:
                    dist[neighbor] = mindist + weight
                else:
                    dist[neighbor] = min(dist[neighbor], mindist + weight)
                heapq.heappush(pq, (dist[neighbor], neighbor))
            visited[minv] = True
    
    # Remove the distance of the start node
    del dist[start_node - 1]
    
    return dist