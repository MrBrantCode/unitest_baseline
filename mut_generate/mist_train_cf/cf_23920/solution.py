"""
QUESTION:
Implement the `bfs` function to perform a breadth-first search traversal on a graph. The function should take as input a graph represented as an adjacency list and a source node, and return a dictionary where the keys are the nodes in the graph and the values are their respective predecessors. Assume that the graph is represented as a dictionary where the keys are the nodes and the values are lists of adjacent nodes. The function should not take any additional inputs or outputs.
"""

from collections import deque

def bfs(graph, source):
    """
    Performs a breadth-first search traversal on a graph and returns a dictionary 
    where the keys are the nodes in the graph and the values are their respective 
    predecessors.

    Args:
        graph (dict): A graph represented as an adjacency list.
        source (node): The source node.

    Returns:
        dict: A dictionary where the keys are the nodes in the graph and the values 
        are their respective predecessors.
    """
    predecessors = {source: None}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in graph.get(u, []):
            if v not in predecessors:
                predecessors[v] = u
                queue.append(v)

    return predecessors