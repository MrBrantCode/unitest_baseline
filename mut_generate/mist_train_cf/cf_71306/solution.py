"""
QUESTION:
Given a list of entities with unique quietness levels `quiet` of length `N` and a list of pairs `richer` where `richer[i] = [x, y]` indicates that entity `x` has more wealth than entity `y`, write a function `loudAndRich` that returns a list `answer` of length `N` where `answer[x]` is the index of the entity that is at least as wealthy as entity `x` and has the smallest quietness level.

The function should take two parameters: `richer` and `quiet`. The function should return the list `answer`.

Restrictions:
- `1 <= quiet.length = N <= 500`
- `0 <= quiet[i] < N`, all `quiet[i]` are unique.
- `0 <= richer.length <= N * (N-1) / 2`
- `0 <= richer[i][j] < N`
- `richer[i][0] != richer[i][1]`
- `richer[i]`'s are all unique.
- The observations in `richer` are all logically consistent.
"""

def loudAndRich(richer, quiet):
    n = len(quiet)
    richer2 = [[] for _ in range(n)]
    answer = [-1]*n
    quietest = list(range(n))

    for x, y in richer:
        richer2[y].append(x)

    def dfs(p):
        if answer[p] != -1:
            return
        minQuiet = quietest[p]
        for x in richer2[p]:
            dfs(x)
            if quiet[answer[x]] < quiet[minQuiet]:
                minQuiet = answer[x]
        answer[p] = minQuiet
        quietest[p] = minQuiet

    for p in range(n):
        dfs(p)
    return answer