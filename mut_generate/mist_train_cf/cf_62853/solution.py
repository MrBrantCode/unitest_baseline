"""
QUESTION:
You are tasked with creating a function `count_pairs_of_nodes` that takes three parameters: `n`, `edges`, and `queries`. The function should return an array `answers` where `answers[j]` is the count of pairs of nodes `(a, b)` that meet the criteria `a < b` and `cnt > queries[j]`, where `cnt` is the maximum count of edges incident to either `a` or `b`. The input parameters have the following constraints: `2 <= n < 2 * 10^4`, `1 <= edges.length < 10^5`, `1 <= ui, vi <= n`, `ui != vi`, `1 <= queries.length <= 20`, and `0 <= queries[j] < edges.length`.
"""

from bisect import bisect_right

def count_pairs_of_nodes(n, edges, queries):
    d = [0] * (n + 1)
    for u, v in edges:
        d[u] += 1
        d[v] += 1
    ds = sorted(d[1:])
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + ds[i]
    max_degrees = [max(d[u], d[v]) for u, v in edges]
    max_degrees.sort()
    res = []
    for q in queries:
        pos = bisect_right(ds, q)
        pos2 = bisect_right(max_degrees, q)
        ans = (n - pos) * n - pos * (pos - 1) // 2 + sum(max_degrees) - sum(max_degrees[:pos2])
        res.append(ans)
    return res