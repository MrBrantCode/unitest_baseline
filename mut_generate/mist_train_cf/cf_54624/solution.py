"""
QUESTION:
Create a data structure to store country names as keys and their corresponding population figures as values. The data structure should allow for efficient operations such as searching, editing, and sorting by both country name and population.
"""

def create_country_population_data_structure(country_population):
    return country_population

def add_country(country_population, country, population):
    country_population[country] = population

def search_country(country_population, country):
    return country_population.get(country)

def sort_by_country(country_population):
    return dict(sorted(country_population.items()))

def sort_by_population(country_population):
    return dict(sorted(country_population.items(), key=lambda item: item[1]))