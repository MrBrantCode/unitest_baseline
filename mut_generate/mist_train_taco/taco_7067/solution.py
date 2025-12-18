"""
QUESTION:
Given the time shown by a wall clock, you have to output the internal angle between the minute and hour hand of the clock.
(Wall Clock displays a 12 hour format.)

For instance, if the time shown is 01:00 , the angle between the hands is 30 degrees.

Input : Time in HH:MM format 
Output: The angle in degrees, correct up to 6 places of decimal.

SAMPLE INPUT
04:00

SAMPLE OUTPUT
120.000000
"""

def calculate_clock_angle(h: int, m: int) -> float:
    """
    Calculate the internal angle between the hour and minute hands of a clock.

    Parameters:
    h (int): The hour value from the time in HH:MM format.
    m (int): The minute value from the time in HH:MM format.

    Returns:
    float: The internal angle between the hour and minute hands, correct up to 6 decimal places.
    """
    # Calculate the angle of the hour hand
    ha = h * 30
    
    # Calculate the angle of the minute hand
    ma = m * 6
    
    # Adjust the hour hand angle for the minutes
    hma = float(m) / 2
    acha = ha + hma
    
    # Calculate the absolute difference between the two angles
    result = abs(acha - ma)
    
    # If the angle is greater than 180 degrees, subtract it from 360
    if result > 180:
        result = 360 - result
    
    # Return the result formatted to 6 decimal places
    return round(result, 6)