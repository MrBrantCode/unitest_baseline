"""
QUESTION:
Create a function called "breadthFirstSearch" that takes in a graph, a starting vertex, and a target vertex as inputs. The graph is a weighted graph where each edge has a different weight and may contain cycles and negative edge weights. The function should find and return the shortest path from the starting vertex to the target vertex. If there is no path or a negative cycle in the graph, the function should return an empty list.
"""

from collections import deque

def breadthFirstSearch(graph, start, target):
    queue = deque([start])
    visited = set()
    distances = {start: 0}
    previous = {}
    
    while queue:
        current = queue.popleft()
        if current == target:
            break
        visited.add(current)
        
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                new_distance = distances[current] + weight
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    queue.append(neighbor)
                    
    if target not in previous:
        return []
    
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = previous.get(current)
        
    return path