"""
QUESTION:
All Indian Robotic Challenge (AIRC) is going to be held in NIT Raipur.Ajeet a student of nitrr want to participate in it and win it. In airc person whose robots will reach faster to end point will win .speed of bot is 20meters/Min.Ajeet want to Know the time Required by Bot to complete the following distance .

Note:-Truncate the Fraction Part of result. 

Input 
First line of Input Contain Number Of Test Case T.Next T lines contain a singe integer D in Meters.

Output 
Output a single integer T Time required to complete the following Distance in Seconds.

SAMPLE INPUT
5
30
45
60
20
40

SAMPLE OUTPUT
90
135
180
60
120
"""

def calculate_time_to_complete_distance(distance_meters):
    """
    Calculate the time required for a robot to complete a given distance in meters.
    
    The robot's speed is 20 meters per minute. The result is truncated to the nearest integer.
    
    Parameters:
    distance_meters (int or float): The distance in meters that the robot needs to travel.
    
    Returns:
    int: The time required to complete the distance in seconds, truncated to the nearest integer.
    """
    time_seconds = int((distance_meters * 60) / 20)
    return time_seconds