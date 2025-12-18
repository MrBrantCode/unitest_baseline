"""
QUESTION:
Create a function `solar_dist(planet1, planet2)` that takes two parameters: the names of two planets in our solar system. The function should return a tuple containing the names of all planets that have a smaller solar distance than the maximum solar distance of the two provided planets. If either of the provided planet names is not valid, the function should return an empty tuple. Assume the solar distances of the planets from the sun are: Mercury (1), Venus (2), Earth (3), Mars (4), Jupiter (5), Saturn (6), Uranus (7), and Neptune (8).
"""

def solar_dist(planet1, planet2):
    def check_validity(planet):
        return planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter","Saturn", "Uranus", "Neptune"]

    solar_distance = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }

    if check_validity(planet1) and check_validity(planet2):
        distance1 = solar_distance.get(planet1)
        distance2 = solar_distance.get(planet2)

        closer_planets = [planet for planet in solar_distance if solar_distance[planet] < max(distance1, distance2)]
        return tuple(closer_planets)
    else:
        return ()