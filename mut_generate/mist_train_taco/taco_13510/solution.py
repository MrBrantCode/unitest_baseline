"""
QUESTION:
Chef is stuck on the minute hand of a giant clock. To escape from this clock he needs to get onto the hour hand which has an exit door. 
Since the minute hand and and hour hand are not connected at any point, chef will surely need to make a jump. Since he wants minimum risks, he chooses to jump on the hour hand so that the angle he has to cover is minimum possible.
You will be given a clock time in $UTC$ format denoting time of chef's jump and you have to compute the minimum angle that chef needs to cover while completing the jump.
For some reason chef times his jump only when the number of minutes is a multiple of 5.

-----Input:-----
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of  $T$ test cases follows.
The first line of each test case contains a string denoting time in UTC format (e.g. 10:20 i.e. 10 hours and 20 minutes)

-----Output-----
For each test case, print a single line denoting the smallest angle of jump.

-----Constraints-----
- $1 \leq T \leq 10^3$
- $0 \leq hours \leq 23$
- $0 \leq minutes \leq 59$

-----Example Input-----
3
14:20
02:10
09:30

-----Example Output-----
50 degree 
5 degree  
105 degree

-----Explanation-----
- In the second case, once the hour hand reaches 2 it starts moving towards 3 with the passing of every minute, hence when the minute hand points 10 minutes, the hour hand has already covered some angle towards 3. 
In this scenario the two angles made by hour and minute hand are 355 and 5 degrees. Since chef will jump on the side with minimum angle, he chooses the one with 5-degree angle.
"""

def calculate_minimum_jump_angle(time_str: str) -> str:
    # Split the input time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    
    # Normalize hours to 12-hour format
    hours_12 = hours % 12
    
    # Ensure minutes are a multiple of 5
    if minutes % 5 != 0:
        minutes = (minutes // 5) * 5 + 5
    
    # Calculate the angle of the hour hand
    hour_angle = (hours_12 * 30) + (0.5 * minutes)
    hour_angle %= 360
    
    # Calculate the angle of the minute hand
    minute_angle = (minutes // 5) * 30
    minute_angle %= 360
    
    # Calculate the two possible angles between the hour and minute hands
    if hour_angle > minute_angle:
        angle1 = hour_angle - minute_angle
        angle2 = 360 - angle1
    else:
        angle1 = minute_angle - hour_angle
        angle2 = 360 - angle1
    
    # Determine the minimum angle
    min_angle = min(angle1, angle2)
    
    # Convert the angle to an integer if it is a whole number
    if min_angle == int(min_angle):
        min_angle = int(min_angle)
    
    # Return the result as a string with the "degree" suffix
    return f"{min_angle} degree"