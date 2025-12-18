"""
QUESTION:
<image>


A directed acyclic graph (DAG) can be used to represent the ordering of tasks. Tasks are represented by vertices and constraints where one task can begin before another, are represented by edges. For example, in the above example, you can undertake task B after both task A and task B are finished. You can obtain the proper sequence of all the tasks by a topological sort.

Given a DAG $G$, print the order of vertices after the topological sort.

Constraints

* $1 \leq |V| \leq 10,000$
* $0 \leq |E| \leq 100,000$
* There are no parallel edges in $G$
* There are no self loops in $G$

Input

A directed graph $G$ is given in the following format:
$|V|\;|E|$
$s_0 \; t_0$
$s_1 \; t_1$
:
$s_{|E|-1} \; t_{|E|-1}$



$|V|$ is the number of vertices and $|E|$ is the number of edges in the graph. The graph vertices are named with the numbers $0, 1,..., |V|-1$ respectively.

$s_i$ and $t_i$ represent source and target nodes of $i$-th edge (directed).

Output

Print the vertices numbers in order. Print a number in a line.

If there are multiple possible solutions, print any one of them (the solution is judged by a special validator).

Example

Input

6 6
0 1
1 2
3 1
3 4
4 5
5 2


Output

0
3
1
4
5
2
"""

from collections import deque
from typing import List, Optional, Tuple

def topological_sort_dag(V: int, E: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    # Initialize the graph and in-degrees
    graph = [[] for _ in range(V)]
    in_degrees = [0] * V
    
    # Build the graph and calculate in-degrees
    for s, t in edges:
        graph[s].append(t)
        in_degrees[t] += 1
    
    # Find all vertices with zero in-degree
    order = [i for i in range(V) if not in_degrees[i]]
    queue = deque(order)
    
    # Perform topological sort
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            in_degrees[v] -= 1
            if not in_degrees[v]:
                queue.append(v)
                order.append(v)
    
    # Check if all vertices are included in the order
    return order if len(order) == V else None