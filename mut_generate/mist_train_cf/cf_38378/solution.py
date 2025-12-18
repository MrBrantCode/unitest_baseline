"""
QUESTION:
Implement a function `possible_to_split(dislikes: List[List[int]]) -> bool` that determines if it is possible to split a group into two smaller groups such that no two people in the same group dislike each other. The input `dislikes` is a list of pairs of integers representing the dislikes between people, where [u, v] denotes that person u dislikes person v. The integers u and v are in the range [1, N], where N is the total number of people, and the length of the list is in the range [1, 2000].
"""

from typing import List

def possible_to_split(dislikes: List[List[int]]) -> bool:
    graph = {}
    for u, v in dislikes:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)

    color = {}

    def dfs(node, c=0):
        if node in color:
            return color[node] == c
        color[node] = c
        return all(dfs(nei, c ^ 1) for nei in graph[node])

    return all(dfs(node) for node in graph if node not in color)