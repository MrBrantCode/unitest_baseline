"""
QUESTION:
The polar bears are going fishing. They plan to sail from (s_{x}, s_{y}) to (e_{x}, e_{y}). However, the boat can only sail by wind. At each second, the wind blows in one of these directions: east, south, west or north. Assume the boat is currently at (x, y).  If the wind blows to the east, the boat will move to (x + 1, y).  If the wind blows to the south, the boat will move to (x, y - 1).  If the wind blows to the west, the boat will move to (x - 1, y).  If the wind blows to the north, the boat will move to (x, y + 1). 

Alternatively, they can hold the boat by the anchor. In this case, the boat stays at (x, y). Given the wind direction for t seconds, what is the earliest time they sail to (e_{x}, e_{y})?


-----Input-----

The first line contains five integers t, s_{x}, s_{y}, e_{x}, e_{y} (1 ≤ t ≤ 10^5,  - 10^9 ≤ s_{x}, s_{y}, e_{x}, e_{y} ≤ 10^9). The starting location and the ending location will be different.

The second line contains t characters, the i-th character is the wind blowing direction at the i-th second. It will be one of the four possibilities: "E" (east), "S" (south), "W" (west) and "N" (north).


-----Output-----

If they can reach (e_{x}, e_{y}) within t seconds, print the earliest time they can achieve it. Otherwise, print "-1" (without quotes).


-----Examples-----
Input
5 0 0 1 1
SESNW

Output
4

Input
10 5 3 3 6
NENSWESNEE

Output
-1



-----Note-----

In the first sample, they can stay at seconds 1, 3, and move at seconds 2, 4.

In the second sample, they cannot sail to the destination.
"""

def find_earliest_arrival_time(t, s_x, s_y, e_x, e_y, wind_directions):
    # Determine the required wind directions to move towards the destination
    if s_y > e_y:
        required_y_direction = 'S'
    else:
        required_y_direction = 'N'
    
    if s_x > e_x:
        required_x_direction = 'W'
    else:
        required_x_direction = 'E'
    
    # Calculate the distance to cover in both x and y directions
    distance_x = abs(s_x - e_x)
    distance_y = abs(s_y - e_y)
    
    # Iterate through the wind directions to find the earliest time
    for i in range(t):
        if wind_directions[i] == required_x_direction:
            distance_x -= 1
        elif wind_directions[i] == required_y_direction:
            distance_y -= 1
        
        # If both distances are covered, return the current time
        if distance_x == 0 and distance_y == 0:
            return i + 1
    
    # If the destination is not reached within t seconds, return -1
    return -1