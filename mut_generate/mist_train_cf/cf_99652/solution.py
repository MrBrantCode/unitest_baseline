"""
QUESTION:
Write a function named `sort_places_by_location` that takes a dictionary of places and their corresponding continents as input. The function should group the places into five lists: Asia, Europe, North America, Oceania, and Others. Then, it should further divide each continent into two groups based on their hemisphere, with Asia and Europe classified as the Northern Hemisphere and North America and Oceania classified as the Southern Hemisphere for this specific problem. However, the classification of hemisphere for each continent should be a general rule. For instance, places located above the equator should be classified as the northern hemisphere, and those below the equator should be classified as the southern hemisphere.
"""

def sort_places_by_location(places):
    """
    This function takes a dictionary of places and their corresponding continents as input.
    It groups the places into five lists: Asia, Europe, North America, Oceania, and Others.
    Then, it further divides each continent into two groups based on their hemisphere.

    Args:
        places (dict): A dictionary of places and their corresponding continents.

    Returns:
        dict: A dictionary containing the grouped places by continent and hemisphere.
    """

    # Group places based on continent and subcontinent
    asia = []
    europe = []
    north_america = []
    oceania = []
    others = []
    for place, continent in places.items():
        if continent == 'Asia':
            asia.append(place)
        elif continent == 'Europe':
            europe.append(place)
        elif continent == 'North America':
            north_america.append(place)
        elif continent == 'Oceania':
            oceania.append(place)
        else:
            others.append(place)

    # Group places based on hemisphere
    northern_hemisphere = []
    southern_hemisphere = []
    for place in asia + europe + north_america + oceania:
        if place in asia or place in europe:
            northern_hemisphere.append(place)
        else:
            southern_hemisphere.append(place)

    # Return the sorted list of places
    return {
        "Asia": asia,
        "Europe": europe,
        "North America": north_america,
        "Oceania": oceania,
        "Others": others,
        "Northern Hemisphere": northern_hemisphere,
        "Southern Hemisphere": southern_hemisphere,
    }