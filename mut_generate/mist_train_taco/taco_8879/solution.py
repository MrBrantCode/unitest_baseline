"""
QUESTION:
Two fishing vessels are sailing the open ocean, both on a joint ops fishing mission.

On a high stakes, high reward expidition - the ships have adopted the strategy of hanging a net between the two ships.

The net is **40 miles long**. Once the straight-line distance between the ships is greater than 40 miles, the net will tear, and their valuable sea harvest will be lost! We need to know how long it will take for this to happen.

Given the bearing of each ship, find the time **in minutes** at which the straight-line distance between the two ships reaches **40 miles**. Both ships travel at **90 miles per hour**. At time 0, assume the ships have the same location.

Bearings are defined as **degrees from north, counting clockwise**.
These will be passed to your function as integers between **0 and 359** degrees.
Round your result to **2 decmal places**.


If the net never breaks, return float('inf')

Happy sailing!
"""

from math import sin, radians

def calculate_time_to_net_break(bearing_A: int, bearing_B: int) -> float:
    """
    Calculate the time in minutes at which the straight-line distance between two ships reaches 40 miles.

    Parameters:
    - bearing_A (int): Bearing of the first ship in degrees (0 to 359).
    - bearing_B (int): Bearing of the second ship in degrees (0 to 359).

    Returns:
    - float: Time in minutes at which the net will break, rounded to 2 decimal places. If the net never breaks, return float('inf').
    """
    a = radians(abs(bearing_A - bearing_B) / 2)
    if a == 0:
        return float('inf')
    time_in_hours = 40 / (3 * sin(a))
    time_in_minutes = time_in_hours * 60
    return round(time_in_minutes, 2)