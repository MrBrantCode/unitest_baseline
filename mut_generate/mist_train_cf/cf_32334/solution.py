"""
QUESTION:
Implement a function `update_particle_state` that takes in a particle's position, velocity, and boundary type (either 'rectangular' or 'circular'). The function should update the particle's state based on its collision with the boundary. If the boundary is rectangular, the function should prevent the particle from exploding upon collision. If the boundary is circular, the function should transition the particle into a liquid state. Assume the particle's initial state and boundary properties are defined elsewhere.
"""

def update_particle_state(position, velocity, boundary_type):
    """
    Updates the particle's state based on its collision with the boundary.
    
    Args:
    position (list): The particle's position.
    velocity (list): The particle's velocity.
    boundary_type (str): The type of boundary, either 'rectangular' or 'circular'.
    
    Returns:
    tuple: A tuple containing the updated position and velocity.
    """

    # Update particle state for rectangular boundary
    if boundary_type == 'rectangular':
        # Prevent particle from exploding upon collision
        # Assuming a rectangular boundary at x=0 and x=max_x
        max_x = 10  # Replace with actual maximum x value
        if position[0] < 0:
            position[0] = 0
            velocity[0] = -velocity[0]  # Reverse x velocity
        elif position[0] > max_x:
            position[0] = max_x
            velocity[0] = -velocity[0]  # Reverse x velocity

    # Update particle state for circular boundary
    elif boundary_type == 'circular':
        # Transition particle into a liquid state
        # Assuming a circular boundary centered at (0, 0) with radius r
        r = 5  # Replace with actual radius value
        distance = (position[0]**2 + position[1]**2)**0.5
        if distance > r:
            # Particle is outside the circular boundary, no collision
            pass
        else:
            # Particle has collided with the circular boundary, transition to liquid state
            # Here you would update the particle's state based on the simulation requirements
            # For demonstration purposes, let's just print a message
            print("Particle has transitioned to a liquid state")

    return position, velocity