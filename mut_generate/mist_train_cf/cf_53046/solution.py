"""
QUESTION:
Create a function named `calculate_angle_of_depression` that calculates the angle of depression when a stone is dropped downward with an initial velocity and subjected to a horizontal wind force. The function should take as input the mass of the stone (in kg), the initial velocity (in m/s), the wind force (in N), and the gravitational acceleration (in m/s²). The function should return the angle of depression in degrees. The angle should be calculated using numerical integration with a time step of 0.01 s and a total simulation time of 1.0 s.
"""

import math

def calculate_angle_of_depression(mass, initial_velocity, wind_force, gravity, simulation_time, time_step):
    """
    Calculate the angle of depression of a stone dropped downward with an initial velocity and subjected to a horizontal wind force.

    Args:
    mass (float): The mass of the stone in kg.
    initial_velocity (float): The initial velocity of the stone in m/s.
    wind_force (float): The wind force in N.
    gravity (float): The gravitational acceleration in m/s².
    simulation_time (float): The total simulation time in s.
    time_step (float): The time step for numerical integration in s.

    Returns:
    float: The angle of depression in degrees.
    """

    # Initial state
    x = 0.0
    y = 0.0
    vx = 0.0
    vy = -initial_velocity  # Negative because it's downward

    for _ in range(int(simulation_time / time_step)):
        # Calculate accelerations
        ax = wind_force / mass
        ay = gravity

        # Update velocities
        vx += ax * time_step
        vy += ay * time_step

        # Update positions
        x += vx * time_step
        y += vy * time_step

    # Calculate the angle of depression [degrees]
    angle = math.degrees(math.atan2(abs(y), x))

    return angle