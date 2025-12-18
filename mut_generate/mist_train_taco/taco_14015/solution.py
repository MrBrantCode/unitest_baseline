"""
QUESTION:
There are N integers written on a blackboard. The i-th integer is A_i.

Takahashi and Aoki will arrange these integers in a row, as follows:

* First, Takahashi will arrange the integers as he wishes.
* Then, Aoki will repeatedly swap two adjacent integers that are coprime, as many times as he wishes.



We will assume that Takahashi acts optimally so that the eventual sequence will be lexicographically as small as possible, and we will also assume that Aoki acts optimally so that the eventual sequence will be lexicographically as large as possible. Find the eventual sequence that will be produced.

Constraints

* 1 ≦ N ≦ 2000
* 1 ≦ A_i ≦ 10^8

Input

The input is given from Standard Input in the following format:


N
A_1 A_2 … A_N


Output

Print the eventual sequence that will be produced, in a line.

Examples

Input

5
1 2 3 4 5


Output

5 3 2 4 1


Input

4
2 3 4 6


Output

2 4 6 3
"""

import sys
sys.setrecursionlimit(1000000000)

def gcd(a: int, b: int):
    while b:
        (a, b) = (b, a % b)
    return a

def merge(a, us, vs):
    (i, j, res) = (0, 0, [])
    while i < len(us) and j < len(vs):
        if a[us[i]] >= a[vs[j]]:
            res.append(us[i])
            i += 1
        else:
            res.append(vs[j])
            j += 1
    return res + us[i:] + vs[j:]

def dfs(g, a, u, vis):
    vis[u] = True
    res = []
    for v in g[u]:
        if not vis[v]:
            res = merge(a, res, dfs(g, a, v, vis))
    return [u] + res

def find_eventual_sequence(N, A):
    a = sorted(A)
    g = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if gcd(a[i], a[j]) != 1:
                g[i].append(j)
                g[j].append(i)
    vis = [False] * N
    res = []
    for u in range(N):
        if not vis[u]:
            res = merge(a, res, dfs(g, a, u, vis))
    return [a[u] for u in res]