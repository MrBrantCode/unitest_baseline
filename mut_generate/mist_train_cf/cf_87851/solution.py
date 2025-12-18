"""
QUESTION:
Write a function named `dfs` that takes in a graph represented as an adjacency list and a starting node, and returns a list of all nodes visited in a depth-first search starting from the given node. The graph can contain cycles, disconnected components, nodes with no outgoing edges, nodes with no incoming edges, and self-loops. The starting node will always be present in the graph. The function should not include any weights in the output.
"""

def dfs(graph, start_node):
    visited = set()  
    stack = [start_node]  

    while stack:
        node = stack.pop()  

        if node not in visited:
            visited.add(node)  
            neighbors = graph[node]  

            for neighbor in neighbors:
                stack.append(neighbor[0])  

    return list(visited)