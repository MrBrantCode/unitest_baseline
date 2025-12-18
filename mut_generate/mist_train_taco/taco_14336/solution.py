"""
QUESTION:
In Subodh's CS Deparment there is a contest of Geometry. In this contest students are told to find minimum angle between hour and minute hand.

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

def calculate_min_angle(H: int, M: int) -> float:
    # Normalize hour to 12-hour format
    H = H % 12
    
    # Calculate the angle of the hour hand
    hour_angle = (H * 60 + M) / 2
    
    # Calculate the angle of the minute hand
    minute_angle = M * 6
    
    # Calculate the absolute difference between the two angles
    angle_difference = abs(hour_angle - minute_angle)
    
    # Find the minimum angle
    min_angle = min(angle_difference, 360 - angle_difference)
    
    return min_angle