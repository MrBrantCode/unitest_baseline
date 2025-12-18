"""
QUESTION:
Implement a function named `depth_first_search` to perform a depth-first traversal of a graph or tree. The function should start at a given root node and return a list of visited nodes in the order they were visited. Assume the graph or tree is represented as an adjacency list, where each key is a node and its corresponding value is a list of its neighboring nodes.
"""

def depth_first_search(graph, root):
    visited = set()
    traversal_order = []
    
    def dfs(node):
        visited.add(node)
        traversal_order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(root)
    return traversal_order