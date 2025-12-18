"""
QUESTION:
Assign colors to the towns in a graph such that no two adjacent towns have the same color. The graph is represented as an adjacency list, where graph[i] contains the neighbors of vertex i. Implement a function assign_town_colors with the following signature:

assign_town_colors(graph: List[List[int]]) -> List[List[int]]

The function should return a list of lists, where each inner list represents a group of towns with the same color. If it's not possible to assign colors without adjacent towns having the same color, the function should return "Not possible to assign colors".
"""

from typing import List

def assign_town_colors(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    town_color = [-1] * n
    group = []

    def dfs(v, past, color):
        town_color[v] = color
        if len(group) <= color:
            group.append([v + 1])
        else:
            group[color].append(v + 1)
        for i in graph[v]:
            if i != past:
                if town_color[i] == -1:
                    dfs(i, v, 1 - color)
                elif town_color[i] == color:
                    return False
        return True

    for i in range(n):
        if town_color[i] == -1:
            if not dfs(i, -1, 0):
                return "Not possible to assign colors"
    return [g for g in group if g]