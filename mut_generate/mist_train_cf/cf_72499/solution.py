"""
QUESTION:
Write a function `calculate_mean_velocity` that calculates the mean velocity of a round trip. The function takes two velocities (in km/h) and a distance (in km) as input and returns the mean velocity of the trip. The velocities are for the two legs of the trip (there and back). The distance is for one leg of the trip, and the same distance is used for the return leg.
"""

def calculate_mean_velocity(v1, v2, d):
    """
    Calculate the mean velocity of a round trip.

    Parameters:
    v1 (float): Velocity from Alpha to Bravo (km/h)
    v2 (float): Velocity from Bravo to Alpha (km/h)
    d (float): Distance from Alpha to Bravo (km)

    Returns:
    float: The mean velocity of the trip (km/h)
    """
    # time from Alpha to Bravo (h)
    t1 = d/v1

    # time from Bravo to Alpha (h)
    t2 = d/v2

    # total time (h)
    total_time = t1 + t2

    # total displacement (km) 
    # since it's a round trip, the total displacement is twice the distance from Alpha to Bravo
    total_displacement = 2*d

    # mean velocity (km/h)
    mean_velocity = total_displacement/total_time

    return mean_velocity