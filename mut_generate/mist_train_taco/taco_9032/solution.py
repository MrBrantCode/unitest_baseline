"""
QUESTION:
You are given an unweighted, undirected graph. Write a program to check if it's a tree topology.

-----Input-----

The first line of the input file contains two integers N and M --- number of nodes and number of edges in the graph (0 < N <= 10000, 0 <= M <= 20000). Next M lines contain M edges of that graph --- Each line contains a pair (u, v) means there is an edge between node u and node v (1 <= u,v <= N).

-----Output-----

Print YES if the given graph is a tree, otherwise print NO.

-----Example-----
Input:
3 2
1 2
2 3

Output:
YES
"""

def is_tree_topology(N, M, edges):
    def iscycle(E, v, EXPLORED_NODES, EXPLORED_EDGES):
        EXPLORED_NODES.add(v)
        r = False
        for e in [x for x in E if v in x]:
            if e in EXPLORED_EDGES:
                continue
            if e[0] == v:
                w = e[1]
            else:
                w = e[0]
            if w in EXPLORED_NODES:
                return True
            else:
                EXPLORED_EDGES.add(e)
                r = r or iscycle(E, w, EXPLORED_NODES, EXPLORED_EDGES)
                if r:
                    break
        return r

    if M != N - 1:
        return "NO"
    
    return "NO" if iscycle(edges, 1, set(), set()) else "YES"