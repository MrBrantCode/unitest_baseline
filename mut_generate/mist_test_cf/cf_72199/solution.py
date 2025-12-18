"""
QUESTION:
Calculate the angle at which a 40-foot ladder leaning against a wall with its base 15 feet away from the wall and use this angle to derive a mathematical model describing the painter's motion up the ladder at a constant speed of 30 feet per 65 seconds, then use the model to find the time it takes for the painter to reach the top of the ladder from the ground, considering gravity and assuming no slippage or horizontal motion.
"""

import math

def calculate_ladder_climbing_time(ladder_length, base_distance, climbing_speed, time_interval):
    """
    Calculate the time it takes for the painter to reach the top of the ladder from the ground.

    Parameters:
    ladder_length (float): The length of the ladder in feet.
    base_distance (float): The distance from the base of the ladder to the wall in feet.
    climbing_speed (float): The speed at which the painter climbs the ladder in feet per second.
    time_interval (float): The time interval over which the climbing speed is measured in seconds.

    Returns:
    float: The time it takes for the painter to reach the top of the ladder from the ground in seconds.
    """

    # Calculate the height of the ladder against the wall using the Pythagorean theorem
    height = math.sqrt(ladder_length**2 - base_distance**2)

    # Calculate the angle at which the ladder is leaning against the wall
    angle = math.atan(height / base_distance)

    # Calculate the time it takes to reach the top of the ladder
    time_to_reach_top = ladder_length / (climbing_speed * math.sin(angle))

    return time_to_reach_top

# Example usage:
ladder_length = 40  # feet
base_distance = 15  # feet
climbing_speed = 30 / 65  # feet per second
time_interval = 65  # seconds

time_to_reach_top = calculate_ladder_climbing_time(ladder_length, base_distance, climbing_speed, time_interval)