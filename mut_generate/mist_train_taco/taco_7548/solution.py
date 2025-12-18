"""
QUESTION:
You are given a tree consisting of $n$ vertices. A number is written on each vertex; the number on vertex $i$ is equal to $a_i$.

Recall that a simple path is a path that visits each vertex at most once. Let the weight of the path be the bitwise XOR of the values written on vertices it consists of. Let's say that a tree is good if no simple path has weight $0$.

You can apply the following operation any number of times (possibly, zero): select a vertex of the tree and replace the value written on it with an arbitrary positive integer. What is the minimum number of times you have to apply this operation in order to make the tree good?


-----Input-----

The first line contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of vertices.

The second line contains $n$ integers $a_1$, $a_2$, ..., $a_n$ ($1 \le a_i < 2^{30}$) — the numbers written on vertices.

Then $n - 1$ lines follow, each containing two integers $x$ and $y$ ($1 \le x, y \le n; x \ne y$) denoting an edge connecting vertex $x$ with vertex $y$. It is guaranteed that these edges form a tree.


-----Output-----

Print a single integer — the minimum number of times you have to apply the operation in order to make the tree good.


-----Examples-----

Input
6
3 2 1 3 2 1
4 5
3 4
1 4
2 1
6 1
Output
2
Input
4
2 1 1 1
1 2
1 3
1 4
Output
0
Input
5
2 2 2 2 2
1 2
2 3
3 4
4 5
Output
2


-----Note-----

In the first example, it is enough to replace the value on the vertex $1$ with $13$, and the value on the vertex $4$ with $42$.
"""

from collections import defaultdict

def min_operations_to_make_tree_good(n, a, edges):
    G = [[] for _ in range(n)]
    for x, y in edges:
        G[x - 1].append(y - 1)
        G[y - 1].append(x - 1)
    
    B = [0] * n
    vals = defaultdict(set)
    res = [0]

    def fill_dfs(v, p):
        B[v] = a[v]
        if p != -1:
            B[v] ^= B[p]
        for u in G[v]:
            if u != p:
                fill_dfs(u, v)

    def calc_dfs(v, p):
        zero = False
        vals[v].add(B[v])
        for u in G[v]:
            if u != p:
                calc_dfs(u, v)
                if len(vals[v]) < len(vals[u]):
                    (vals[v], vals[u]) = (vals[u], vals[v])
                for x in vals[u]:
                    zero |= x ^ a[v] in vals[v]
                for x in vals[u]:
                    vals[v].add(x)
                vals[u].clear()
        if zero:
            res[0] += 1
            vals[v].clear()
    
    fill_dfs(0, -1)
    calc_dfs(0, -1)
    return res[0]