"""
QUESTION:
You are given $3$ unweighted, undirected graphs, $G_1$, $G_2$, and $G_3$, with $n$ vertices each, where the $k^{th}$ graph has $m_{k}$ edges and the vertices in each graph are numbered from $\mbox{1}$ through $n$. Find the number of ordered triples $(a,b,c)$, where $1\leq a,b,c\leq n$, $a\neq b,b\neq c,c\neq a$, such that there is an edge $(a,b)$ in $G_1$, an edge $(b,c)$ in $G_2$, and an edge $(c,a)$ in $G_3$.

Input Format

The first line contains single integer, $n$, denoting the number of vertices in the graphs. The subsequent lines define $G_1$, $G_2$, and $G_3$. Each graph is defined as follows:

The first line contains an integer, $m$, describing the number of edges in the graph being defined.
Each line $\boldsymbol{i}$ of the $m$ subsequent lines (where $1\leq i\leq m$) contains $2$ space-separated integers describing the respective nodes, $u_i$ and $v_i$ connected by edge $\boldsymbol{i}$.

Constraints

$n\leq10^{5}$
$m_k\leq10^5$, and $k\in\{1,2,3\}$
Each graph contains no cycles and any pair of directly connected nodes is connected by a maximum of $\mbox{1}$ edge.

Output Format

Print a single integer denoting the number of distinct $(a,b,c)$ triples as described in the Problem Statement above.

Sample Input
3
2
1 2
2 3
3
1 2
1 3
2 3
2
1 3
2 3

Sample Output
3

Explanation

There are three possible triples in our Sample Input: 

$(1,2,3)$
$(2,1,3)$
$(3,2,1)$

Thus, we print $3$ as our output.
"""

def count_valid_triples(n, edges_g1, edges_g2, edges_g3):
    # Initialize adjacency lists for each graph
    graph = [[None] * (n + 1) for _ in range(4)]
    
    # Helper function to build adjacency list
    def build_graph(edges, graph_index):
        for u, v in edges:
            if graph[graph_index][u] is None:
                graph[graph_index][u] = set()
            if graph[graph_index][v] is None:
                graph[graph_index][v] = set()
            graph[graph_index][u].add(v)
            graph[graph_index][v].add(u)
    
    # Build adjacency lists for G1, G2, and G3
    build_graph(edges_g1, 1)
    build_graph(edges_g2, 2)
    build_graph(edges_g3, 3)
    
    count = 0
    
    # Iterate over each vertex
    for vertex in range(1, n + 1):
        vertices_to_g1 = graph[1][vertex]
        if vertices_to_g1 is not None:
            vertices_from_g2 = graph[2][vertex]
            if vertices_from_g2 is not None:
                for to_vertex in vertices_from_g2:
                    vertices_from_g3 = graph[3][to_vertex]
                    if vertices_from_g3 is not None:
                        count += len(vertices_to_g1.intersection(vertices_from_g3))
    
    return count