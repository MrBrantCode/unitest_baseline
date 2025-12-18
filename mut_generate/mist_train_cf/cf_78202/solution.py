"""
QUESTION:
Implement a function `dfs_iterative` that performs a depth-first search on a graph. The function should take as input a dictionary representing the graph, where each key is a node and its corresponding value is a set of adjacent nodes, and a starting node. The function should return a set of visited nodes.
"""

def dfs_iterative(graph, start):
    stack, visited = [start], set()
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - set(visited)) 
            
    return visited