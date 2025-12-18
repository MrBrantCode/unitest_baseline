"""
QUESTION:
Depth-first search (DFS) follows the strategy to search ”deeper” in the graph whenever possible. In DFS, edges are recursively explored out of the most recently discovered vertex $v$ that still has unexplored edges leaving it. When all of $v$'s edges have been explored, the search ”backtracks” to explore edges leaving the vertex from which $v$ was discovered.

This process continues until all the vertices that are reachable from the original source vertex have been discovered. If any undiscovered vertices remain, then one of them is selected as a new source and the search is repeated from that source.

DFS timestamps each vertex as follows:

* $d[v]$ records when $v$ is first discovered.
* $f[v]$ records when the search finishes examining $v$’s adjacency list.



Write a program which reads a directed graph $G = (V, E)$ and demonstrates DFS on the graph based on the following rules:

* $G$ is given in an adjacency-list. Vertices are identified by IDs $1, 2,... n$ respectively.
* IDs in the adjacency list are arranged in ascending order.
* The program should report the discover time and the finish time for each vertex.
* When there are several candidates to visit during DFS, the algorithm should select the vertex with the smallest ID.
* The timestamp starts with 1.

Constraints

* $1 \leq n \leq 100$

Input

In the first line, an integer $n$ denoting the number of vertices of $G$ is given. In the next $n$ lines, adjacency lists of $u$ are given in the following format:

$u$ $k$ $v_1$ $v_2$ ... $v_k$

$u$ is ID of the vertex and $k$ denotes its degree. $v_i$ are IDs of vertices adjacent to $u$.

Output

For each vertex, print $id$, $d$ and $f$ separated by a space character in a line. $id$ is ID of the vertex, $d$ and $f$ is the discover time and the finish time respectively. Print in order of vertex IDs.

Examples

Input

4
1 1 2
2 1 4
3 0
4 1 3


Output

1 1 8
2 2 7
3 4 5
4 3 6


Input

6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0


Output

1 1 12
2 2 11
3 3 8
4 9 10
5 4 7
6 5 6
"""

def depth_first_search(n, adj_list):
    # Initialize the state and timestamp variables
    sndf = [[False, i] for i in range(n + 1)]
    tt = 0

    def dfs(u):
        nonlocal tt
        sndf[u][0] = True
        tt += 1
        sndf[u].append(tt)
        for v in adj_list[u]:
            if not sndf[v][0]:
                dfs(v)
        tt += 1
        sndf[u].append(tt)

    # Perform DFS for each unvisited vertex
    for i in range(1, n + 1):
        if not sndf[i][0]:
            dfs(i)

    # Extract the results in the required format
    result = [(sndf[i][1], sndf[i][2], sndf[i][3]) for i in range(1, n + 1)]
    return result