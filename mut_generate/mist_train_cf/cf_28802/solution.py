"""
QUESTION:
Write a function `simulate_projectile(m, v0, theta, k, dt, total_time)` that simulates the trajectory of a projectile in a 2D space, accounting for air resistance. The function should take the mass of the projectile (m), the initial velocity (v0), the launch angle (theta) in degrees, the air resistance coefficient (k), the time step (dt), and the total simulation time (total_time) as parameters, and return two lists representing the x and y coordinates of the projectile at each time step. Assume the acceleration due to gravity (g) is 9.81 m/s^2.
"""

import math

def simulate_projectile(m, v0, theta, k, dt, total_time):
    g = 9.81  # m/s^2
    x_values = []
    y_values = []

    # Convert angle from degrees to radians
    theta_rad = math.radians(theta)

    # Initial conditions
    x = 0
    y = 0
    vx = v0 * math.cos(theta_rad)
    vy = v0 * math.sin(theta_rad)

    while total_time > 0:
        x_values.append(x)
        y_values.append(y)

        v = math.sqrt(vx**2 + vy**2)
        ax = -k * v * vx / m
        ay = -g - k * v * vy / m

        x += vx * dt
        y += vy * dt
        vx += ax * dt
        vy += ay * dt

        total_time -= dt

    return x_values, y_values