"""
QUESTION:
In PIET's CS Deparment there is a contest of Geometry. In this contest students are told to find minimum angle between hour and minute hand.

Input:
The first line contains the number of test cases, T. T lines follow, each of which contains two integer Hour hand H and minute hand M .

Output:
Print the minimum angle between the hands.

Constraints
1 ≤ T ≤ 100 
01 ≤ H ≤ 12
01 ≤ M ≤ 59 

SAMPLE INPUT
2
12 30
06 00

SAMPLE OUTPUT
165 
180

Explanation

In first input time is 12:30 i.e. hour hand is in middle of 12 and 1 & minute hand is pointing at 6 which makes angle of 165 degrees. 

In Second input time is 06:00 i.e. hour hand is at 12 and minute hand is at 6 which makes angle of 180 degrees.
"""

def calculate_min_angle(hh: int, mm: int) -> float:
    """
    Calculate the minimum angle between the hour and minute hands on a clock.

    Parameters:
    hh (int): The hour hand position (0 ≤ hh ≤ 12).
    mm (int): The minute hand position (0 ≤ mm ≤ 59).

    Returns:
    float: The minimum angle between the hour and minute hands.
    """
    # Normalize hour to 12-hour format
    hh = hh % 12
    
    # Calculate the angle of the hour hand
    hour_angle = hh * 30 + mm * 0.5
    
    # Calculate the angle of the minute hand
    minute_angle = mm * 6
    
    # Calculate the absolute difference between the two angles
    angle_diff = abs(hour_angle - minute_angle)
    
    # The minimum angle is the smaller of the angle difference or 360 minus the angle difference
    min_angle = min(angle_diff, 360 - angle_diff)
    
    return min_angle