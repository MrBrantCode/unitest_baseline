"""
QUESTION:
Implement a function `simulate_pendulum(initial_guesses: np.ndarray) -> np.ndarray` that simulates the trajectory of a pendulum given an array of initial guesses for the pendulum's state and control variables. The pendulum's dynamics are governed by the equations θ'(t) = ω(t) and ω'(t) = -g/l * sin(θ(t)) + u(t), where g = 9.81 m/s^2 is the acceleration due to gravity, l is the length of the pendulum, and u(t) is the control variable. The function should return the simulated trajectory of the pendulum as an array of angular positions and velocities over time.
"""

import numpy as np

def simulate_pendulum(initial_guesses: np.ndarray) -> np.ndarray:
    # Constants
    g = 9.81  # m/s^2
    l = 1.0   # length of the pendulum

    # Extract initial guesses
    theta_0 = initial_guesses[0]
    omega_0 = initial_guesses[1]
    control = initial_guesses[2]

    # Simulation parameters
    dt = 0.01  # time step
    num_steps = 1000  # number of time steps

    # Initialize arrays to store trajectory
    theta = np.zeros(num_steps)
    omega = np.zeros(num_steps)

    # Set initial conditions
    theta[0] = theta_0
    omega[0] = omega_0

    # Perform simulation using Euler's method
    for i in range(1, num_steps):
        omega[i] = omega[i-1] - (g/l) * np.sin(theta[i-1]) + control
        theta[i] = theta[i-1] + omega[i] * dt

    # Return simulated trajectory
    return np.vstack((theta, omega)).T