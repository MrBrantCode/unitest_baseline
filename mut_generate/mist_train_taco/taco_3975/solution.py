"""
QUESTION:
Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health.
Health can't be less than 0.
"""

def calculate_new_health(current_health, damage):
    """
    Calculate the player's new health after taking damage.

    Parameters:
    - current_health (int or float): The player's current health.
    - damage (int or float): The amount of damage received.

    Returns:
    - new_health (int or float): The player's new health after taking the damage, ensuring it is not less than 0.
    """
    return max(0, current_health - damage)