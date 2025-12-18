"""
QUESTION:
You are given a rooted tree, consisting of $n$ vertices. The vertices are numbered from $1$ to $n$, the root is the vertex $1$.

You can perform the following operation at most $k$ times:

choose an edge $(v, u)$ of the tree such that $v$ is a parent of $u$;

remove the edge $(v, u)$;

add an edge $(1, u)$ (i. e. make $u$ with its subtree a child of the root).

The height of a tree is the maximum depth of its vertices, and the depth of a vertex is the number of edges on the path from the root to it. For example, the depth of vertex $1$ is $0$, since it's the root, and the depth of all its children is $1$.

What's the smallest height of the tree that can be achieved?


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of testcases.

The first line of each testcase contains two integers $n$ and $k$ ($2 \le n \le 2 \cdot 10^5$; $0 \le k \le n - 1$) — the number of vertices in the tree and the maximum number of operations you can perform.

The second line contains $n-1$ integers $p_2, p_3, \dots, p_n$ ($1 \le p_i < i$) — the parent of the $i$-th vertex. Vertex $1$ is the root.

The sum of $n$ over all testcases doesn't exceed $2 \cdot 10^5$.


-----Output-----

For each testcase, print a single integer — the smallest height of the tree that can achieved by performing at most $k$ operations.


-----Examples-----

Input
5
5 1
1 1 2 2
5 2
1 1 2 2
6 0
1 2 3 4 5
6 1
1 2 3 4 5
4 3
1 1 1
Output
2
1
5
3
1


-----Note-----

None
"""

def find_min_tree_height(n, k, parents):
    def check(pars, dep, k):
        _oper = 0
        depths = [1 for _ in range(len(pars))]
        for i in range(len(pars) - 1, 0, -1):
            if depths[i] == dep and pars[i] != 0:
                _oper += 1
            else:
                par = pars[i]
                depths[par] = max(depths[par], depths[i] + 1)
        return _oper <= k

    pars = [0] + [p - 1 for p in parents]  # Adjusting parent indices to be 0-based
    low, high = 1, n - 1
    while low < high:
        mid = (low + high) // 2
        if check(pars, mid, k):
            high = mid
        else:
            low = mid + 1
    if check(pars, high, k):
        return high
    else:
        return high + 1