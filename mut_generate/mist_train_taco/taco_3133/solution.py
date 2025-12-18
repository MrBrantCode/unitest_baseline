"""
QUESTION:
A direced graph is strongly connected if every two nodes are reachable from each other. In a strongly connected component of a directed graph, every two nodes of the component are mutually reachable.

Constraints

* 1 ≤ |V| ≤ 10,000
* 0 ≤ |E| ≤ 30,000
* 1 ≤ Q ≤ 100,000

Input

A directed graph G(V, E) and a sequence of queries where each query contains a pair of nodes u and v.


|V| |E|
s0 t0
s1 t1
:
s|E|-1 t|E|-1
Q
u0 v0
u1 v1
:
uQ-1 vQ-1


|V| is the number of nodes and |E| is the number of edges in the graph. The graph nodes are named with the numbers 0, 1,..., |V|-1 respectively.

si and ti represent source and target nodes of i-th edge (directed).

ui and vi represent a pair of nodes given as the i-th query.

Output

For each query, pinrt "1" if the given nodes belong to the same strongly connected component, "0" otherwise.

Example

Input

5 6
0 1
1 0
1 2
2 4
4 3
3 2
4
0 1
0 3
2 3
3 4


Output

1
0
1
1
"""

def are_nodes_in_same_scc(num_nodes, edges, queries):
    def kosaraju(edges, reverse_edges):
        import sys
        sys.setrecursionlimit(10 ** 7)
        v_count = len(edges)
        order = [0] * v_count
        k = [1]

        def get_order(v):
            order[v] = 1
            [None for dest in edges[v] if order[dest] == 0 and get_order(dest)]
            order[v] = k[0]
            k[0] += 1

        def get_components(v):
            order[v] = 0
            return [v] + [_v for dest in reverse_edges[v] if order[dest] > 0 for _v in get_components(dest)]
        
        [None for v in range(v_count) if order[v] == 0 and get_order(v)]
        return [get_components(v) for (v, _) in sorted(enumerate(order), key=lambda x: x[1], reverse=True) if order[v] > 0]

    # Create adjacency lists for the graph and its reverse
    adj_list = [[] for _ in range(num_nodes)]
    reverse_adj_list = [[] for _ in range(num_nodes)]
    
    for (a, b) in edges:
        adj_list[a].append(b)
        reverse_adj_list[b].append(a)
    
    # Get strongly connected components
    scc = kosaraju(adj_list, reverse_adj_list)
    
    # Create a group mapping for each node
    group = [0] * num_nodes
    for i, component in enumerate(scc):
        for node in component:
            group[node] = i
    
    # Process queries
    result = []
    for (u, v) in queries:
        result.append('1' if group[u] == group[v] else '0')
    
    return result