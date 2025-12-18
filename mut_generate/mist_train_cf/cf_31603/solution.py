"""
QUESTION:
Create a function called `group_countries_by_letter` that takes a list of country names as input. The function should sort the countries in alphabetical order, group them by the first letter of each country, count the number of countries that start with each letter, and return the result as a string with each group on a new line in the format "Letter: Count - Country1, Country2, ...".
"""

def group_countries_by_letter(countries):
    """
    Sorts countries in alphabetical order, groups them by the first letter of each country,
    counts the number of countries that start with each letter, and returns the result as a string.

    Args:
        countries (list): A list of country names.

    Returns:
        str: A string with each group on a new line in the format "Letter: Count - Country1, Country2, ...".
    """
    # Create a dictionary to store countries grouped by the first letter
    country_groups = {}

    # Sort the countries in alphabetical order
    countries.sort()

    # Group the countries by the first letter and count the occurrences
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in country_groups:
            country_groups[first_letter].append(country)
        else:
            country_groups[first_letter] = [country]

    # Return the grouped countries and their counts as a string
    result = ""
    for letter, country_list in sorted(country_groups.items()):
        count = len(country_list)
        country_names = ", ".join(country_list)
        result += f"{letter}: {count} - {country_names}\n"
    return result.strip()