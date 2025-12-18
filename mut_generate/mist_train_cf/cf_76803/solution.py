"""
QUESTION:
Write a function `shortest_city_names` that takes a list of tuples, where each tuple contains a city name and its corresponding country code (ISO Alpha-2 code), and returns a dictionary where the keys are the country codes and the values are lists containing the shortest city names for each country. If there are multiple city names with the same shortest length for the same country, return them all in the order they appear in the list.
"""

def shortest_city_names(city_list):
    country_city = {}
    for city, country in city_list:
        if country in country_city.keys():
            if len(city) < len(country_city[country][0]):
                country_city[country] = [city]
            elif len(city) == len(country_city[country][0]):
                country_city[country].append(city)
        else:
            country_city[country] = [city]
    return country_city