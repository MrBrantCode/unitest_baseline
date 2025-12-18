"""
QUESTION:
Given a non-directed, interconnected tree structure with N nodes (each assigned a unique label from 0 to N-1) and N-1 edges, write a function `sumOfDistancesInTree(N, edges)` that generates a list where each element at index i represents the cumulative sum of the distances between node i and all other nodes in the tree. The input edges is a list of pairs, where each pair represents a connection between two nodes. The function should run in linear time complexity and space complexity.
"""

import collections

def sumOfDistancesInTree(N, edges):
    graph = collections.defaultdict(set)
    answer = [0] * N
    count = [1] * N

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    def dfs(node = 0, parent = None):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                answer[node] += answer[child] + count[child]

    def dfs2(node = 0, parent = None):
        for child in graph[node]:
            if child != parent:
                answer[child] = answer[node] - count[child] + N - count[child]
                dfs2(child, node)

    dfs()
    dfs2()

    return answer