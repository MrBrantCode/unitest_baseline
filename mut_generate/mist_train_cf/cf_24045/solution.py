"""
QUESTION:
Write a function `traveling_salesman_heuristic` that takes a square distance matrix as input, where the element at row `i` and column `j` represents the distance between city `i` and city `j`. The function should return a tuple containing an approximate route for the traveling salesman problem and the total distance of the route. The route should be a list of city indices in the order they should be visited, and the function should use a nearest neighbor heuristic to find the route.
"""

def traveling_salesman_heuristic(distance_matrix):
    num_cities = len(distance_matrix)
    cities = range(num_cities)
    visited = [False for _ in range(num_cities)]
    route = []
    current_city = 0
    visited[current_city] = True
    route.append(current_city)
    total_distance = 0

    while False in visited:
        best_city = 0
        best_distance = float('inf')
        for i in range(num_cities):
            if not visited[i] and distance_matrix[current_city][i] < best_distance:
                best_city = i
                best_distance = distance_matrix[current_city][i]
                
        visited[best_city] = True
        route.append(best_city)
        total_distance += best_distance
        current_city = best_city
        
    total_distance += distance_matrix[route[-1]][route[0]]
    
    return route, total_distance