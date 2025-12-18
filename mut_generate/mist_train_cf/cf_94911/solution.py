"""
QUESTION:
Write a function called `populate_countries` that takes a list of country names and a dictionary mapping country names to their populations. The function should return a dictionary where the keys are the unique country names and the values are the total population for each country, with the population values in descending order. The function should have a time complexity of O(nlogn) and a space complexity of O(n), and should handle duplicate country names in the input list.
"""

def populate_countries(countries, population):
    country_population = {}
    
    for country in countries:
        country_population[country] = country_population.get(country, 0) + population[country]
    
    return dict(sorted(country_population.items(), key=lambda item: item[1], reverse=True))