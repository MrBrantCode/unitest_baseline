"""
QUESTION:
Constraints

* 1 ≤ |V| ≤ 1000
* 0 ≤ |E| ≤ 2000
* -10000 ≤ di ≤ 10000
* There are no parallel edges
* There are no self-loops

Input

An edge-weighted graph G (V, E) and the source r.


|V| |E| r
s0 t0 d0
s1 t1 d1
:
s|E|-1 t|E|-1 d|E|-1


|V| is the number of vertices and |E| is the number of edges in G. The graph vertices are named with the numbers 0, 1,..., |V|-1 respectively. r is the source of the graph.

si and ti represent source and target vertices of i-th edge (directed) and di represents the cost of the i-th edge.

Output

If the graph contains a negative cycle (a cycle whose sum of edge costs is a negative value) which is reachable from the source r, print


NEGATIVE CYCLE


in a line.

Otherwise, print


c0
c1
:
c|V|-1


The output consists of |V| lines. Print the cost of the shortest path from the source r to each vertex 0, 1, ... |V|-1 in order. If there is no path from the source to a vertex, print "INF".

Examples

Input

4 5 0
0 1 2
0 2 3
1 2 -5
1 3 1
2 3 2


Output

0
2
-3
-1


Input

4 6 0
0 1 2
0 2 3
1 2 -5
1 3 1
2 3 2
3 1 0


Output

NEGATIVE CYCLE


Input

4 5 1
0 1 2
0 2 3
1 2 -5
1 3 1
2 3 2


Output

INF
0
-5
-3
"""

import collections

def find_shortest_paths(V_num, E_num, r, edges):
    adjc_list = [[] for _ in range(V_num)]
    for src, dst, w in edges:
        adjc_list[src].append((w, dst))
    
    INF = 99999999999999
    d = [INF for _ in range(V_num)]
    d[r] = 0
    stack = collections.deque()
    yet = [ele for ele in range(V_num)]

    def dfs(stack):
        if not stack:
            return
        n = stack[0]
        yet.remove(n)
        for _, dst in adjc_list[n]:
            if dst in yet:
                stack.appendleft(dst)
                dfs(stack)
        else:
            stack.popleft()

    def bellman_ford():
        for _ in range(V_num - 1):
            for src, dst, w in edges:
                if d[dst] > w + d[src]:
                    d[dst] = w + d[src]
        for src, dst, w in edges:
            if d[dst] > w + d[src]:
                return -1
        return

    stack.clear()
    stack.appendleft(r)
    dfs(stack)
    filtered_edges = list(filter(lambda e: e[0] not in yet and e[1] not in yet, edges))
    
    if bellman_ford() == -1:
        return "NEGATIVE CYCLE"
    
    result = []
    for d_i in d:
        if d_i == INF:
            result.append("INF")
        else:
            result.append(d_i)
    
    return result