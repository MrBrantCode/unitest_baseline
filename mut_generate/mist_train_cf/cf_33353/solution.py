"""
QUESTION:
Implement the `sim_step` function that updates the position `u` and velocity `v` of a particle in a 2D space according to the equations: 
`u = (u[0] + v[0], u[1] + v[1])` and `v = (v[0] * 0.9, v[1] * 0.9)`, where `u` and `v` are tuples representing the position and velocity of the particle respectively. 

The `sim_step` function should take a particle's current velocity as an argument, and the particle's position and velocity should be updated based on this velocity. 

Assuming the `sim_step` function is called 100 times, starting from an initial position of (0, 0) and an initial velocity of (1, 1), implement the function and output the final position of the particle after the simulation.
"""

def sim_step(u, v):
    """
    Updates the position and velocity of a particle in a 2D space.
    
    Args:
    u (tuple): The current position of the particle.
    v (tuple): The current velocity of the particle.
    
    Returns:
    tuple: A tuple containing the updated position and velocity.
    """
    new_u = (u[0] + v[0], u[1] + v[1])
    new_v = (v[0] * 0.9, v[1] * 0.9)
    return new_u, new_v