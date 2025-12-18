"""
QUESTION:
Write a function called `tsp_brute_force` that takes a list of cities as input, where each city is represented by its coordinates (x, y). The function should return the shortest route that visits all cities and returns to the starting city. The function should use a brute-force approach by generating all possible permutations of cities and calculating the total distance for each permutation.

Restrictions: The function should not use any external libraries or built-in functions to generate permutations or calculate distances. The function should also not use any optimization techniques or heuristics.
"""

def tsp_brute_force(cities):
    def permutations(cities):
        if len(cities) == 1:
            return [cities]
        result = []
        for i in range(len(cities)):
            current_city = cities[i]
            remaining_cities = cities[:i] + cities[i+1:]
            for p in permutations(remaining_cities):
                result.append([current_city] + p)
        return result

    def calculate_distance(route):
        distance = 0
        for i in range(len(route) - 1):
            x1, y1 = route[i]
            x2, y2 = route[i+1]
            distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return distance

    shortest_route = None
    shortest_distance = float('inf')
    for route in permutations(cities):
        distance = calculate_distance(route)
        distance += ((route[-1][0] - route[0][0]) ** 2 + (route[-1][1] - route[0][1]) ** 2) ** 0.5  # add the distance from the last city back to the first city
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route
    return shortest_route