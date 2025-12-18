"""
QUESTION:
The best night ever in the world has come! It's 8 p.m. of December 24th, yes, the night of Cristmas Eve. Santa Clause comes to a silent city with ringing bells. Overtaking north wind, from a sleigh a reindeer pulls she shoot presents to soxes hanged near windows for children.

The sleigh she is on departs from a big christmas tree on the fringe of the city. Miracle power that the christmas tree spread over the sky like a web and form a paths that the sleigh can go on. Since the paths with thicker miracle power is easier to go, these paths can be expressed as undirected weighted graph.

Derivering the present is very strict about time. When it begins dawning the miracle power rapidly weakens and Santa Clause can not continue derivering any more. Her pride as a Santa Clause never excuses such a thing, so she have to finish derivering before dawning.

The sleigh a reindeer pulls departs from christmas tree (which corresponds to 0th node), and go across the city to the opposite fringe (n-1 th node) along the shortest path. Santa Clause create presents from the miracle power and shoot them from the sleigh the reindeer pulls at his full power. If there are two or more shortest paths, the reindeer selects one of all shortest paths with equal probability and go along it.

By the way, in this city there are p children that wish to see Santa Clause and are looking up the starlit sky from their home. Above the i-th child's home there is a cross point of the miracle power that corresponds to c[i]-th node of the graph. The child can see Santa Clause if (and only if) Santa Clause go through the node.

Please find the probability that each child can see Santa Clause.

Constraints

* 3 ≤ n ≤ 100
* There are no parallel edges and a edge whose end points are identical.
* 0 < weight of the edge < 10000

Input

Input consists of several datasets.

The first line of each dataset contains three integers n, m, p, which means the number of nodes and edges of the graph, and the number of the children. Each node are numbered 0 to n-1.

Following m lines contains information about edges. Each line has three integers. The first two integers means nodes on two endpoints of the edge. The third one is weight of the edge.

Next p lines represent c[i] respectively.

Input terminates when n = m = p = 0.

Output

For each dataset, output p decimal values in same order as input. Write a blank line after that.

You may output any number of digit and may contain an error less than 1.0e-6.

Example

Input

3 2 1
0 1 2
1 2 3
1
4 5 2
0 1 1
0 2 1
1 2 1
1 3 1
2 3 1
1
2
0 0 0


Output

1.00000000

0.50000000
0.50000000
"""

from heapq import heappush, heappop

def calculate_visibility_probabilities(n, m, p, edges, children):
    INF = 10 ** 20
    
    # Initialize the graph
    graph = [[] for _ in range(n)]
    for (x, y, w) in edges:
        graph[x].append((y, w))
        graph[y].append((x, w))
    
    # Dijkstra's algorithm setup
    que = []
    heappush(que, (0, 0))
    shortest_counter = [[0] * n for _ in range(n)]
    shortest_counter[0][0] = 1
    dist = [INF] * n
    dist[0] = 0
    path_counter = [0] * n
    path_counter[0] = 1
    
    # Dijkstra's algorithm
    while que:
        (total, node) = heappop(que)
        count = shortest_counter[node]
        for (to, w) in graph[node]:
            new_total = total + w
            new_count = [i for i in count]
            new_count[to] += path_counter[node]
            if dist[to] > new_total:
                dist[to] = new_total
                shortest_counter[to] = [i for i in new_count]
                path_counter[to] = path_counter[node]
                heappush(que, (new_total, to))
            elif dist[to] == new_total:
                shortest_counter[to] = [i + j for (i, j) in zip(shortest_counter[to], new_count)]
                path_counter[to] += path_counter[node]
    
    # Calculate probabilities
    probabilities = []
    for child in children:
        probabilities.append(shortest_counter[n - 1][child] / path_counter[n - 1])
    
    return probabilities