"""
QUESTION:
Given an initial average of a set of observations and the new average after adding a new observation, find the value of the new observation.

Create a function `find_additional_observation` that takes four parameters: the initial average `original_avg`, the number of original observations `original_count`, the new average `new_avg`, and the new total count of observations `new_count`. The function should return the value of the additional observation.
"""

def find_additional_observation(original_avg, original_count, new_avg, new_count):
    """
    This function calculates the value of the additional observation given 
    the initial average, the number of original observations, the new average, 
    and the new total count of observations.

    Parameters:
    original_avg (float): The initial average of the observations.
    original_count (int): The number of original observations.
    new_avg (float): The new average after adding a new observation.
    new_count (int): The new total count of observations.

    Returns:
    float: The value of the additional observation.
    """
    original_sum = original_avg * original_count
    new_sum = new_avg * new_count
    additional_observation = new_sum - original_sum
    return additional_observation