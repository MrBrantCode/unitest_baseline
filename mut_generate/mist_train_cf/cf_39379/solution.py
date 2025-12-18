"""
QUESTION:
Implement a function `simulate_orbit(json_input)` that simulates the orbit of a celestial body around a planet given a JSON string. The JSON string contains parameters "GM" (gravitational parameter of the planet), "x0" and "y0" (initial x and y coordinates of the celestial body), and "vx0" and "vy0" (initial velocities in the x and y directions of the celestial body). The function should calculate the trajectory of the celestial body over time using numerical methods and output the trajectory coordinates at regular intervals. Assume the input JSON string is well-formed and contains all required parameters.
"""

import json
import math

def simulate_orbit(json_input):
    params = json.loads(json_input)
    GM = params["GM"]
    x0 = params["x0"]
    y0 = params["y0"]
    vx0 = params["vx0"]
    vy0 = params["vy0"]

    # Define simulation parameters
    num_steps = 1000
    delta_t = 0.1

    # Initialize arrays to store trajectory coordinates
    x_traj = [x0]
    y_traj = [y0]

    # Perform simulation using Euler's method
    for _ in range(num_steps):
        r = math.sqrt(x_traj[-1]**2 + y_traj[-1]**2)
        ax = -GM * x_traj[-1] / r**3
        ay = -GM * y_traj[-1] / r**3
        vx0 += ax * delta_t
        vy0 += ay * delta_t
        x0 += vx0 * delta_t
        y0 += vy0 * delta_t
        x_traj.append(x0)
        y_traj.append(y0)

    # Return the trajectory coordinates
    return list(zip(x_traj, y_traj))