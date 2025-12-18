"""
QUESTION:
Create a function `bf(planet1, planet2)` that takes two strings representing planet names in our solar system and returns a sorted tuple of tuples. Each inner tuple contains the name of a planet between `planet1` and `planet2` (inclusive of neither) and the time it would take a spaceship traveling at light speed to reach that planet from the Sun in hours. If `planet1` or `planet2` is not a valid planet name, the function should return an empty tuple. Assume the average distance of each planet from the Sun is provided in a dictionary where the keys are planet names and the values are average distances in Astronomical Units (AU).
"""

# Orbits are not perfect circles thus these are average distances.
orbit_time = {
    'Mercury': 0.39,
    'Venus': 0.72,
    'Earth': 1, 
    'Mars': 1.52,
    'Jupiter': 5.20,
    'Saturn': 9.58,
    'Uranus': 19.18,
    'Neptune': 30.07,
    'Pluto': 39.48
}
# According to astronomy, light travels 1 AU in about 499.0 seconds
# In hours, this would be about 0.1386 hours/AU
LIGHT_SPEED = 0.1386  #hours/AU 

def between_planets(planet1, planet2):
    if planet1 in orbit_time and planet2 in orbit_time:
        planet_list = sorted(orbit_time.keys(), key=lambda p: orbit_time[p])
        start = min(planet_list.index(planet1), planet_list.index(planet2))
        end = max(planet_list.index(planet1), planet_list.index(planet2))
        return tuple([(planet, round(orbit_time[planet] * LIGHT_SPEED, 2)) for planet in planet_list[start+1:end]])
    else:
        return ()