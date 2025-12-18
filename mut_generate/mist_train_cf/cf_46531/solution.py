"""
QUESTION:
Connect all N cities with the minimum cost while maximizing the efficiency of the connections. Each connection between two cities has a cost and an efficiency. Given a list of connections where each connection is a list of [city1, city2, cost, efficiency], return the minimum cost such that every pair of cities has a path of connections. If it's impossible to connect all cities, return -1. The total efficiency of the connections used should be maximized, which is the minimum efficiency among them. 

Note that 1 <= N <= 10000, 1 <= connections.length <= 10000, and each connection is valid (1 <= city1, city2 <= N, 0 <= cost <= 10^5, 1 <= efficiency <= 10^5).
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parent[px] = py


def maximumEfficiency(N, connections):
    connections.sort(key=lambda x: (-x[3], x[2]))
    dsu = DSU(N)
    cost, efficiency, count = 0, float('inf'), 0

    for u, v, c, e in connections:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            cost += c
            efficiency = min(efficiency, e)
            count += 1

    return cost if count == N - 1 else -1