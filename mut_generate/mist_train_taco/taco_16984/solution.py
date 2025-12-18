"""
QUESTION:
You are given a graph with $3 \cdot n$ vertices and $m$ edges. You are to find a matching of $n$ edges, or an independent set of $n$ vertices.

A set of edges is called a matching if no two edges share an endpoint.

A set of vertices is called an independent set if no two vertices are connected with an edge.


-----Input-----

The first line contains a single integer $T \ge 1$ — the number of graphs you need to process. The description of $T$ graphs follows.

The first line of description of a single graph contains two integers $n$ and $m$, where $3 \cdot n$ is the number of vertices, and $m$ is the number of edges in the graph ($1 \leq n \leq 10^{5}$, $0 \leq m \leq 5 \cdot 10^{5}$).

Each of the next $m$ lines contains two integers $v_i$ and $u_i$ ($1 \leq v_i, u_i \leq 3 \cdot n$), meaning that there is an edge between vertices $v_i$ and $u_i$.

It is guaranteed that there are no self-loops and no multiple edges in the graph.

It is guaranteed that the sum of all $n$ over all graphs in a single test does not exceed $10^{5}$, and the sum of all $m$ over all graphs in a single test does not exceed $5 \cdot 10^{5}$.


-----Output-----

Print your answer for each of the $T$ graphs. Output your answer for a single graph in the following format.

If you found a matching of size $n$, on the first line print "Matching" (without quotes), and on the second line print $n$ integers — the indices of the edges in the matching. The edges are numbered from $1$ to $m$ in the input order.

If you found an independent set of size $n$, on the first line print "IndSet" (without quotes), and on the second line print $n$ integers — the indices of the vertices in the independent set.

If there is no matching and no independent set of the specified size, print "Impossible" (without quotes).

You can print edges and vertices in any order.

If there are several solutions, print any. In particular, if there are both a matching of size $n$, and an independent set of size $n$, then you should print exactly one of such matchings or exactly one of such independent sets.


-----Example-----
Input
4
1 2
1 3
1 2
1 2
1 3
1 2
2 5
1 2
3 1
1 4
5 1
1 6
2 15
1 2
1 3
1 4
1 5
1 6
2 3
2 4
2 5
2 6
3 4
3 5
3 6
4 5
4 6
5 6

Output
Matching
2
IndSet
1
IndSet
2 4
Matching
1 15



-----Note-----

The first two graphs are same, and there are both a matching of size 1 and an independent set of size 1. Any of these matchings and independent sets is a correct answer.

The third graph does not have a matching of size 2, however, there is an independent set of size 2. Moreover, there is an independent set of size 5: 2 3 4 5 6. However such answer is not correct, because you are asked to find an independent set (or matching) of size exactly $n$.

The fourth graph does not have an independent set of size 2, but there is a matching of size 2.
"""

def find_matching_or_independent_set(n, m, edges):
    total_node = 3 * n
    is_node_covered = [False] * (total_node + 1)
    is_edge_in_matching = [False] * (m + 1)
    matching_edge_count = 0

    for i, (u, v) in enumerate(edges, start=1):
        if not is_node_covered[u] and not is_node_covered[v]:
            is_node_covered[u] = is_node_covered[v] = True
            is_edge_in_matching[i] = True
            matching_edge_count += 1

    if matching_edge_count >= n:
        result_type = "Matching"
        result_indices = [i for i in range(1, m + 1) if is_edge_in_matching[i]][:n]
    else:
        result_type = "IndSet"
        result_indices = [i for i in range(1, total_node + 1) if not is_node_covered[i]][:n]

    if len(result_indices) < n:
        result_type = "Impossible"
        result_indices = []

    return result_type, result_indices