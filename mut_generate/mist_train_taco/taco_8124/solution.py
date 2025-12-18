"""
QUESTION:
Jack has just moved to a new city called Rapture. He wants to use the public public transport system. The fare rules are as follows:  

1.Each pair of connected stations has a fare assigned to it regardless of direction of travel.  
2.If Jack travels from station A to station B, he only has to pay the  difference between (the fare from A to B) and (the cumulative fare paid to reach station A),  [fare(A,B) - total fare to reach station A].  If the difference is negative, travel is free of cost from A to B.  

Jack is low on cash and needs your help to figure out the most cost efficient way to go from the first station to the last station. Given the number of stations $g\text{_}nodes$ (numbered from $\mbox{1}$ to $g\text{_}nodes$), and the fares (weights) between the $g\text{_edges}$ pairs of stations that are connected, determine the lowest fare from station $\mbox{1}$ to station $g\text{_}nodes$.  

Example 

$g\text{_}nodes=4$ 

$g_{-}\textit{from}=[1,1,2,3]$ 

$g_{-}to=[2,3,4,4]$ 

$g\text{_weight}=[20,5,30,40]$   

The graph looks like this:

Travel from station $1\rightarrow2\rightarrow4$ costs $\textbf{20}$ for the first segment ($1\rightarrow2$) then the cost differential, an additional $30-20=10$ for the remainder.  The total cost is $30$.   

Travel from station $1\rightarrow3\rightarrow4$ costs $5$ for the first segment, then an additional $40-5=35$ for the remainder, a total cost of $\boldsymbol{40}$.   

The lower priced option costs $30$.  

Function Description 

Complete the getCost function in the editor below.  

getCost has the following parameters:

int g_nodes: the number of stations in the network  
int g_from[g_edges]: end stations of a bidirectional connection  
int g_to[g_edges]: $g\text{_from}[i]$ is connected to $g\textrm{_to}[i]$  at cost $g\text{_weight}[i]$  
int g_weight[g_edges]: the cost of travel between associated stations  

Prints 

- int or string: the cost of the lowest priced route from station $\mbox{I}$ to station $g\text{_}nodes$ or NO PATH EXISTS.  No return value is expected.

Input Format

The first line contains two space-separated integers, $g\text{_}nodes$ and $g\text{_edges}$, the number of stations and the number of connections between them. 

Each of the next $g\text{_edges}$ lines contains three space-separated integers, $g\text{_from},g\text{_to}$ and $g\text{_weight}$, the connected stations and the fare between them.  

Constraints

$1\leq g\text{_}nodes\leq50000$  
$1\leq g\text{_edges}\leq5000000$  
$1\leq g\text{_weight}[i]\leq10^7$
"""

import heapq

def find_lowest_fare(g_nodes, g_from, g_to, g_weight):
    # Create the graph
    graph = {i: [] for i in range(1, g_nodes + 1)}
    for a, b, w in zip(g_from, g_to, g_weight):
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    # Initialize the priority queue and visited set
    queue = [(0, 1)]
    visited = set()
    no_path = True
    
    # Dijkstra's algorithm with a twist
    while queue:
        curr = heapq.heappop(queue)
        visited.add(curr[1])
        if curr[1] == g_nodes:
            return curr[0]
        for w, b in graph[curr[1]]:
            if b not in visited:
                heapq.heappush(queue, (max(curr[0], w), b))
    
    # If no path is found
    return 'NO PATH EXISTS'