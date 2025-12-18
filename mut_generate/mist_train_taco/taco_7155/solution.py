"""
QUESTION:
Chouti was tired of the tedious homework, so he opened up an old programming problem he created years ago.

You are given a connected undirected graph with $n$ vertices and $m$ weighted edges. There are $k$ special vertices: $x_1, x_2, \ldots, x_k$.

Let's define the cost of the path as the maximum weight of the edges in it. And the distance between two vertexes as the minimum cost of the paths connecting them.

For each special vertex, find another special vertex which is farthest from it (in terms of the previous paragraph, i.e. the corresponding distance is maximum possible) and output the distance between them.

The original constraints are really small so he thought the problem was boring. Now, he raises the constraints and hopes you can solve it for him.


-----Input-----

The first line contains three integers $n$, $m$ and $k$ ($2 \leq k \leq n \leq 10^5$, $n-1 \leq m \leq 10^5$) — the number of vertices, the number of edges and the number of special vertices.

The second line contains $k$ distinct integers $x_1, x_2, \ldots, x_k$ ($1 \leq x_i \leq n$).

Each of the following $m$ lines contains three integers $u$, $v$ and $w$ ($1 \leq u,v \leq n, 1 \leq w \leq 10^9$), denoting there is an edge between $u$ and $v$ of weight $w$. The given graph is undirected, so an edge $(u, v)$ can be used in the both directions.

The graph may have multiple edges and self-loops.

It is guaranteed, that the graph is connected.


-----Output-----

The first and only line should contain $k$ integers. The $i$-th integer is the distance between $x_i$ and the farthest special vertex from it.


-----Examples-----
Input
2 3 2
2 1
1 2 3
1 2 2
2 2 1

Output
2 2 

Input
4 5 3
1 2 3
1 2 5
4 2 1
2 3 2
1 4 4
1 3 3

Output
3 3 3 



-----Note-----

In the first example, the distance between vertex $1$ and $2$ equals to $2$ because one can walk through the edge of weight $2$ connecting them. So the distance to the farthest node for both $1$ and $2$ equals to $2$.

In the second example, one can find that distance between $1$ and $2$, distance between $1$ and $3$ are both $3$ and the distance between $2$ and $3$ is $2$.

The graph may have multiple edges between and self-loops, as in the first example.
"""

def find_farthest_special_vertex_distances(n, m, k, special_vertices, edges):
    # Convert special vertices to zero-indexed
    special_vertices = [v - 1 for v in special_vertices]
    
    # Create adjacency list
    adjacency_list = [[] for _ in range(n)]
    max_dist = 0
    for (u, v, w) in edges:
        adjacency_list[u - 1].append((v - 1, w))
        adjacency_list[v - 1].append((u - 1, w))
        if w > max_dist:
            max_dist = w
    
    # Binary search to find the minimum maximum distance
    l = 0
    r = max_dist + 1
    while l < r:
        mid = (l + r) // 2
        is_visited = [False] * n
        dfs_stack = [special_vertices[0]]
        is_visited[special_vertices[0]] = True
        
        while dfs_stack:
            cur_vertex = dfs_stack.pop()
            for (elem, dist) in adjacency_list[cur_vertex]:
                if not is_visited[elem] and dist <= mid:
                    is_visited[elem] = True
                    dfs_stack.append(elem)
        
        all_visited = all(is_visited[v] for v in special_vertices)
        
        if all_visited:
            r = mid
        else:
            l = mid + 1
    
    # Return the result as a list of distances
    return [l] * k