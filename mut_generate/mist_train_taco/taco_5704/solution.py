"""
QUESTION:
You are given a weighted tree consisting of $n$ vertices. Recall that a tree is a connected graph without cycles. Vertices $u_i$ and $v_i$ are connected by an edge with weight $w_i$.

You are given $m$ queries. The $i$-th query is given as an integer $q_i$. In this query you need to calculate the number of pairs of vertices $(u, v)$ ($u < v$) such that the maximum weight of an edge on a simple path between $u$ and $v$ doesn't exceed $q_i$.


-----Input-----

The first line of the input contains two integers $n$ and $m$ ($1 \le n, m \le 2 \cdot 10^5$) — the number of vertices in the tree and the number of queries.

Each of the next $n - 1$ lines describes an edge of the tree. Edge $i$ is denoted by three integers $u_i$, $v_i$ and $w_i$ — the labels of vertices it connects ($1 \le u_i, v_i \le n$, $u_i \ne v_i$) and the weight of the edge ($1 \le w_i \le 2 \cdot 10^5$). It is guaranteed that the given edges form a tree.

The last line of the input contains $m$ integers $q_1, q_2, \dots, q_m$ ($1 \le q_i \le 2 \cdot 10^5$), where $q_i$ is the maximum weight of an edge in the $i$-th query.


-----Output-----

Print $m$ integers — the answers to the queries. The $i$-th value should be equal to the number of pairs of vertices $(u, v)$ ($u < v$) such that the maximum weight of an edge on a simple path between $u$ and $v$ doesn't exceed $q_i$.

Queries are numbered from $1$ to $m$ in the order of the input.


-----Examples-----
Input
7 5
1 2 1
3 2 3
2 4 1
4 5 2
5 7 4
3 6 2
5 2 3 4 1

Output
21 7 15 21 3 

Input
1 2
1 2

Output
0 0 

Input
3 3
1 2 1
2 3 2
1 3 2

Output
1 3 3 



-----Note-----

The picture shows the tree from the first example: [Image]
"""

def count_valid_pairs(n, m, edges, queries):
    par = [-1] * n

    def c(x):
        return x * (x - 1) // 2

    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                (x, y) = (y, x)
            par[x] += par[y]
            par[y] = x
            return True

    def same(x, y):
        return find(x) == find(y)

    def size(x):
        return -par[find(x)]

    import collections
    Edge = collections.defaultdict(list)
    for (u, v, w) in edges:
        Edge[w].append((u, v))

    q = max(queries)
    Ans = [0] * (q + 1)
    ans = 0

    for i in range(1, q + 1):
        for (u, v) in Edge[i]:
            if same(u - 1, v - 1):
                continue
            else:
                (uu, vv) = (size(u - 1), size(v - 1))
                unite(u - 1, v - 1)
                uv = size(u - 1)
                ans += c(uv) - c(uu) - c(vv)
        Ans[i] = ans

    Ans2 = []
    for q in queries:
        Ans2.append(Ans[q])

    return Ans2