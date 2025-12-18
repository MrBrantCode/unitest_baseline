"""
QUESTION:
Detective Rust is investigating a homicide and he wants to chase down the murderer. The murderer knows he would definitely get caught if he takes the main roads for fleeing, so he uses the village roads (or side lanes) for running away from the crime scene.

Rust knows that the murderer will take village roads and he wants to chase him down. He is observing the city map, but it doesn't show the village roads (or side lanes) on it and shows only the main roads. 

The map of the city is a graph consisting $N$ nodes (labeled $\mbox{I}$ to $N$) where a specific given node $\mbox{S}$ represents the current position of Rust and the rest of the nodes denote other places in the city, and an edge between two nodes is a main road between two places in the city. It can be suitably assumed that an edge that doesn't exist/isn't shown on the map is a village road (side lane). That means, there is a village road between two nodes $\boldsymbol{\alpha}$ and $\boldsymbol{b}$ iff(if and only if) there is no city road between them.  

In this problem, distance is calculated as number of village roads (side lanes) between any two places in the city.

Rust wants to calculate the shortest distance from his position (Node $\mbox{S}$) to all the other places in the city if he travels only using the village roads (side lanes).

Note: The graph/map of the city is ensured to be a sparse graph.

Input Format

The first line contains $\mathbf{T}$, denoting the number of test cases. $\mathbf{T}$ testcases follow. 

First line of each test case has two integers $N$, denoting the number of cities in the map and $\mbox{M}$, denoting the number of roads in the map. 

The next $\mbox{M}$ lines each consist of two space-separated integers $\boldsymbol{x}$ and $y$ denoting a main road between city $\boldsymbol{x}$ and city $y$. 
The last line has an integer $\mbox{S}$, denoting the current position of Rust. 

Constraints

$1\leq T\leq10$  
$2\leq N\leq2\times10^5$  
$0\leq M\leq120000$  
$1\leq x,y,S\leq N$  

Note  

No nodes will have a road to itself.   
There will not be multiple edges between any pair of nodes i.e. there is at most one undirected edge between them.   
Graph is guaranteed to be sparse. 
It is guranteed that there will be a path between any pair of nodes using the side lanes.

Output Format

For each of T test cases, print a single line consisting of N-1 space separated integers, denoting the shortest distances of the remaining N-1 places from Rust's position (that is all distances, except the source node to itself) using the village roads/side lanes in ascending order based on vertex number.  

Sample Input 0
2
4 3
1 2
2 3
1 4
1
4 2
1 2
2 3
2

Sample Output 0
3 1 2
2 2 1

Explanation 0

The graph in the first testcase can be shown as:

Here the source node is 1 (marked S). 

The distance from 1 to 2 is 3. Path: 1 -> 3 -> 4 -> 2 

The distance from 1 to 3 is 1. Path: 1 -> 3 

The distance from 1 to 4 is 2. Path: 1 -> 3 -> 4
"""

from collections import deque

def shortest_village_distances(n, m, main_roads, start_node):
    # Create sets to store main roads and nodes involved in main roads
    pe = set(main_roads)
    pe1 = set(node for road in main_roads for node in road)
    
    # Initialize result list with None
    res = [None] * (n + 1)
    
    # BFS function to calculate shortest distances
    def bfs(s, pe, res, n, pe1):
        notdiscovered = set(range(1, n + 1))
        q = deque()
        level = 0
        q.append((s, level))
        notdiscovered.discard(s)
        while q and notdiscovered:
            v = q.popleft()
            i = v[0]
            level = v[1] + 1
            nd = []
            for j in notdiscovered:
                if j == i:
                    continue
                if i not in pe1 and j not in pe1 or ((i, j) not in pe and (j, i) not in pe):
                    q.append((j, level))
                    nd.append(j)
                    res[j] = level
            for j in nd:
                notdiscovered.discard(j)
        return res
    
    # Call BFS function
    res = bfs(start_node, pe, res, n, pe1)
    
    # Filter out the start node and return the result
    return [dist for dist in res if dist is not None and dist != 0]