"""
QUESTION:
Given a number of gardens `n` and a list of bidirectional paths between gardens `paths`, plant one of 4 types of flowers in each garden such that any two connected gardens have different types of flowers and no three connected gardens in a triangle have the same sequence of flower types. Return a list `answer` where `answer[i]` is the type of flower in the `(i+1)th` garden.

Constraints: `1 <= n <= 10^4`, `0 <= paths.length <= 2 * 10^4`, `1 <= xi, yi <= n`, `xi != yi`, and every garden has at most 3 paths.
"""

def gardenNoAdj(n, paths):
    G = [[] for i in range(n)]
    res = [0] * n
    for x, y in paths:
        G[x-1].append(y-1)
        G[y-1].append(x-1)
    for i in range(n):
        res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
    return res