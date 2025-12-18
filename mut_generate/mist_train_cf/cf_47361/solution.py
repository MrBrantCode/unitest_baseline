"""
QUESTION:
Write a function `differential_return` that calculates the differential return for an action in a continuing task scenario. The function should take in the reward for the action and the average reward rate, and return the differential return value. The differential return is defined as the difference between the reward and the average reward rate.
"""

def differential_return(reward, average_reward_rate):
    """
    Calculate the differential return for an action in a continuing task scenario.

    Args:
        reward (float): The reward for the action.
        average_reward_rate (float): The average reward rate.

    Returns:
        float: The differential return value.
    """
    return reward - average_reward_rate