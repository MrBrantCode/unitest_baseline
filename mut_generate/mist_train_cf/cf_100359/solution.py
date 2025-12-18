"""
QUESTION:
Write a function `convert_to_decimal(degrees, minutes, seconds, direction)` that takes in degrees, minutes, seconds, and direction ('N', 'S', 'E', or 'W') and returns the corresponding decimal latitude or longitude. The function should account for the Earth's curvature and the observer's position relative to the Equator and Prime Meridian.
"""

def convert_to_decimal(degrees, minutes, seconds, direction):
    """
    Converts coordinates in degrees, minutes, and seconds to decimal format
    using the observer's position relative to the Equator and Prime Meridian.
    """
    # Convert to decimal degrees
    decimal_degrees = degrees + minutes/60.0 + seconds/3600.0

    # Determine the sign of the coordinate based on the direction
    sign = 1 if direction in ['N', 'E'] else -1

    # Calculate the latitude or longitude in decimal format
    decimal_coord = sign * decimal_degrees

    return decimal_coord