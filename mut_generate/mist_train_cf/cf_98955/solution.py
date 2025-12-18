"""
QUESTION:
Write a function named `find_top_countries` that finds the top three countries with the highest migrant populations from a given dictionary, excluding the countries listed in `excluded_countries`. The function should return the names of the top three countries.

The input dictionary contains country names as keys and their corresponding migrant populations as values. The excluded countries are: Italy, Russia, Austria-Hungary, Germany, Great Britain, Ireland, Sweden, Norway, Denmark, and Greece.
"""

def find_top_countries(migrants, excluded_countries):
    # Exclude countries from the dictionary
    for country in excluded_countries:
        migrants.pop(country, None)

    # Sort the dictionary by values in descending order
    sorted_migrants = sorted(migrants.items(), key=lambda x: x[1], reverse=True)

    # Return the names of the top three countries
    return [country[0] for country in sorted_migrants[:3]]