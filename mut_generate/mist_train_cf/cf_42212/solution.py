"""
QUESTION:
Implement the function `calculate_observation_error` that takes two NumPy arrays `real_trajectories` and `sim_trajectories` of shape `(n, m)` as input, where `n` is the number of observations and `m` is the number of features in each observation. The function should calculate the mean squared error (MSE) between the two trajectories, ensuring they have the same length before calculation. The function should return the overall MSE as a single float value.
"""

import numpy as np

def calculate_observation_error(real_trajectories, sim_trajectories):
    """Calculates MSE of observations in two trajectories."""
    def pad_or_truncate(observations, desired_length):
        (current_length, _) = observations.shape
        if current_length < desired_length:
            return np.pad(
                observations,
                pad_width=((0, desired_length - current_length), (0, 0)),
                mode="edge",
            )
        else:
            return observations[:desired_length, :]

    # Ensure both trajectories have the same length
    max_length = max(real_trajectories.shape[0], sim_trajectories.shape[0])
    real_padded = pad_or_truncate(real_trajectories, max_length)
    sim_padded = pad_or_truncate(sim_trajectories, max_length)

    # Calculate MSE for each observation and return the overall MSE
    mse = np.mean((real_padded - sim_padded) ** 2)
    return mse