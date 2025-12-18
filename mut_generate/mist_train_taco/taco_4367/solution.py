"""
QUESTION:
You are given an integer N. Build an undirected graph with N vertices with indices 1 to N that satisfies the following two conditions:

* The graph is simple and connected.
* There exists an integer S such that, for every vertex, the sum of the indices of the vertices adjacent to that vertex is S.



It can be proved that at least one such graph exists under the constraints of this problem.

Constraints

* All values in input are integers.
* 3 \leq N \leq 100

Input

Input is given from Standard Input in the following format:


N


Output

In the first line, print the number of edges, M, in the graph you made. In the i-th of the following M lines, print two integers a_i and b_i, representing the endpoints of the i-th edge.

The output will be judged correct if the graph satisfies the conditions.

Example

Input

3


Output

2
1 3
2 3
"""

def generate_graph_edges(N: int) -> list:
    """
    Generates an undirected graph with N vertices that satisfies the given conditions.

    Parameters:
    N (int): The number of vertices in the graph.

    Returns:
    list: A list of tuples representing the edges of the graph.
    """
    M = N * (N - 1) // 2 - N // 2
    edges = []
    
    if N % 2 == 0:
        rem = N + 1
    else:
        rem = N
    
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if i + j != rem:
                edges.append((i, j))
    
    return edges