"""
QUESTION:
Create a function `bf(planet1, planet2)` that takes two strings representing planet names in our solar system and returns a tuple of planets located orbitally between `planet1` and `planet2`, sorted by their proximity to the sun. The function should return an empty tuple if either `planet1` or `planet2` is not a valid planet name. Use a helper function `is_valid(planet)` to check if a given planet name is valid. The list of valid planet names is ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].
"""

def is_valid(planet):
    return planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def between_planets(planet1, planet2):
    planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if is_valid(planet1) and is_valid(planet2):
        planet1_index, planet2_index = planets_order.index(planet1), planets_order.index(planet2)
        
        # Swap the indices if their order is reversed (i.e. planet2 is closer to the sun than planet1)
        if planet1_index > planet2_index:
            planet1_index, planet2_index = planet2_index, planet1_index
        
        # Return a tuple of the planets located orbitally between planet1 and planet2, sorted by their proximity to the sun
        return tuple(planets_order[planet1_index+1:planet2_index])
    
    else:
        return ()