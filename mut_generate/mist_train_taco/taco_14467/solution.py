"""
QUESTION:
You are given a connected undirected weighted graph consisting of $n$ vertices and $m$ edges.

You need to print the $k$-th smallest shortest path in this graph (paths from the vertex to itself are not counted, paths from $i$ to $j$ and from $j$ to $i$ are counted as one).

More formally, if $d$ is the matrix of shortest paths, where $d_{i, j}$ is the length of the shortest path between vertices $i$ and $j$ ($1 \le i < j \le n$), then you need to print the $k$-th element in the sorted array consisting of all $d_{i, j}$, where $1 \le i < j \le n$.


-----Input-----

The first line of the input contains three integers $n, m$ and $k$ ($2 \le n \le 2 \cdot 10^5$, $n - 1 \le m \le \min\Big(\frac{n(n-1)}{2}, 2 \cdot 10^5\Big)$, $1 \le k \le \min\Big(\frac{n(n-1)}{2}, 400\Big)$ — the number of vertices in the graph, the number of edges in the graph and the value of $k$, correspondingly.

Then $m$ lines follow, each containing three integers $x$, $y$ and $w$ ($1 \le x, y \le n$, $1 \le w \le 10^9$, $x \ne y$) denoting an edge between vertices $x$ and $y$ of weight $w$.

It is guaranteed that the given graph is connected (there is a path between any pair of vertices), there are no self-loops (edges connecting the vertex with itself) and multiple edges (for each pair of vertices $x$ and $y$, there is at most one edge between this pair of vertices in the graph).


-----Output-----

Print one integer — the length of the $k$-th smallest shortest path in the given graph (paths from the vertex to itself are not counted, paths from $i$ to $j$ and from $j$ to $i$ are counted as one).


-----Examples-----
Input
6 10 5
2 5 1
5 3 9
6 2 2
1 3 1
5 1 8
6 5 10
1 6 5
6 4 6
3 6 2
3 4 5

Output
3

Input
7 15 18
2 6 3
5 7 4
6 5 4
3 6 9
6 7 7
1 6 4
7 1 6
7 2 1
4 3 2
3 2 8
5 3 6
2 5 5
3 7 9
4 1 8
2 1 1

Output
9
"""

def find_kth_smallest_shortest_path(n, m, k, edges):
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize a list to store the shortest paths
    shortest_paths = edges[:k] + [[0, 0, 10**20] for _ in range(k)]
    
    # Dictionary to store the shortest paths found
    path_dict = {}
    for (x, y, w) in edges:
        if x:
            path_dict[x * 10**6 + y] = w
    
    # Flag to indicate if any new shortest path was found
    flg = 1
    
    while flg:
        flg = 0
        for i in range(len(shortest_paths)):
            (x1, y1, w1) = shortest_paths[i]
            for j in range(i + 1, len(shortest_paths)):
                (x2, y2, w2) = shortest_paths[j]
                if x1 == x2:
                    (a, b) = (min(y1, y2), max(y1, y2))
                elif y1 == y2:
                    (a, b) = (min(x1, x2), max(x1, x2))
                elif x1 == y2:
                    (a, b) = (x2, y1)
                elif x2 == y1:
                    (a, b) = (x1, y2)
                else:
                    (a, b) = (0, 0)
                
                if a:
                    if (a * 10**6 + b in path_dict and w1 + w2 < path_dict[a * 10**6 + b]) or \
                       (a * 10**6 + b not in path_dict and w1 + w2 < shortest_paths[-1][2]):
                        if a * 10**6 + b in path_dict:
                            for k in range(len(shortest_paths)):
                                if shortest_paths[k][0] == a and shortest_paths[k][1] == b:
                                    shortest_paths[k][2] = w1 + w2
                        else:
                            (x, y, w) = shortest_paths.pop()
                            if x:
                                path_dict.pop(x * 10**6 + y)
                            shortest_paths.append([a, b, w1 + w2])
                        
                        path_dict[a * 10**6 + b] = w1 + w2
                        shortest_paths = sorted(shortest_paths, key=lambda x: x[2])
                        flg = 1
                        break
            if flg:
                break
    
    return shortest_paths[-1][2]