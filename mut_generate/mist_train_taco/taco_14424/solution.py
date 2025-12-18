"""
QUESTION:
Examples

Input

4 5 2
0 1 2 1
0 2 1 2
1 2 1 1
1 3 1 3
2 3 2 1


Output

6


Input




Output
"""

from collections import defaultdict
from heapq import *

def min_cost_flow(n, m, f, edges):
    class MinCostFlow:
        def __init__(self):
            self.inf = 10 ** 9
            self.to = defaultdict(dict)

        def add_edge(self, u, v, cap, cost):
            self.to[u][v] = [cap, cost]
            self.to[v][u] = [0, -cost]

        def cal(self, s, t, f):
            min_cost = 0
            pot = defaultdict(int)
            while f:
                dist = {}
                pre_u = {}
                hp = []
                heappush(hp, (0, s))
                dist[s] = 0
                while hp:
                    (d, u) = heappop(hp)
                    if d > dist[u]:
                        continue
                    for (v, [cap, cost]) in self.to[u].items():
                        if cap == 0:
                            continue
                        nd = dist[u] + cost + pot[u] - pot[v]
                        dist.setdefault(v, self.inf)
                        if nd >= dist[v]:
                            continue
                        dist[v] = nd
                        pre_u[v] = u
                        heappush(hp, (nd, v))
                if t not in dist:
                    return -1
                for (u, d) in dist.items():
                    pot[u] += d
                u = t
                min_cap = f
                while u != s:
                    (u, v) = (pre_u[u], u)
                    min_cap = min(min_cap, self.to[u][v][0])
                f -= min_cap
                min_cost += min_cap * pot[t]
                u = t
                while u != s:
                    (u, v) = (pre_u[u], u)
                    self.to[u][v][0] -= min_cap
                    self.to[v][u][0] += min_cap
            return min_cost

    mc = MinCostFlow()
    for (u, v, c, d) in edges:
        mc.add_edge(u, v, c, d)
    return mc.cal(0, n - 1, f)