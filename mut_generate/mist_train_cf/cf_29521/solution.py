"""
QUESTION:
Implement a function `simulate_particle_trajectory` that takes the following parameters:
- `initial_position`: a tuple (x, y) representing the initial position of the particle.
- `velocity_vectors`: a list of tuples representing the velocity vectors in the format (vx, vy).
- `time_step`: a float representing the time interval between each velocity update.

The function should return a list of tuples, where each tuple represents the x and y coordinates of the particle at each time step.
"""

def simulate_particle_trajectory(initial_position, velocity_vectors, time_step):
    x, y = initial_position
    positions = [(x, y)]
    
    for vx, vy in velocity_vectors:
        x += vx * time_step
        y += vy * time_step
        positions.append((x, y))
    
    return positions