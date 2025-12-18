"""
QUESTION:
Tom is solving an IQ quiz in which he is stuck in a question which says that there are two circles whose center coordinates and radius are given. Now Tom has to find whether the two circles overlap, do not overlap or are tangential with each other. Help Tom in solving the problem.  

Input:
The input to the problem will be the coordinates for the center of each circle, followed by the radius of each circle. The first line of input represents the coordinates of first circle while second line of input represents the coordinate of second circle.

Output:  
The output will state whether the circles overlap, do not overlap, or are tangential.  

Assumptions:  
‘Y’ will indicate that the circles will overlap.  
‘N’ will indicate that the circles do not overlap.  
‘T’ will indicate that the circles are tangential.  

Constraints:
All inputs are integers that lie between 0 to 1000.   

Example:    

Input:
5 5 5 
15 5 5    

Output:
T

SAMPLE INPUT
100 60 52 
200 90 45

SAMPLE OUTPUT
N
"""

import math

def check_circle_overlap(center1, radius1, center2, radius2):
    def distance(p0, p1):
        return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    
    dist = distance(center1, center2)
    sum_of_radii = radius1 + radius2
    
    if dist == sum_of_radii:
        return 'T'
    elif dist > sum_of_radii:
        return 'N'
    else:
        return 'Y'