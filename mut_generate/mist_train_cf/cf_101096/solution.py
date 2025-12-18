"""
QUESTION:
Write a function `rank_cities_by_population(cities, populations)` that takes two lists as input: `cities` containing city names and `populations` containing corresponding population values. The function should return a list of city names sorted in descending order of their population. The function should assume that the input lists are of the same length and that the population values are numeric.
"""

def rank_cities_by_population(cities, populations):
    # Create a dictionary to store the city-population pairs
    city_populations = {}
    for i in range(len(cities)):
        city_populations[cities[i]] = populations[i]
    
    # Sort the dictionary by population in descending order
    sorted_cities = sorted(city_populations.items(), key=lambda x: x[1], reverse=True)
    
    # Extract the sorted city names and return them as a list
    sorted_city_names = [city[0] for city in sorted_cities]
    return sorted_city_names