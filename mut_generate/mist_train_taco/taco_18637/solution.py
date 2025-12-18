"""
QUESTION:
Consider an analog clock whose hour and minute hands are A and B centimeters long, respectively.
An endpoint of the hour hand and an endpoint of the minute hand are fixed at the same point, around which each hand rotates clockwise at constant angular velocity. It takes the hour and minute hands 12 hours and 1 hour to make one full rotation, respectively.
At 0 o'clock, the two hands overlap each other. H hours and M minutes later, what is the distance in centimeters between the unfixed endpoints of the hands?

-----Constraints-----
 - All values in input are integers.
 - 1 \leq A, B \leq 1000
 - 0 \leq H \leq 11
 - 0 \leq M \leq 59

-----Input-----
Input is given from Standard Input in the following format:
A B H M

-----Output-----
Print the answer without units. Your output will be accepted when its absolute or relative error from the correct value is at most 10^{-9}.

-----Sample Input-----
3 4 9 0

-----Sample Output-----
5.00000000000000000000

The two hands will be in the positions shown in the figure below, so the answer is 5 centimeters.
"""

import math

def calculate_hand_distance(A: int, B: int, H: int, M: int) -> float:
    # Calculate the angles of the hour and minute hands in radians
    alpha = 2 * math.pi * H / 12 + math.pi / 6 * M / 60
    beta = 2 * math.pi * M / 60
    
    # Calculate the distance using the law of cosines
    distance = (A * A + B * B - 2 * A * B * math.cos(alpha - beta)) ** 0.5
    
    return distance