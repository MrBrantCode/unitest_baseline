"""
QUESTION:
Create a function named `cloneGraph` that takes a node from a connected undirected graph as input and returns a deep copy of the graph as a reference to the cloned node. The graph's nodes have an integer value 'val' and a list of neighboring nodes 'neighbors'. The node's value is unique and ranges from 1 to 100, the number of nodes does not exceed 100, and there are no repeated edges or self-loops in the graph. The graph is connected, allowing all nodes to be visited from the given node.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    visited = {}
    def dfs(node):
        if node in visited:
            return visited[node]
        copy = Node(node.val)
        visited[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node) if node else None