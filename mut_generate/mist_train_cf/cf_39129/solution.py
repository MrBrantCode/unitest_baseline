"""
QUESTION:
Create a class `NBodySimulator` with the following functionalities: 

- Initialize the simulator with a list of celestial objects, each represented by its mass, initial position, and initial velocity.
- Simulate the motion of the celestial objects over a specified duration using a numerical integration method.
- Provide a method to retrieve the positions of the celestial objects at any given time during the simulation.

Restrictions: The implementation should accurately model the gravitational interactions between the celestial objects.
"""

def entrance(masses, initial_positions, initial_velocities, duration, time_step):
    """
    Simulate the motion of celestial objects over a specified duration.

    Parameters:
    masses (list): List of masses of celestial objects.
    initial_positions (list): List of initial positions of celestial objects.
    initial_velocities (list): List of initial velocities of celestial objects.
    duration (float): Duration of the simulation.
    time_step (float): Time step for the simulation.

    Returns:
    positions_over_time (list): List of positions of celestial objects at each time step.
    """

    celestial_objects = [
        CelestialObject(mass, position, velocity)
        for mass, position, velocity in zip(masses, initial_positions, initial_velocities)
    ]

    num_steps = int(duration / time_step)
    positions_over_time = []

    for _ in range(num_steps):
        positions = [obj.position.tolist() for obj in celestial_objects]
        positions_over_time.append(positions)
        _update_positions(celestial_objects, time_step)

    return positions_over_time


def _update_positions(celestial_objects, time_step):
    for obj in celestial_objects:
        acceleration = _calculate_acceleration(obj, celestial_objects)
        obj.position += obj.velocity * time_step
        obj.velocity += acceleration * time_step


def _calculate_acceleration(obj, celestial_objects):
    acceleration = np.zeros_like(obj.position)
    for other_obj in celestial_objects:
        if other_obj != obj:
            displacement = other_obj.position - obj.position
            distance = np.linalg.norm(displacement)
            force_magnitude = (obj.mass * other_obj.mass) / distance**2
            force_direction = displacement / distance
            acceleration += force_magnitude / obj.mass * force_direction
    return acceleration


class CelestialObject:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)