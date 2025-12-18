"""
QUESTION:
Create a function named `city_directory` that takes a list of dictionaries representing cities in Spain, each containing information such as name, population, area, and whether the city is a political and administrative center. The function should return a new list containing only the cities that are primary centers, i.e., where the 'center' key is True. The function should be optimized for efficiency and maintain a balance between efficiency and complexity.
"""

def city_directory(cities):
    return [city for city in cities if city['center'] is True]