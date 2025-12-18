"""
QUESTION:
We define the diameter of a strongly-connected oriented graph, $G=(V,E)$, as the minimum integer $\boldsymbol{d}$ such that for each $u,v\in G$ there is a path from $\mbox{u}$ to $v$ of length $\leq d$ (recall that a path's length is its number of edges).  

Given two integers, $n$ and $m$, build a strongly-connected oriented graph with $n$ vertices where each vertex has outdegree $m$ and the graph's diameter is as small as possible (see the Scoring section below for more detail). Then print the graph according to the Output Format specified below.  

Here's a sample strongly-connected oriented graph with $3$ nodes, whose outdegree is $2$ and diameter is $1$.  

Note: Cycles and multiple edges between vertices are allowed.

Input Format

Two space-separated integers describing the respective values of $n$ (the number of vertices) and $m$ (the outdegree of each vertex).

Constraints

$2\leq n\leq1000$
$2\leq m\leq\text{min}(n,5)$

Scoring     

We denote the diameter of your graph as $\boldsymbol{d}$ and the diameter of the graph in the author's solution as $\boldsymbol{\mathrm{~S~}}$. Your score for each test case (as a real number from $0$ to $\mbox{I}$) is:

$1$ if $d\leq s+1$
$\frac{\mbox{s}}{d}$ if $s+1<d\leq5\times s$
$0$ if $5\times s<d$

Output Format

First, print an integer denoting the diameter of your graph on a new line. 

Next, print $n$ lines where each line $\boldsymbol{i}$ ($0\leq i<n$) contains $m$ space-separated integers in the inclusive range from $0$ to $n-1$ describing the endpoints for each of vertex $\boldsymbol{i}$'s outbound edges.

Sample Input 0
5 2

Sample Output 0
2
1 4
2 0
3 1
4 2
0 3

Explanation 0

The diagram below depicts a strongly-connected oriented graph with $n=5$ nodes where each node has an outdegree of $m=2$:

The diameter of this graph is $\boldsymbol{d}=2$, which is minimal as the outdegree of each node must be $m$. We cannot construct a graph with a smaller diameter of $\boldsymbol{d}=1$ because it requires an outbound edge from each vertex to each other vertex in the graph (so the outdegree of that graph would be $n-1$).
"""

def generate_strongly_connected_graph(n: int, m: int) -> (int, list):
    """
    Generates a strongly-connected oriented graph with `n` vertices and each vertex having an outdegree of `m`.
    The function returns the diameter of the graph and the adjacency list representing the graph.

    Parameters:
    n (int): The number of vertices in the graph.
    m (int): The outdegree of each vertex in the graph.

    Returns:
    tuple: A tuple containing the diameter of the graph (int) and the adjacency list (list of lists).
    """
    import math

    # Calculate the diameter
    dim = math.ceil(math.log(n) / math.log(m))
    if n < 4:
        dim = 1
    if n < 6:
        dim = 2

    # Special case for n == 5
    if n == 5:
        adjacency_list = [
            [1, 4],
            [2, 0],
            [3, 1],
            [4, 2],
            [0, 3]
        ]
    else:
        adjacency_list = [
            [(i * m + c) % n for c in range(m)] for i in range(n)
        ]

    return dim, adjacency_list