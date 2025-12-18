"""
QUESTION:
Write a function named `populate_countries` that constructs a dictionary with countries as keys and their total population as values. The function should handle duplicate country values in the input list and return the countries sorted in descending order of their population. The function should have a time complexity of O(nlogn) and a space complexity of O(n). The function should take two parameters: a list of country names and a dictionary containing the population of each country.
"""

def populate_countries(countries, population):
    result = {}
    for country in countries:
        result[country] = result.get(country, 0) + population[country]
    return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}