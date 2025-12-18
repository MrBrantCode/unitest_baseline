"""
QUESTION:
Allison loves graph theory and just started learning about Minimum Spanning Trees(MST). She has three integers, $n$, $m$, and $\boldsymbol{\mathrm{~S~}}$, and uses them to construct a graph with the following properties:

The graph has $n$ nodes and $m$ undirected edges where each edge has a positive integer length.
No edge may directly connect a node to itself, and each pair of nodes can only be directly connected by at most one edge.
The graph is connected, meaning each node is reachable from any other node.
The value of the minimum spanning tree is $\boldsymbol{\mathrm{~S~}}$. Value of the MST is the sum of all the lengths of all edges of which are part of the tree.
The sum of the lengths of all edges is as small as possible.

For example, let's say $n=4$, $m=5$ and $s=4$. We need to construct a graph with $4$ nodes and $5$ edges. The value of minimum spanning tree must be $4$. The diagram belows shows a way to construct such a graph while keeping the lengths of all edges is as small as possible:

Here the sum of lengths of all edges is $7$.

Given $n$, $m$, and $\boldsymbol{\mathrm{~S~}}$ for $\mathrm{~g~}$ graphs satisfying the conditions above, find and print the minimum sum of the lengths of all the edges in each graph on a new line.

Note: It is guaranteed that, for all given combinations of $n$, $m$, and $\boldsymbol{\mathrm{~S~}}$, we can construct a valid graph.

Input Format

The first line contains an integer, $\mathrm{~g~}$, denoting the number of graphs. 

Each of the $\mathrm{~g~}$ subsequent lines contains three space-separated integers describing the respective values of $n$ (the number of nodes in the graph), $m$ (the number of edges in the graph), and $\boldsymbol{\mathrm{~S~}}$ (the value of the MST graph).

Constraints

For $20\%$ of the maximum score: 

$1$ $\leq$ $\mathrm{~g~}$ $\leq$ $100$
$2$ $\leq$ $n$ $\leq$ $10$
$1$ $\leq$ $m$ $\leq$ $50$
$1$ $\leq$ $\boldsymbol{\mathrm{~S~}}$ $\leq$ $\textbf{20}$

For $50\%$ of the maximum score: 

$1$ $\leq$ $\mathrm{~g~}$ $\leq$ $100$
$2$ $\leq$ $n$ $\leq$ $50$
$1$ $\leq$ $m$ $\leq$ $\textbf{2000}$
$1$ $\leq$ $\boldsymbol{\mathrm{~S~}}$ $\leq$ $\textbf{200}$

For $70\%$ of the maximum score: 

$1$ $\leq$ $\mathrm{~g~}$ $\leq$ $100$
$2$ $\leq$ $n$ $\leq$ $10^{5}$
$1$ $\leq$ $m$ $\leq$ $\mathbf{10}^{10}$
$1$ $\leq$ $\boldsymbol{\mathrm{~S~}}$ $\leq$ $10^{6}$

For $\textbf{100%}$ of the maximum score: 

$1$ $\leq$ $\mathrm{~g~}$ $\leq$ $\textbf{1000}$
$2$ $\leq$ $n$ $\leq$ $10^{8}$
$1$ $\leq$ $m$ $\leq$ $\mathbf{10}^{16}$
$1$ $\leq$ $\boldsymbol{\mathrm{~S~}}$ $\leq$ $\mathbf{10}^{10}$

Output Format

For each graph, print an integer on a new line denoting the minimum sum of the lengths of all edges in a graph satisfying the given conditions.

Sample Input
2
4 5 4
4 3 6

Sample Output
7
6

Explanation

Graph $1$:

The answer for this sample is already explained the problem statement.

Graph $2$:

We must construct a graph with $n=4$ nodes, $m=3$ edges, and an MST value of $s=6$. Recall that a connected graph with $n$ nodes and $n-1$ edges is already a tree, so the MST will contain all $m=3$ edges and the total length of all the edges of the graph will be equal to the value of the minimum spanning tree. So the answer is $\boldsymbol{6}$.
"""

def calculate_minimum_edge_sum(n, m, s):
    if m <= (n - 1) * (n - 2) // 2 + 1:
        return m + s - n + 1
    else:
        s -= n - 1
        e = m - (n - 1) * (n - 2) // 2
        mnc = (s + n - 2) // (n - 1)
        ans = 1e+42
        s -= mnc
        for A in [0, s // (n - 2), s // (n - 2) - 1]:
            for B in [0, n - 3, (s - A * (n - 2)) % (n - 2)]:
                x = A * (n - 2) + B
                if 0 <= x <= s:
                    ans = min(ans, (s - x + mnc) * e + (n - 1) * (n - 2) // 2 * A + B * (B - 1) // 2 + B * (n - B - 1))
        return ans + m