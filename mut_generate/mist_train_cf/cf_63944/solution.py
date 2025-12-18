"""
QUESTION:
Given an array `stones` of length `n` where `stones[i] = [xi, yi]` represents the location of the `ith` stone on a 2D plane, implement a function `removeStones` that returns the largest possible number of stones that can be removed. A stone can be removed if it shares either the same row or the same column as another stone that has not been removed. The removal of stones must follow a specific order: the stone with the highest x-coordinate should be removed first, and if there are multiple stones with the same x-coordinate, then the stone with the highest y-coordinate should be removed first.

Constraints: `1 <= stones.length <= 1000`, `0 <= xi, yi <= 10^4`, and no two stones are at the same coordinate point.
"""

from collections import defaultdict

class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

def removeStones(stones):
    N = len(stones)
    dsu = DSU(20000)  # the maximum value of xi or yi (as given in constraints)
    for x, y in stones:
        dsu.union(x, y + 10000)  # we add 10000 to distinguish between x and y

    groups = defaultdict(int)
    for x, y in stones:
        groups[dsu.find(x)] += 1

    return N - len(groups)