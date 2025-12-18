"""
QUESTION:
Write a function `find_first_collision(particles)` that takes a list of tuples `particles` where each tuple contains a unique positive integer identifier and an integer velocity between -100 and 100. The function should return a tuple of the identifiers of the two particles that will collide first in a one-dimensional space, or None if no collision will occur. The list `particles` will contain at least two elements.
"""

def find_first_collision(particles):
    min_time = float('inf')
    collision_pair = None

    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            time_to_collision = (particles[j][0] - particles[i][0]) / (particles[i][1] - particles[j][1])
            if time_to_collision > 0 and time_to_collision < min_time:
                min_time = time_to_collision
                collision_pair = (particles[i][0], particles[j][0])

    return collision_pair