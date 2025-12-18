"""
QUESTION:
Write a function `gardenNoAdj(n, paths)` that takes the number of gardens `n` and a list of bidirectional paths `paths` as input, and returns a list where each element represents the type of flower planted in the corresponding garden, such that any two gardens connected by a path have different types of flowers. 

The number of gardens `n` is between 1 and 10^4, and the number of paths is between 0 and 2 * 10^4. Each garden has at most 4 paths coming into or leaving it, and the flower types are denoted 1, 2, 3, or 4. It is guaranteed that an answer exists.
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