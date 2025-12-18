"""
QUESTION:
Write a function `brownian_motion_moment(n, t)` to calculate the nth moment of a standard Brownian motion Bt at time t, where n is a non-negative integer and t is a non-negative real number. The function should return the calculated moment value. Note that the Brownian motion starts at 0.
"""

import math

def brownian_motion_moment(n, t):
    """
    Calculate the nth moment of a standard Brownian motion Bt at time t.
    
    Parameters:
    n (int): The moment number, a non-negative integer.
    t (float): The time, a non-negative real number.
    
    Returns:
    float: The calculated moment value.
    """
    
    # Check if the moment number is even
    if n % 2 == 0:
        # Calculate the moment for even n
        k = n // 2
        moment = math.factorial(n) / (math.factorial(k) * 2 ** k) * t ** k
    else:
        # The moment is 0 for odd n
        moment = 0
    
    return moment