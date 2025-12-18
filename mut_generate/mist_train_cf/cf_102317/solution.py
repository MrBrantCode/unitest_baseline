"""
QUESTION:
Write a function `find_most_populous_countries` that takes a list of country dictionaries with 'name' and 'population' keys and returns the name and population of the top 10 most populous countries, the country with the lowest population, and the average population of the top 10 countries. The function should minimize unnecessary iterations and optimize the use of data structures.
"""

def find_most_populous_countries(countries):
    most_populous_countries = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]
    lowest_population_country = min(countries, key=lambda x: x['population'])
    total_population = sum(country['population'] for country in most_populous_countries)
    average_population = total_population / len(most_populous_countries)
    
    return most_populous_countries, lowest_population_country, average_population