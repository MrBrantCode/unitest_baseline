"""
QUESTION:
Write a function `sort_places` that takes a dictionary of places and their continents as input. The function should return two types of groups. The first type should group the places by their continents, with five lists for 'Asia', 'Europe', 'North America', 'Oceania', and 'Others'. The second type should group the places by their hemispheres, with two lists for 'Northern Hemisphere' and 'Southern Hemisphere'. 

Assume the following rules for hemisphere classification: 
- 'Asia' and 'Europe' belong to the 'Northern Hemisphere'.
- 'North America' is classified based on the actual location of the city, but for the purpose of this exercise, assume all cities in 'North America' belong to the 'Northern Hemisphere'.
- 'Oceania' belongs to the 'Southern Hemisphere'.
"""

def sort_places(places):
    """
    Sorts a dictionary of places by their continents and hemispheres.

    Args:
    places (dict): A dictionary of places and their continents.

    Returns:
    tuple: Two dictionaries. The first dictionary groups places by their continents,
           and the second dictionary groups places by their hemispheres.
    """
    # Initialize dictionaries to store the results
    by_continent = {'Asia': [], 'Europe': [], 'North America': [], 'Oceania': [], 'Others': []}
    by_hemisphere = {'Northern Hemisphere': [], 'Southern Hemisphere': []}

    # Group places based on continent and hemisphere
    for place, continent in places.items():
        if continent in by_continent:
            by_continent[continent].append(place)
        else:
            by_continent['Others'].append(place)

        if continent in ['Asia', 'Europe', 'North America']:
            by_hemisphere['Northern Hemisphere'].append(place)
        elif continent == 'Oceania':
            by_hemisphere['Southern Hemisphere'].append(place)

    return by_continent, by_hemisphere