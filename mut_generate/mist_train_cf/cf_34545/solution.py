"""
QUESTION:
Implement a function `simulate_motion` that simulates the motion of a sphere falling through a fluid under the influence of gravity. The function should take four parameters: `initial_velocity`, `initial_position`, `time_step`, and `total_time`. It should return two lists, the first containing the position of the sphere at each time step, and the second containing the velocity of the sphere at each time step. The simulation should be performed using the Euler method, taking into account the gravitational force, buoyant force, and drag force acting on the sphere. Assume the physical parameters are given: volume of the sphere (V), density of the fluid (rho_f), acceleration due to gravity (g), density of the sphere (rho_s), and viscosity of the fluid (eta), but these values can be hardcoded within the function.
"""

import math

def simulate_motion(initial_velocity, initial_position, time_step, total_time):
    # Physical parameters
    V = 0.1  # Volume of the sphere in cubic meters
    rho_f = 1000  # Density of the fluid in kg/m^3
    g = 9.81  # Acceleration due to gravity in m/s^2
    rho_s = 500  # Density of the sphere in kg/m^3
    eta = 0.01  # Viscosity of the fluid in N*s/m^2
    R = 0.05  # Radius of the sphere in meters

    # Initial conditions
    velocity = initial_velocity
    position = initial_position

    # Calculate sphere mass
    m = V * rho_s

    # To shorten the expressions
    A = -6 * math.pi * eta * R

    # Lists to store position and velocity at each time step
    positions = [position]
    velocities = [velocity]

    # Loop over every time step, always calculating the new elevation
    for t in range(0, int(total_time / time_step)):
        Fb = V * rho_f * g  # Buoyant force
        Fg = -m * g  # Gravitational force
        Fd = A * velocity  # Drag force
        net_force = Fb + Fg + Fd  # Net force

        # Update velocity and position using Euler method
        acceleration = net_force / m
        velocity += acceleration * time_step
        position += velocity * time_step

        # Append the new position and velocity to the lists
        positions.append(position)
        velocities.append(velocity)

    return positions, velocities