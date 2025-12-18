"""
QUESTION:
Write a function `calculate_distance` that calculates the Euclidean distance between two ships after `t` hours. The ships are traveling in opposite directions with speeds given by the functions `f(t) = t^2 - t + 20` and `g(t) = 2t^2 + 16`. The function should return the distance in kilometers. The input `t` is a non-negative number representing time in hours.
"""

def calculate_distance(t):
    """
    Calculate the Euclidean distance between two ships after 't' hours.
    
    Parameters:
    t (float): time in hours
    
    Returns:
    float: Euclidean distance in kilometers
    """
    return t**4/4 - t**3/3 + 18*t**2