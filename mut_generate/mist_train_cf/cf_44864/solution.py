"""
QUESTION:
Implement a function named `nearest_neighbor` that takes a list of cities, where each city is represented as a tuple of two integers (x, y) representing its coordinates. The function should return a list of cities representing the shortest possible route that visits each city exactly once, starting and ending at the same city, using the Nearest Neighbor algorithm. The distance between two cities is calculated using the Euclidean distance formula.
"""

def nearest_neighbor(cities):
    current_city = cities[0]
    path = [current_city]
    remaining_cities = set(cities[1:])
    
    def distance(city1, city2):
        return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distance(current_city, city))
        remaining_cities.remove(next_city)
        path.append(next_city)
        current_city = next_city
    
    path.append(cities[0])
    return path