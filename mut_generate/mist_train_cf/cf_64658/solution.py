"""
QUESTION:
Create a function `count_moons` that takes a dictionary `solar_system` where the keys are the names of celestial bodies and the values are lists of their corresponding moons, and returns a dictionary where the keys are the celestial bodies and the values are the number of moons. 

Then, create a function `sort_bodies` that takes the dictionary returned by `count_moons` and returns a new dictionary sorted by the number of moons in descending order. 

The input dictionary can contain any celestial body with any number of moons, including zero. The function should handle potential exceptions and edge cases.
"""

def count_moons(solar_system):
    return {body: len(moons) if moons is not None else 0 for body, moons in solar_system.items()}

def sort_bodies(moon_counts):
    return {k: v for k, v in sorted(moon_counts.items(), key=lambda item: item[1], reverse=True)}