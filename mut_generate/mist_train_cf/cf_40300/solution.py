"""
QUESTION:
Write a function `getHubs` that takes a graph represented as an adjacency list and returns a list of nodes that qualify as hubs based on their degree. The graph is represented as a dictionary where the keys are the nodes and the values are lists of adjacent nodes. The function should return a list of nodes with the highest degree. If multiple nodes have the same highest degree, all should be included in the list. If there are no hubs, the function should return an empty list.
"""

from typing import List, Dict

def getHubs(graph: Dict[str, List[str]]) -> List[str]:
    max_degree = 0
    hubs = []
    
    for node, neighbors in graph.items():
        degree = len(neighbors)
        if degree > max_degree:
            max_degree = degree
            hubs = [node]
        elif degree == max_degree:
            hubs.append(node)
    
    return hubs