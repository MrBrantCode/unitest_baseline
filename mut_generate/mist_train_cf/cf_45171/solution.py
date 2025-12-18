"""
QUESTION:
Create a function called `nearestNeighbour(graph)` that implements a greedy algorithm to find a possibly optimal solution for the traveling salesman problem, given a graph represented as a list of weighted edges between cities. The graph should be a list of lists, where each sublist contains two cities and the distance between them. The function should return the order in which the cities should be visited.
"""

def nearestNeighbour(graph):
    current_city = graph[0][0]
    path = [current_city]
    visited_cities = {city: False for city in set([city for pair in graph for city in pair[:2]])}
    visited_cities[current_city] = True

    while len(path) < len(visited_cities):
        closest_city = None
        min_distance = float('inf')
        for city_a, city_b, distance in graph:
            if city_a == current_city and not visited_cities[city_b] and distance < min_distance:
                min_distance = distance
                closest_city = city_b
            elif city_b == current_city and not visited_cities[city_a] and distance < min_distance:
                min_distance = distance
                closest_city = city_a
        path.append(closest_city)
        visited_cities[closest_city] = True
        current_city = closest_city

    return path