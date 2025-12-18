"""
QUESTION:
Write a function named `sort_nodes` that takes a dictionary representing a graph where keys indicate nodes and values represent lists of directly reachable nodes. The function should sort the list of reachable nodes for each key in lexicographical order and return a list of keys sorted by the count of their corresponding directly reachable nodes in descending order. In case of a tie, sort the keys based on their lexicographical order. The function should be done in one pass through the dictionary.
"""

def sort_nodes(graph):
    for node in graph:
        graph[node].sort()
    return sorted(graph, key=lambda node: (-len(graph[node]), node))