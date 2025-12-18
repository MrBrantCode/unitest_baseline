"""
QUESTION:
Given a ship that sails at 25 km/h for 2 hours, then at 30 km/h for 2 hours, and then encounters a current that reduces its speed by a factor 'n' (0 < n < 1) for 2 hours, write a function `travel_info(n)` to calculate the total distance traveled after 6 hours, the actual average speed, and the additional time it would take to travel the same distance without the current. The function should return the results accurate to 2 decimal places.
"""

def travel_info(n):
    """
    Calculate the total distance traveled after 6 hours, the actual average speed, 
    and the additional time it would take to travel the same distance without the current.

    Args:
    n (float): The factor by which the current reduces the speed (0 < n < 1)

    Returns:
    tuple: A tuple containing the total distance traveled, the actual average speed, 
           and the additional time it would take to travel the same distance without the current.
    """
    speed_1 = 25 
    time_1 = 2 
    speed_2 = 30 
    time_2 = 2 
    time_current = 2 
    speed_current = speed_2 * n 

    distance_1 = speed_1 * time_1 
    distance_2 = speed_2 * time_2 
    distance_current = speed_current * time_current 

    total_distance = distance_1 + distance_2 + distance_current 
    total_time = time_1 + time_2 + time_current 

    average_speed = total_distance / total_time 

    time_without_current = total_distance / speed_2 

    return round(total_distance, 2), round(average_speed, 2), round(time_without_current - total_time, 2)