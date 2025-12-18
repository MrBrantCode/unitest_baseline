"""
QUESTION:
Create a function `simulate_disc_trajectory` that takes the following parameters:
- `model` (string): The disc model name.
- `a` (float): The launch angle in degrees.
- `v` (float): The launch velocity in meters per second.
- `rot` (float): The rotation rate in radians per second.
- `nose_up` (bool): Indicates whether the disc is thrown nose up (True) or not (False).
- `hyzer` (float): The hyzer angle in degrees.
- `time` (float): The total time for which the trajectory should be simulated.

The function should return a list of tuples, where each tuple represents the disc's position at a specific time during its flight. Each tuple should contain the time (in seconds) and the 3D coordinates (x, y, z) of the disc's position.
"""

import math

def simulate_disc_trajectory(model, a, v, rot, nose_up, hyzer, time):
    """
    Simulates the trajectory of a disc based on given parameters.

    Args:
    - model (string): The disc model name.
    - a (float): The launch angle in degrees.
    - v (float): The launch velocity in meters per second.
    - rot (float): The rotation rate in radians per second.
    - nose_up (bool): Indicates whether the disc is thrown nose up (True) or not (False).
    - hyzer (float): The hyzer angle in degrees.
    - time (float): The total time for which the trajectory should be simulated.

    Returns:
    - A list of tuples, where each tuple represents the disc's position at a specific time during its flight.
      Each tuple contains the time (in seconds) and the 3D coordinates (x, y, z) of the disc's position.
    """

    vx = math.cos(a * math.pi / 180) * v
    vz = math.sin(a * math.pi / 180) * v
    trajectory = []
    max_step = 0.2  # Default max_step value

    # Simulate disc trajectory using given parameters
    # Replace the following with actual trajectory simulation logic
    for t in range(0, int(time*10)+1):
        x = vx * t * max_step
        y = vz * t * max_step
        z = rot * t * max_step
        trajectory.append((t * max_step, x, y, z))

    return trajectory