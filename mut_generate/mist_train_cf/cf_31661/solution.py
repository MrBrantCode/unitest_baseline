"""
QUESTION:
Write a function `find_200th_vaporized` that takes a dictionary `asteroids` as input, where the keys are the coordinates of asteroids and the values are their corresponding angles with respect to the laser's starting position. The function should return the coordinates of the 200th asteroid to be vaporized when the laser starts at a specific location and rotates around the asteroids in a clockwise direction.
"""

def find_200th_vaporized(asteroids):
    vaporised_coords = set()
    last_angle = None
    vaporised = 0
    for asteroid, info in sorted(asteroids.items(), key=lambda x: x[1]):
        angle = info
        if angle == last_angle or asteroid in vaporised_coords:
            continue
        last_angle = angle
        vaporised_coords.add(asteroid)
        vaporised += 1
        if vaporised == 200:
            return asteroid