"""
QUESTION:
Write a function `track_strongest_signal` that continuously adjusts the direction of an antenna to point towards the strongest RSSI (Received Signal Strength Indicator) signal emitted by a moving target, given the antenna's current direction and the RSSI values at each direction. The function should be able to handle a dynamic environment where the target moves over time and the antenna can rotate 360 degrees. The goal is to maximize the RSSI value by finding the optimal direction. The solution should be efficient and suitable for implementation on an Arduino.
"""

def track_strongest_signal(current_direction, rssi_values):
    """
    Continuously adjusts the direction of an antenna to point towards the strongest RSSI signal.

    Args:
        current_direction (float): The current direction of the antenna in degrees.
        rssi_values (list): A list of RSSI values at each direction.

    Returns:
        float: The optimal direction to point the antenna for the strongest RSSI signal.
    """

    # Initialize the maximum RSSI value and the corresponding direction
    max_rssi = float('-inf')
    optimal_direction = current_direction

    # Iterate over all directions and RSSI values
    for direction, rssi in enumerate(rssi_values):
        # Check if the current RSSI value is stronger than the maximum
        if rssi > max_rssi:
            # Update the maximum RSSI value and the optimal direction
            max_rssi = rssi
            optimal_direction = direction

    # Return the optimal direction
    return optimal_direction