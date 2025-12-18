"""
QUESTION:
Write a function `normalize_data` that takes a list of city names with their state abbreviations as input and returns a list with the data normalized. The normalization process involves title casing the city name, removing any full stops, upper casing the state abbreviation, and removing any extra characters apart from the comma separating the city and state.
"""

def normalize_data(dataset):
    normalized_data = []
    for city in dataset:
        city_name, city_abbr = city.split(',')

        city_name = city_name.replace('.', '').strip()
        city_abbr = city_abbr.replace('.', '').strip()

        city_name = city_name.title()
        city_abbr = city_abbr.upper()

        normalized_city = city_name + ', ' + city_abbr

        normalized_data.append(normalized_city)

    return normalized_data