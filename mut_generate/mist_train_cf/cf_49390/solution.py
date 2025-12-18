"""
QUESTION:
Create a function `simulate_bots` that takes two parameters: `time` (float) and `total_distance_x` (float). The function should simulate two bots moving in opposite directions on a 2-dimensional plane, one to the north-east and the other to the south-west. The bot moving to the north-east should move three times as fast in the x-direction as the bot moving to the south-west, but only half as fast in the y-direction. The function should calculate and return the individual velocities of the bots in both directions (x and y) in km/h and their current positions on the plane after the given time. Assume that the bots start at the same point (0, 0) and move in a straight line.
"""

def simulate_bots(time, total_distance_x):
    """
    Simulates two bots moving in opposite directions on a 2-dimensional plane.
    
    Parameters:
    time (float): Time in hours
    total_distance_x (float): Total distance in km in x-direction
    
    Returns:
    A dictionary containing the individual velocities of the bots in both directions (x and y) in km/h and their current positions on the plane after the given time.
    """
    
    # Calculate velocities based on given conditions 
    x_velocity_SW = total_distance_x / (4 * time)
    x_velocity_NE = 3 * x_velocity_SW
    y_velocity_SW = total_distance_x / (2 * time)
    y_velocity_NE = y_velocity_SW / 2

    # Calculate positions
    x_SW = -x_velocity_SW * time
    y_SW = -y_velocity_SW * time
    x_NE = x_velocity_NE * time
    y_NE = y_velocity_NE * time

    # Return results
    return {
        "SW": {
            "velocity": (x_velocity_SW, y_velocity_SW),
            "position": (x_SW, y_SW)
        },
        "NE": {
            "velocity": (x_velocity_NE, y_velocity_NE),
            "position": (x_NE, y_NE)
        }
    }