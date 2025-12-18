"""
QUESTION:
You are given $n$ colored segments on the number line. Each segment is either colored red or blue. The $i$-th segment can be represented by a tuple $(c_i, l_i, r_i)$. The segment contains all the points in the range $[l_i, r_i]$, inclusive, and its color denoted by $c_i$:

if $c_i = 0$, it is a red segment;

if $c_i = 1$, it is a blue segment.

We say that two segments of different colors are connected, if they share at least one common point. Two segments belong to the same group, if they are either connected directly, or through a sequence of directly connected segments. Find the number of groups of segments.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^5$). Description of the test cases follows.

The first line of each test case contains a single integer $n$ ($1 \leq n \leq 10^5$) — the number of segments.

Each of the next $n$ lines contains three integers $c_i, l_i, r_i$ ($0 \leq c_i \leq 1, 0 \leq l_i \leq r_i \leq 10^9$), describing the $i$-th segment.

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^5$.


-----Output-----

For each test case, print a single integer $k$, the number of groups of segments.


-----Examples-----

Input
2
5
0 0 5
1 2 12
0 4 7
1 9 16
0 13 19
3
1 0 1
1 1 2
0 3 4
Output
2
3


-----Note-----

In the first example there are $5$ segments. The segments $1$ and $2$ are connected, because they are of different colors and share a point. Also, the segments $2$ and $3$ are connected, and so are segments $4$ and $5$. Thus, there are two groups: one containing segments $\{1, 2, 3\}$, and the other one containing segments $\{4, 5\}$.
"""

def count_segment_groups(n, segments):
    # Add an index to each segment for tracking purposes
    segs = [(c, l, r, i) for i, (c, l, r) in enumerate(segments)]
    segs.sort(key=lambda x: x[1])  # Sort segments by their left endpoint
    par = [-1] * n  # Parent array for union-find
    cnt_comp = n  # Number of components (initially each segment is its own component)

    def find_set(u):
        p = u
        while par[p] >= 0:
            p = par[p]
        while u != p:
            t = par[u]
            par[u] = p
            u = t
        return p

    def join(u, v):
        nonlocal cnt_comp
        nonlocal par
        u = find_set(u)
        v = find_set(v)
        if u == v:
            return
        if -par[u] < -par[v]:
            (u, v) = (v, u)
        par[u] += par[v]
        par[v] = u
        cnt_comp -= 1

    hp = [[], []]  # Heaps for red and blue segments
    for (col, l, r, id) in segs:
        for elm in hp[1 - col]:
            if elm[0] < l:
                continue
            join(elm[1], id)
        if len(hp[1 - col]):
            hp[1 - col] = [max(hp[1 - col])]
        hp[col].append((r, id))

    return cnt_comp