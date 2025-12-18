"""
QUESTION:
Create a function `top_three_migrant_countries` that takes a dictionary `migrants` where the keys are country names and the values are the number of migrants from each country. The function should exclude the countries listed in the `excluded_countries` list and return the names of the top three countries with the highest number of migrants. 

The function should assume that the input dictionary does not contain any of the excluded countries and that there are at least three countries in the dictionary. The function should also assume that the values in the dictionary are non-negative integers.
"""

def top_three_migrant_countries(migrants, excluded_countries):
    for country in excluded_countries:
        migrants.pop(country, None)
    sorted_migrants = sorted(migrants.items(), key=lambda x: x[1], reverse=True)
    return [country[0] for country in sorted_migrants[:3]]