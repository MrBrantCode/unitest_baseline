"""
QUESTION:
Fox Ciel has a robot on a 2D plane. Initially it is located in (0, 0). Fox Ciel code a command to it. The command was represented by string s. Each character of s is one move operation. There are four move operations at all:  'U': go up, (x, y)  →  (x, y+1);  'D': go down, (x, y)  →  (x, y-1);  'L': go left, (x, y)  →  (x-1, y);  'R': go right, (x, y)  →  (x+1, y). 

The robot will do the operations in s from left to right, and repeat it infinite times. Help Fox Ciel to determine if after some steps the robot will located in (a, b).


-----Input-----

The first line contains two integers a and b, ( - 10^9 ≤ a, b ≤ 10^9). The second line contains a string s (1 ≤ |s| ≤ 100, s only contains characters 'U', 'D', 'L', 'R') — the command.


-----Output-----

Print "Yes" if the robot will be located at (a, b), and "No" otherwise.


-----Examples-----
Input
2 2
RU

Output
Yes

Input
1 2
RU

Output
No

Input
-1 1000000000
LRRLU

Output
Yes

Input
0 0
D

Output
Yes



-----Note-----

In the first and second test case, command string is "RU", so the robot will go right, then go up, then right, and then up and so on.

The locations of its moves are (0, 0)  →  (1, 0)  →  (1, 1)  →  (2, 1)  →  (2, 2)  →  ...

So it can reach (2, 2) but not (1, 2).
"""

from math import hypot

def will_robot_reach_target(a: int, b: int, s: str) -> str:
    dx, dy = 0, 0
    
    # Calculate the net movement after one full cycle of the command string
    for move in s:
        if move == 'R':
            dx += 1
        elif move == 'L':
            dx -= 1
        elif move == 'D':
            dy -= 1
        elif move == 'U':
            dy += 1
    
    # Check if the target is already reachable after one cycle
    if dx == a and dy == b:
        return 'Yes'
    
    # If the net movement is zero, check if the target is (0, 0)
    if dx == 0 and dy == 0:
        return 'Yes' if a == 0 and b == 0 else 'No'
    
    # Calculate the number of full cycles needed to get close to the target
    lngt = int(max(0, hypot(a, b) / hypot(dx, dy) - 500))
    x, y = dx * lngt, dy * lngt
    
    # Simulate the movement for additional steps
    for _ in range(1000):
        for move in s:
            if x == a and y == b:
                return 'Yes'
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'D':
                y -= 1
            elif move == 'U':
                y += 1
            if x == a and y == b:
                return 'Yes'
    
    return 'No'