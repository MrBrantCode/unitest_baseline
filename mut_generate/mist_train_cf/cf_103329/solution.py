"""
QUESTION:
Write a function `get_planet_name` that takes an integer `num` representing the position of a planet from the Sun and returns the name of the corresponding planet. The function should have access to a list of planet names. If `num` is greater than the total number of planets, the function should return an error message indicating the total number of planets in the solar system.
"""

def get_planet_name(num):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if num > len(planets):
        return "Invalid input: There are only " + str(len(planets)) + " planets in the solar system."
    else:
        return planets[num - 1]