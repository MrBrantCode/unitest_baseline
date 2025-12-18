"""
QUESTION:
Vasya has a graph containing both directed (oriented) and undirected (non-oriented) edges. There can be multiple edges between a pair of vertices.

Vasya has picked a vertex s from the graph. Now Vasya wants to create two separate plans:

  to orient each undirected edge in one of two possible directions to maximize number of vertices reachable from vertex s;  to orient each undirected edge in one of two possible directions to minimize number of vertices reachable from vertex s. 

In each of two plans each undirected edge must become directed. For an edge chosen directions can differ in two plans.

Help Vasya find the plans.


-----Input-----

The first line contains three integers n, m and s (2 ≤ n ≤ 3·10^5, 1 ≤ m ≤ 3·10^5, 1 ≤ s ≤ n) — number of vertices and edges in the graph, and the vertex Vasya has picked.

The following m lines contain information about the graph edges. Each line contains three integers t_{i}, u_{i} and v_{i} (1 ≤ t_{i} ≤ 2, 1 ≤ u_{i}, v_{i} ≤ n, u_{i} ≠ v_{i}) — edge type and vertices connected by the edge. If t_{i} = 1 then the edge is directed and goes from the vertex u_{i} to the vertex v_{i}. If t_{i} = 2 then the edge is undirected and it connects the vertices u_{i} and v_{i}.

It is guaranteed that there is at least one undirected edge in the graph.


-----Output-----

The first two lines should describe the plan which maximizes the number of reachable vertices. The lines three and four should describe the plan which minimizes the number of reachable vertices.

A description of each plan should start with a line containing the number of reachable vertices. The second line of a plan should consist of f symbols '+' and '-', where f is the number of undirected edges in the initial graph. Print '+' as the j-th symbol of the string if the j-th undirected edge (u, v) from the input should be oriented from u to v. Print '-' to signify the opposite direction (from v to u). Consider undirected edges to be numbered in the same order they are given in the input.

If there are multiple solutions, print any of them.


-----Examples-----
Input
2 2 1
1 1 2
2 2 1

Output
2
-
2
+

Input
6 6 3
2 2 6
1 4 5
2 3 4
1 4 1
1 3 1
2 2 3

Output
6
++-
2
+-+
"""

def plan_reachable_vertices(n, m, s, edges):
    def dfs(x, flag=1):
        s, vis, ans = [x], [0] * n, ['+'] * m
        vis[x] = 1
        while s:
            i = s.pop()
            for j, k in graph[i]:
                if vis[j] == 0:
                    if k * flag < 0:
                        ans[abs(k) - 1] = '-'
                    elif k * flag > 0:
                        ans[abs(k) - 1] = '+'
                    if flag == 1 or k == 0:
                        s.append(j)
                        vis[j] = 1
        return ''.join(ans), sum(vis)

    graph = [[] for _ in range(n)]
    k = 1
    for z, x, y in edges:
        x, y = x - 1, y - 1
        if z == 1:
            graph[x].append((y, 0))
        else:
            graph[x].append((y, k))
            graph[y].append((x, -k))
            k += 1
    m = k - 1

    max_plan = dfs(s - 1, 1)
    min_plan = dfs(s - 1, -1)

    return max_plan, min_plan