"""
QUESTION:
Problem

Gaccho has his favorite watch. One day the minute hand of the clock came off and I lost it somewhere. However, Gaccho wants to keep using the watch and wants to read the time with only the short hand.

Output the time (hour h, minute m) for the information θ of the short hand. A clock is a so-called analog clock, in which numbers 1 to 12 are arranged clockwise at regular intervals in ascending order.

Constraints

* 0 ≤ θ ≤ 359

Input

The input is given in the following format.


θ


An integer representing the angle θ of the short hand is given in one line in degrees. The direction pointed by the short hand is the direction rotated by θ degrees clockwise when the direction pointing to 12 o'clock is 0 degrees.

Output

The time when the hour hand takes a given angle
h m
Output in one line in the form of.

Since there is no distinction between morning and afternoon in the time, 0 ≤ h ≤ 11 is set.

Examples

Input

0


Output

0 0


Input

45


Output

1 30


Input

100


Output

3 20
"""

def calculate_time_from_angle(theta: int) -> tuple:
    """
    Calculate the time (hour and minute) from the given angle of the short hand.

    Parameters:
    theta (int): The angle of the short hand in degrees (0 ≤ θ ≤ 359).

    Returns:
    tuple: A tuple (h, m) where h is the hour (0 ≤ h ≤ 11) and m is the minute.
    """
    # Convert the angle to minutes (each degree corresponds to 2 minutes)
    total_minutes = theta * 2
    
    # Calculate the hour and minute
    hour = total_minutes // 60
    minute = total_minutes % 60
    
    return (hour, minute)