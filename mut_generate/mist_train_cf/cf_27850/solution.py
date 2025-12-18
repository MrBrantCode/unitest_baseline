"""
QUESTION:
Implement a function `count_mobs_spawned` that takes a list of mob spawn requests, where each request is a list of four values (mob identifier, x-coordinate, y-coordinate, and a boolean indicating aggressiveness), and returns a dictionary containing the total number of mobs spawned at each coordinate. The dictionary should have coordinates as keys (represented as (x, y) tuples) and the total number of mobs spawned at those coordinates as values. Ignore the mob identifier and aggressiveness for this task.
"""

def count_mobs_spawned(spawn_requests):
    mob_counts = {}
    for request in spawn_requests:
        coordinates = (request[1], request[2])  # Extract x and y coordinates from the spawn request
        mob_counts[coordinates] = mob_counts.get(coordinates, 0) + 1  # Increment the count for the coordinates
    return mob_counts