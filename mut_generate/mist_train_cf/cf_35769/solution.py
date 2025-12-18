"""
QUESTION:
Implement a method `calculate_average_joint_position(joint_index)` within a class that calculates the average position of a specific joint across all samples in a given 5D NumPy array. The 5D array represents motion capture data with dimensions (N, C, T, V, M), where V is the number of joints and M is the dimensionality of the joints. The method should return the average (x, y, z) position of the joint specified by `joint_index` as a NumPy array of shape (3,). The input `joint_index` is the index of the joint for which to calculate the average position.
"""

import numpy as np

def calculate_average_joint_position(data, joint_index):
    # Calculate the average position of the specified joint across all samples
    joint_data = data[:, :, :, joint_index, :]  # Extract data for the specified joint
    average_position = np.mean(joint_data, axis=(0, 1, 2))  # Calculate the average position
    return average_position