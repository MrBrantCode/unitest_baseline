"""
QUESTION:
Implement a function `dijkstra(graph, start, end, streets)` that uses Dijkstra's algorithm to find the shortest path between two points in a graph. The graph is represented as a dictionary of vertices and their neighbors, where each neighbor is represented as a tuple containing the neighbor vertex and the distance between them. The function should only consider streets that are in the `streets` list, which contains tuples representing the allowed streets. The function should return the shortest path as a string, with each vertex separated by an arrow. If no path is found, the function should return `None`.
"""

import heapq

def entrance(graph, start, end, streets):
    # create a dictionary to store the distance to each vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    # create a dictionary to store the previous vertex in the shortest path
    previous_vertices = {vertex: None for vertex in graph}
    # create a priority queue to store the vertices to visit
    vertices_queue = [(0, start)]
    # loop through the priority queue until it is empty
    while vertices_queue:
        # get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(vertices_queue)
        # check if we have reached the end vertex
        if current_vertex == end:
            # create a list to store the shortest path
            path = []
            # loop through the previous vertices until we reach the start vertex
            while current_vertex is not None:
                path.append(current_vertex)
                current_vertex = previous_vertices[current_vertex]
            # reverse the path and return it as a string
            return ' -> '.join(path[::-1])
        # loop through the neighbors of the current vertex
        for neighbor, distance in graph[current_vertex]:
            # check if the neighbor is on a street that can be used
            if (current_vertex, neighbor) in streets or (neighbor, current_vertex) in streets:
                # calculate the distance to the neighbor
                new_distance = current_distance + distance
                # check if the new distance is smaller than the current distance
                if new_distance < distances[neighbor]:
                    # update the distance to the neighbor
                    distances[neighbor] = new_distance
                    # update the previous vertex in the shortest path
                    previous_vertices[neighbor] = current_vertex
                    # add the neighbor to the priority queue
                    heapq.heappush(vertices_queue, (new_distance, neighbor))
    # if we have not found a path, return None
    return None