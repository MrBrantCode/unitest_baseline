"""
QUESTION:
Calculate the angle between the hour hand and minute hand. 
Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.
Example 1:
Input:
H = 9 , M = 0
Output:
90
Explanation:
The minimum angle between hour and minute
hand when the time is 9 is 90 degress.
Example 2:
Input:
H = 3 , M = 30
Output:
75
Explanation:
The minimum angle between hour and minute
hand when the time is 3:30 is 75 degress.
Your Task:
You don't need to read, input, or print anything. Your task is to complete the function getAngle(), which takes 2 Integers H and M as input and returns the answer.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ H ≤ 12
0 ≤ M < 60
H and M are Integers
"""

import math

def calculate_angle(H: int, M: int) -> int:
    # Calculate the angle of the minute hand
    minutes_angle = 360 / 60 * M
    
    # Calculate the angle of the hour hand
    hours_angle = 360 / 12 * H + M / 60 * (360 / 12)
    
    # Calculate the absolute difference between the two angles
    diff = abs(minutes_angle - hours_angle)
    
    # Return the minimum of the difference and 360 - difference, floored
    return math.floor(min(diff, 360 - diff))