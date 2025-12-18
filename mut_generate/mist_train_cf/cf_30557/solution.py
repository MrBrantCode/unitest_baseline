"""
QUESTION:
Write a function `isBipartite(graph)` that determines if a given graph is bipartite. The graph is represented as an adjacency list, where the keys are the nodes and the values are lists of neighboring nodes. The function should return `True` if the graph is bipartite and `False` otherwise. A graph is bipartite if it can be colored using two colors such that no two adjacent nodes have the same color.
"""

from collections import deque

def isBipartite(graph):
    color = {}  
    q = deque()  

    for node in graph:
        if node not in color:  
            color[node] = 0  
            q.append(node)  

            while q:  
                cur = q.popleft()  
                for nei in graph[cur]:  
                    if nei not in color:  
                        color[nei] = 1 - color[cur]  
                        q.append(nei)  
                    elif color[nei] == color[cur]:  
                        return False  

    return True 