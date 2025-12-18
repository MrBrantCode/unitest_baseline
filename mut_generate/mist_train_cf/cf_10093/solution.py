"""
QUESTION:
Create a function `top_cities_by_population` that takes a list of cities and countries as input. The function should return the names of the top 5 cities with the highest population, but only include cities that are located in countries with a GDP per capita greater than $50,000. The cities and countries are related by a common 'country_id' and each city has a 'population' attribute. Each country has a 'gdp_per_capita' attribute.
"""

def top_cities_by_population(cities, countries):
    # First, filter countries with GDP per capita greater than $50,000
    eligible_countries = [country for country in countries if country['gdp_per_capita'] > 50000]

    # Then, filter cities that are located in eligible countries
    eligible_cities = [city for city in cities if city['country_id'] in [country['country_id'] for country in eligible_countries]]

    # Sort the eligible cities by population in descending order
    eligible_cities.sort(key=lambda city: city['population'], reverse=True)

    # Return the names of the top 5 cities
    return [city['city_name'] for city in eligible_cities[:5]]