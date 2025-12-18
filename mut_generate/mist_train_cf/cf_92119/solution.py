"""
QUESTION:
Create a function `get_planet_name` that takes an integer as input representing the position of a planet from the Sun and returns the name of the corresponding planet. The function should use a predefined list of planet names. If the input number exceeds the total number of planets, the function should return an error message indicating the total number of planets in the solar system.
"""

def get_planet_name(id):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if id > len(planets):
        return f"Invalid input: There are only {len(planets)} planets in the solar system."
    else:
        return planets[id - 1]