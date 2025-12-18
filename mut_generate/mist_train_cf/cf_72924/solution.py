"""
QUESTION:
Given two integer arrays `source` and `target` of length `n`, and an array `allowedSwaps` where each `allowedSwaps[i] = [ai, bi]` indicates that elements at index `ai` and `bi` of array `source` can be swapped, find the minimum Manhattan distance of `source` and `target` after any amount of swap operations on array `source`.

Constraints: `n == source.length == target.length`, `1 <= n <= 10^5`, `1 <= source[i], target[i] <= 10^5`, `0 <= allowedSwaps.length <= 10^5`, `allowedSwaps[i].length == 2`, `0 <= ai, bi <= n - 1`, `ai != bi`.

Implement the function `minimumHammingDistance(source, target, allowedSwaps)` to return the minimum Manhattan distance.
"""

from collections import defaultdict, Counter

def minimumHammingDistance(source, target, allowedSwaps):
    n = len(source)
    graph = defaultdict(list)
    for u, v in allowedSwaps:
        graph[u].append(v)
        graph[v].append(u)
    visited = [0]*n
    ans = 0
    # Depth-first search
    def dfs(i):
        visited[i] = 1
        nodes.append(i)
        for j in graph[i]:
            if not visited[j]: dfs(j)
    for i in range(n):
        if not visited[i]:
            nodes = []
            dfs(i)
            # cancel out the differences between the source and target
            s = Counter(source[j] for j in nodes)
            t = Counter(target[j] for j in nodes)
            ans += sum((s - t).values())  # remaining differences
    return ans