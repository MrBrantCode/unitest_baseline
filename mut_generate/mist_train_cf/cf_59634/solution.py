"""
QUESTION:
Function Name: calculate_speed

The function should take three parameters: total_time (X) in hours, total_distance (Y) in kilometers, and stop_time (Z) in minutes. The car makes two stops, one on the way to the destination and one on the way back. The car travels 20% slower on the return journey. 

The function should calculate and return the speed of the car on its outbound journey in kilometers per hour, considering that speed remains constant throughout the journey except during stops.
"""

def calculate_speed(total_time, total_distance, stop_time):
    """
    Calculate the speed of the car on its outbound journey in kilometers per hour.

    Args:
    total_time (float): The total time for the round trip in hours.
    total_distance (float): The total distance to the destination in kilometers.
    stop_time (float): The stop time in minutes.

    Returns:
    float: The speed of the car on the outbound journey in kilometers per hour.
    """
    # Calculate the total time in hours for the stops
    total_stop_time_hour = (stop_time * 2) / 60
    
    # Calculate the driving time
    driving_time = total_time - total_stop_time_hour
    
    # Calculate the time taken for the outbound journey
    outbound_time = (1 / 1.2) * driving_time
    
    # Calculate the speed of the car on the outbound journey
    speed = total_distance / outbound_time
    
    return speed