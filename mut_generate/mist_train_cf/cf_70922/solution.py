"""
QUESTION:
You are given a 2D integer sequence `adjacentPairs` of size `n - 1` where each `adjacentPairs[i] = [ui, vi]` indicates that the elements `ui` and `vi` are immediate neighbors in the original sequence `nums`. `nums.length == n`, `2 <= n <= 10^5`, and `-10^5 <= nums[i], ui, vi <= 10^5`. Design a function `restoreArray` to reconstruct the original sequence `nums` and return the sequence along with the sum of all the elements in the sequence.
"""

from collections import defaultdict
def restoreArray(adjacentPairs):
    graph = defaultdict(list)
    for u, v in adjacentPairs:
        graph[u].append(v)
        graph[v].append(u)
    head = [u for u in graph if len(graph[u]) == 1][0]
    res, prev = [head], None
    while len(res) < len(adjacentPairs) + 1:
        for v in graph[res[-1]]:
            if v != prev:
                res.append(v)
                prev = res[-2]
    sum_res = sum(res)
    return res, sum_res