"""
QUESTION:
Write a function named `calculate_average_velocity` to calculate the average velocity for a round trip where the same route is traversed at two different speeds. The function should take two parameters: `speed_downhill` and `speed_uphill`, both in km/h, which represent the speeds for the downhill and uphill portions of the trip, respectively. The total distance for each portion is the same.
"""

def calculate_average_velocity(speed_downhill, speed_uphill):
    """
    Calculate the average velocity for a round trip.

    The function takes two parameters: speed_downhill and speed_uphill, 
    both in km/h, which represent the speeds for the downhill and uphill 
    portions of the trip, respectively.

    Returns:
    float: The average velocity in km/h.
    """
    # Since the displacement is zero for a round trip, the average velocity is zero.
    return 0