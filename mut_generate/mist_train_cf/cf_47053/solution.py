"""
QUESTION:
Write a function `planet_name(n)` that takes an integer `n` representing the order of a planet from the sun in our solar system. Return the name of the corresponding planet, considering only the eight planets (Mercury to Neptune) and disregarding exoplanets and dwarf planets. If `n` is out of range (less than 1 or greater than 8), return "No such planet in our solar system!"
"""

def planet_name(n):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if 1 <= n <= 8:
        return planets[n-1]
    return "No such planet in our solar system!"