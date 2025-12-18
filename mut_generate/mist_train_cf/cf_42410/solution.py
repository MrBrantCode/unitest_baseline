"""
QUESTION:
Write a function `simulate_robot_motion` that takes the initial pose of a robot (x, y, theta), linear velocity, angular velocity, and time interval as input and returns the final pose (x, y, theta) of the robot after the given time interval, where the robot's motion is governed by the kinematic equations dx/dt = v * cos(theta), dy/dt = v * sin(theta), and dtheta/dt = omega. The orientation angle theta should be normalized to the range [0, 2*pi).
"""

import numpy as np

def simulate_robot_motion(initial_pose, linear_velocity, angular_velocity, time_interval):
    x, y, theta = initial_pose
    v = linear_velocity
    omega = angular_velocity

    # Update the pose using kinematic equations
    x += v * np.cos(theta) * time_interval
    y += v * np.sin(theta) * time_interval
    theta += omega * time_interval

    # Normalize theta to the range [0, 2*pi)
    theta = (theta + 2 * np.pi) % (2 * np.pi)

    return x, y, theta