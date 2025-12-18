"""
QUESTION:
Implement the `process_buffers` function that takes in `adv_buffer`, `obs_buffer`, `action_buffer`, `reward_buffer`, `value_buffer`, and `logp_buffer` as inputs. The function should normalize the `adv_buffer` by subtracting its mean and dividing by its standard deviation. Then, it should return a dictionary `data` containing the contents of `obs_buffer`, `action_buffer`, `reward_buffer`, `value_buffer`, and `logp_buffer` with the keys 'obs', 'action', 'reward', 'value', and 'logp' respectively. The function should not modify the original buffers. Assume that the input buffers are numpy arrays. The function should handle potential division by zero error when normalizing the `adv_buffer`.
"""

import numpy as np

def process_buffers(adv_buffer, obs_buffer, action_buffer, reward_buffer, value_buffer, logp_buffer):
    """
    Normalize the advantage buffer by subtracting its mean and dividing by its standard deviation.
    Populate a dictionary with the contents of the observation, action, reward, value, and log probability buffers.
    
    Parameters:
    adv_buffer (numpy array): Advantage buffer
    obs_buffer (numpy array): Observation buffer
    action_buffer (numpy array): Action buffer
    reward_buffer (numpy array): Reward buffer
    value_buffer (numpy array): Value buffer
    logp_buffer (numpy array): Log probability buffer
    
    Returns:
    dict: Dictionary containing the observation, action, reward, value, and log probability buffers
    """

    # Normalize adv_buffer by subtracting its mean and dividing by its standard deviation
    # Add a small value to std to handle potential division by zero error
    normalized_adv_buffer = (adv_buffer - adv_buffer.mean()) / (adv_buffer.std() + 1e-8)

    # Populate data dictionary with the contents of the buffers
    data = dict(
        obs=obs_buffer,
        action=action_buffer,
        reward=reward_buffer,
        value=value_buffer,
        logp=logp_buffer,
        adv=normalized_adv_buffer  # Include the normalized advantage buffer in the data dictionary
    )

    return data