"""
QUESTION:
Write a function `find_planets_between` that takes two string parameters, `planet1` and `planet2`, representing the names of two planets in our solar system. The function should return a tuple of planet names that are orbitally located between `planet1` and `planet2`, ordered by their proximity to the Sun. If either `planet1` or `planet2` is not a valid planet name, the function should return an empty tuple. The valid planet names are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.
"""

def find_planets_between(planet1, planet2):
    planets_in_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Get the index of the given planets in the ordered list
    planet1_index = planets_in_order.index(planet1) if planet1 in planets_in_order else -1
    planet2_index = planets_in_order.index(planet2) if planet2 in planets_in_order else -1

    # If either planet is not found, return an empty list
    if planet1_index == -1 or planet2_index == -1:
        return []

    # Make sure, planet1_index is the smaller index
    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index

    # Return all the planets located between planet1 and planet2
    return planets_in_order[planet1_index+1 : planet2_index]