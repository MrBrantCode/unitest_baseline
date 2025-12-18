"""
QUESTION:
Write a function named `rank_cities_by_population` that ranks a list of cities in descending order of their corresponding populations. The function should take two parameters: `cities` (a list of city names) and `populations` (a list of population values corresponding to the cities). The function should return a list of city names in the order of their population, with the most populous city first. The length of the input lists `cities` and `populations` will always be the same.
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