"""
QUESTION:
Write a function `find_top_and_lowest_population_countries` that finds and returns the names and populations of the top three most populous countries and the country with the lowest population from a given list of countries with their populations. The function should also return the average population of the top three countries. 

The input is a list of dictionaries, where each dictionary contains the name and population of a country. The function should minimize unnecessary iterations and optimize the use of data structures.
"""

def find_top_and_lowest_population_countries(countries):
    # Sort the countries list in descending order based on population
    countries.sort(key=lambda x: x['population'], reverse=True)
    
    # Get the top three most populous countries
    top_countries = countries[:3]
    
    # Sort the countries list in ascending order based on population
    countries.sort(key=lambda x: x['population'])
    
    # Get the country with the lowest population
    lowest_population_country = countries[0]
    
    # Calculate the average population of the top three countries
    average_population = sum(country['population'] for country in top_countries) / len(top_countries)
    
    return top_countries, lowest_population_country, average_population