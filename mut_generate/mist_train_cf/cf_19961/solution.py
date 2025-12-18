"""
QUESTION:
Implement a function `get_top_countries` that takes in a list of tuples representing countries and their populations, and returns the top 10 most populous countries. Additionally, the function should be able to efficiently retrieve the countries with a population above a certain threshold. The function should return a tuple where the first element is a list of the top 10 most populous countries and the second element is a function that takes a population threshold and returns a list of countries with a population above that threshold.
"""

import heapq

def get_top_countries(country_populations):
    country_map = {}
    top_countries = []
    
    # Populate the country map and initialize the heap
    for country, population in country_populations:
        country_map[country] = population
    
    # Get the top 10 most populous countries using a min-heap
    for country, population in country_map.items():
        if len(top_countries) < 10:
            heapq.heappush(top_countries, (population, country))
        else:
            heapq.heappushpop(top_countries, (population, country))
    
    # Sort the top countries in descending order
    top_countries = [country for _, country in sorted(top_countries, reverse=True)]
    
    # Function to get countries with a population above a certain threshold
    def get_countries_above_threshold(threshold):
        return [country for country, population in country_map.items() if population > threshold]
    
    return top_countries, get_countries_above_threshold