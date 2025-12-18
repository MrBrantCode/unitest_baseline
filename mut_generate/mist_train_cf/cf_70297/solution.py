"""
QUESTION:
Write a function `bf(planet1, planet2, planet3)` that accepts three strings representing planet names in our solar system. The function should return a tuple of planet names that are closer to the Sun than the input planets, sorted in order of their proximity to the Sun. If any input is not a valid planet name, return an empty tuple. The planets of our solar system in order of their proximity to the Sun are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.
"""

def bf(planet1, planet2, planet3):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    valid_planets = set(planets)
    if planet1 not in valid_planets or planet2 not in valid_planets or planet3 not in valid_planets:
        return tuple()
    else:
        planets_input = sorted([planet1, planet2, planet3], key=planets.index)
        return tuple(planets[:planets.index(planets_input[0])])