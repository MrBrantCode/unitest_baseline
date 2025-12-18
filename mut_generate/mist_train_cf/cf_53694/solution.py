"""
QUESTION:
Write a function `bf(planet1, planet2)` that accepts two strings as planet names. The function should return a tuple of planets closer to the Sun than the inputted planets, in order of their proximity to the Sun. If the inputted planets are not valid, the function should return an empty tuple. A valid planet name is one of the following: 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'. The function should be case insensitive.
"""

def bf(planet1, planet2):
    solar_system = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if planet1.capitalize() in solar_system and planet2.capitalize() in solar_system:
        planet1_index = solar_system.index(planet1.capitalize())
        planet2_index = solar_system.index(planet2.capitalize())

        if planet1_index < planet2_index:
            return tuple(solar_system[i] for i in range(planet1_index + 1, planet2_index))
        
        if planet2_index < planet1_index:
            return tuple(solar_system[i] for i in range(planet2_index + 1, planet1_index))
        
        return ()

    else:
        return ()