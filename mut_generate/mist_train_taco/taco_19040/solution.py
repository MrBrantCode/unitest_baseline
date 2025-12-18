"""
QUESTION:
Victoria has a tree, $\mathbf{T}$, consisting of $N$ nodes numbered from $1$ to $N$. Each edge from node $U_i$ to $V_i$ in tree $\mathbf{T}$ has an integer weight, $W_i$.

Let's define the cost, $\mbox{C}$, of a path from some node $\mbox{X}$ to some other node $\mathbf{Y}$ as the maximum weight ($\mbox{w}$) for any edge in the unique path from node $\mbox{X}$ to node $\mathbf{Y}$.

Victoria wants your help processing $Q$ queries on tree $\mathbf{T}$, where each query contains $2$ integers, $\boldsymbol{\mbox{L}}$ and $\mbox{R}$, such that $L\leq R$. For each query, she wants to print the number of different paths in $\mathbf{T}$ that have a cost, $\mbox{C}$, in the inclusive range $[L,R]$.

It should be noted that path from some node $\mbox{X}$ to some other node $\mathbf{Y}$ is considered same as path from node $\mathbf{Y}$ to $\mbox{X}$ i.e $\{X,Y\}$ is same as $\{Y,X\}$. 

Input Format

The first line contains $2$ space-separated integers, $N$ (the number of nodes) and $Q$ (the number of queries), respectively. 

Each of the $N-1$ subsequent lines contain $3$ space-separated integers, $\mbox{U}$, $\mbox{V}$, and $\mbox{w}$, respectively, describing a bidirectional road between nodes $\mbox{U}$ and $\mbox{V}$ which has weight $\mbox{w}$. 

The $Q$ subsequent lines each contain $2$ space-separated integers denoting $\boldsymbol{\mbox{L}}$ and $\mbox{R}$.

Constraints

$1\leq N,Q\leq10^5$   
$1\leq U,V\leq N$   
$1\leq W\leq10^9$  
$1\leq L\leq R\leq10^9$ 

Scoring

$1\leq N,Q\leq10^3$ for $30\%$ of the test data.  
$1\leq N,Q\leq10^5$ for $\textbf{100\%}$ of the test data.

Output Format

For each of the $Q$ queries, print the number of paths in $\mathbf{T}$ having cost $\mbox{C}$ in the inclusive range $[L,R]$ on a new line.

Sample Input
5 5
1 2 3
1 4 2
2 5 6
3 4 1
1 1
1 2
2 3
2 5
1 6

Sample Output
1
3
5
5
10

Explanation

$Q_1$: $\{3,4\}$ 

$Q_2$: $\{1,3\},\{3,4\},\{1,4\}$ 

$Q_3$: $\{1,4\},\{1,2\},\{2,4\},\{1,3\},\{2,3\}$ 

$Q_4$: $\{1,4\},\{1,2\},\{2,4\},\{1,3\},\{2,3\}$ 

...etc.
"""

from collections import defaultdict
import bisect

def count_paths_in_cost_range(N, Q, edges, queries):
    weights = sorted(edges)
    
    class Node:
        def __init__(self, size, parent=None):
            self.size = size
            self.parent = parent
    
    clusters = {n: Node(1) for n in range(1, N + 1)}
    counts = defaultdict(int)
    
    for (W, U, V) in weights:
        u = clusters[U]
        v = clusters[V]
        while u.parent:
            u = u.parent
        while v.parent:
            v = v.parent
        counts[W] += u.size * v.size
        n = Node(u.size + v.size)
        u.parent = n
        v.parent = n
        clusters[U] = n
        clusters[V] = n
    
    K = sorted(counts)
    V = [counts[k] for k in K]
    Z = [0]
    t = 0
    for v in V:
        t += v
        Z.append(t)
    
    results = []
    for (L, R) in queries:
        x = bisect.bisect_left(K, L)
        y = bisect.bisect_right(K, R)
        results.append(Z[y] - Z[x])
    
    return results