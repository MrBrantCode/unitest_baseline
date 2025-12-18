"""
QUESTION:
Write a function `calculate_particle_positions(inputs)` that takes in an object `inputs` with the following properties: `per_circ`, `radius`, and `time_interval`, and returns a list of positions for each particle at the specified time intervals.

- `per_circ` is the number of circular paths in the simulation.
- `radius` is the radius of each circular path.
- `time_interval` is the time interval at which to calculate the positions.

Each position should be a tuple representing the x, y, and z coordinates of a particle, where x is always 0 since the particles move in the y-z plane.
"""

import math

def calculate_particle_positions(inputs):
    positions = []
    for j in range(inputs.per_circ):
        angular_velocity = 2 * math.pi / inputs.time_interval
        particle_positions = [(0, inputs.radius * math.cos(angular_velocity * t), inputs.radius * math.sin(angular_velocity * t)) for t in range(0, inputs.time_interval + 1)]
        positions.append(particle_positions)
    return positions