"""
QUESTION:
Ehab is interested in the bitwise-xor operation and the special graphs. Mahmoud gave him a problem that combines both. He has a complete graph consisting of n vertices numbered from 0 to n - 1. For all 0 ≤ u < v < n, vertex u and vertex v are connected with an undirected edge that has weight $u \oplus v$ (where $\oplus$ is the bitwise-xor operation). Can you find the weight of the minimum spanning tree of that graph?

You can read about complete graphs in https://en.wikipedia.org/wiki/Complete_graph

You can read about the minimum spanning tree in https://en.wikipedia.org/wiki/Minimum_spanning_tree

The weight of the minimum spanning tree is the sum of the weights on the edges included in it.


-----Input-----

The only line contains an integer n (2 ≤ n ≤ 10^12), the number of vertices in the graph.


-----Output-----

The only line contains an integer x, the weight of the graph's minimum spanning tree.


-----Example-----
Input
4

Output
4


-----Note-----

In the first sample: [Image] The weight of the minimum spanning tree is 1+2+1=4.
"""

def calculate_mst_weight(n: int) -> int:
    """
    Calculate the weight of the minimum spanning tree (MST) of a complete graph with n vertices.
    The graph has edges with weights defined by the bitwise-xor operation between vertex indices.

    Parameters:
    n (int): The number of vertices in the graph (2 ≤ n ≤ 10^12).

    Returns:
    int: The weight of the minimum spanning tree.
    """
    a = 0
    n -= 1  # Adjust n to be zero-indexed
    for i in range(40):
        k = 1 << i
        a += (n + k) // (k * 2) * k
    return a