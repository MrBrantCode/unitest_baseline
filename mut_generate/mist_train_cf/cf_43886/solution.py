"""
QUESTION:
Compute the volume of a trapezoid with the formula V = (b1 + b2)/2 * h * l, where V is the volume, b1 is the bottom base, b2 is the top base, h is the height, and l is the length. Create a function `trapezoidal_reservoir_volume` that takes in the bottom base, top base, height, and length as parameters.
"""

def trapezoidal_reservoir_volume(b1, b2, h, l):
    """
    Compute the volume of a trapezoid with the formula V = (b1 + b2)/2 * h * l.
    
    Parameters:
    b1 (float): The bottom base of the trapezoid.
    b2 (float): The top base of the trapezoid.
    h (float): The height of the trapezoid.
    l (float): The length of the trapezoid.
    
    Returns:
    float: The volume of the trapezoid.
    """
    return (b1 + b2) / 2 * h * l