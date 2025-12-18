"""
QUESTION:
You are given a spaceship that accelerates from rest to 80% the speed of light and then decelerates back to rest. The acceleration and deceleration phases take up a constant proportion, K (0 < K <= 0.5), of the total trip distance. Write a function `trip_duration` that calculates the total time taken for the trip from Proxima Centauri to Earth (a distance of 4.24 light-years) under the effects of special relativity, given the proportion K and the acceleration a. The function should take in parameters `K` and `a`, and return the total time in years.
"""

import math

def trip_duration(K, a):
    """
    Calculate the total time taken for a trip from Proxima Centauri to Earth under the effects of special relativity.

    Parameters:
    K (float): The proportion of the total trip distance for the acceleration and deceleration phases.
    a (float): The acceleration of the spaceship.

    Returns:
    float: The total time taken for the trip in years.
    """
    
    c = 299792458  # Speed of light in m/s
    v_max = 0.8 * c  # Maximum speed (80% of the speed of light)
    distance = 4.24 * 9.461e15  # Distance from Proxima Centauri to Earth in meters

    # Calculate time for acceleration and deceleration phases
    t_acc_dec = (c / a) * (math.asinh((v_max * math.sqrt(1 - (v_max**2 / c**2))) / c))

    # Calculate time for cruising phase
    t_cruise = ((1 - 2 * K) * distance) / v_max

    # Calculate total time
    total_time = (t_acc_dec + t_cruise) / 31536000  # Convert to years

    return total_time