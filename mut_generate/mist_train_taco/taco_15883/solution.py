"""
QUESTION:
Recently, Pari and Arya did some research about NP-Hard problems and they found the minimum vertex cover problem very interesting.

Suppose the graph G is given. Subset A of its vertices is called a vertex cover of this graph, if for each edge uv there is at least one endpoint of it in this set, i.e. $u \in A$ or $v \in A$ (or both).

Pari and Arya have won a great undirected graph as an award in a team contest. Now they have to split it in two parts, but both of them want their parts of the graph to be a vertex cover.

They have agreed to give you their graph and you need to find two disjoint subsets of its vertices A and B, such that both A and B are vertex cover or claim it's impossible. Each vertex should be given to no more than one of the friends (or you can even keep it for yourself).


-----Input-----

The first line of the input contains two integers n and m (2 ≤ n ≤ 100 000, 1 ≤ m ≤ 100 000) — the number of vertices and the number of edges in the prize graph, respectively.

Each of the next m lines contains a pair of integers u_{i} and v_{i} (1  ≤  u_{i},  v_{i}  ≤  n), denoting an undirected edge between u_{i} and v_{i}. It's guaranteed the graph won't contain any self-loops or multiple edges.


-----Output-----

If it's impossible to split the graph between Pari and Arya as they expect, print "-1" (without quotes).

If there are two disjoint sets of vertices, such that both sets are vertex cover, print their descriptions. Each description must contain two lines. The first line contains a single integer k denoting the number of vertices in that vertex cover, and the second line contains k integers — the indices of vertices. Note that because of m ≥ 1, vertex cover cannot be empty.


-----Examples-----
Input
4 2
1 2
2 3

Output
1
2 
2
1 3 

Input
3 3
1 2
2 3
1 3

Output
-1



-----Note-----

In the first sample, you can give the vertex number 2 to Arya and vertices numbered 1 and 3 to Pari and keep vertex number 4 for yourself (or give it someone, if you wish).

In the second sample, there is no way to satisfy both Pari and Arya.
"""

from collections import defaultdict

def find_vertex_covers(n, m, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    
    v1 = []
    v2 = []
    mark = [-1] * (n + 1)

    def bfs(start):
        q = []
        q.append(start)
        mark[start] = 1
        v2.append(start)
        while q:
            v = q.pop(0)
            for u in g[v]:
                if mark[u] == -1:
                    mark[u] = 1 - mark[v]
                    q.append(u)
                    if mark[u] == 0:
                        v1.append(u)
                    else:
                        v2.append(u)
                elif mark[u] == mark[v]:
                    return -1
        return 0
    
    for i in range(1, n + 1):
        if mark[i] == -1 and len(g[i]):
            res = bfs(i)
            if res == -1:
                return -1
    
    return v1, v2