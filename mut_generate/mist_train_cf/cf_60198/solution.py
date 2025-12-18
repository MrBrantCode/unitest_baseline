"""
QUESTION:
Write a function `bf` that takes two planetary names as strings, `planet1` and `planet2`, and returns a list of planets that orbit the sun between the orbits of `planet1` and `planet2`, in order of their proximity to the sun. If either `planet1` or `planet2` is not a valid planet, return an empty list.
"""

def bf(planet1, planet2):
    """
    Returns a list of planets that orbit the sun between the orbits of planet1 and planet2,
    in order of their proximity to the sun.

    Args:
        planet1 (str): The first planetary name.
        planet2 (str): The second planetary name.

    Returns:
        list: A list of planets between planet1 and planet2, or an empty list if either planet is not valid.
    """
    planets_pos = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }

    if planet1 not in planets_pos or planet2 not in planets_pos:
        return []

    lower = min(planets_pos[planet1], planets_pos[planet2])
    upper = max(planets_pos[planet1], planets_pos[planet2])

    result = [planet for planet, pos in planets_pos.items() if lower < pos < upper]

    return result