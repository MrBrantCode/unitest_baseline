"""
QUESTION:
Implement a function `dijkstra(graph, start, end, streets)` that uses Dijkstra's algorithm to find the shortest path between two points in a graph. 

The function should take as input a graph represented as a dictionary where each key is a vertex and its corresponding value is a list of tuples containing the neighboring vertex and the distance between them. 

The function should also take as input the starting and ending points of the path, represented as strings, and a list of tuples representing the streets that can be used, where each tuple contains two vertices that are connected by a street.

The function should return the shortest path as a string, with each vertex separated by an arrow. If no path is found, the function should return None.

The function should assume that the graph does not contain any negative-weight edges and that the streets list only contains valid edges from the graph.
"""

import heapq

def entrance(graph, start, end, streets):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    vertices_queue = [(0, start)]

    while vertices_queue:
        current_distance, current_vertex = heapq.heappop(vertices_queue)
        if current_vertex == end:
            path = []
            while current_vertex is not None:
                path.append(current_vertex)
                current_vertex = previous_vertices[current_vertex]
            return ' -> '.join(path[::-1])
        for neighbor, distance in graph[current_vertex]:
            if (current_vertex, neighbor) in streets or (neighbor, current_vertex) in streets:
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(vertices_queue, (new_distance, neighbor))
    return None