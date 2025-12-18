"""
QUESTION:
Write a function `findJudge(N, trust)` that identifies the town judge in a town of `N` people based on a given array of trust relationships `trust`. If the town judge exists and can be identified, return the label of the town judge. Otherwise, return `-1`. Note that there is exactly one person that satisfies the properties of a town judge: the town judge trusts nobody, and everybody (except for the town judge) trusts the town judge. The function should work for `1 <= N <= 1000` and `0 <= trust.length <= 10^4`, where `trust[i].length == 2` and `trust[i]` are all different.
"""

def findJudge(N, trust):
    trust_counts = [0] * (N + 1)
    for a, b in trust:
        trust_counts[a] -= 1
        trust_counts[b] += 1
    for i in range(1, N + 1):
        if trust_counts[i] == N - 1:
            return i
    return -1