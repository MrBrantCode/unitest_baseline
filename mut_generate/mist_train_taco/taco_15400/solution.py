"""
QUESTION:
Ayrat is looking for the perfect code. He decided to start his search from an infinite field tiled by hexagons. For convenience the coordinate system is introduced, take a look at the picture to see how the coordinates of hexagon are defined: 

[Image] [Image] Ayrat is searching through the field. He started at point (0, 0) and is moving along the spiral (see second picture). Sometimes he forgets where he is now. Help Ayrat determine his location after n moves.


-----Input-----

The only line of the input contains integer n (0 ≤ n ≤ 10^18) — the number of Ayrat's moves.


-----Output-----

Print two integers x and y — current coordinates of Ayrat coordinates.


-----Examples-----
Input
3

Output
-2 0

Input
7

Output
3 2
"""

import math

def calculate_spiral_coordinates(n):
    if n == 0:
        return (0, 0)
    
    x = math.floor(1 / 6 * ((12 * n - 3) ** 0.5 + 3))
    
    while True:
        d = n - (x ** 3 - (x - 1) ** 3)
        if d < 0:
            x -= 1
        elif d > x * 6 + 6:
            x += 1
        else:
            break
    
    s, r = divmod(d, x)
    
    if s == 0:
        return (2 * x - r - 1, 2 * r + 2)
    elif s == 1:
        return (x - 2 * r - 2, 2 * x)
    elif s == 2:
        return (-x - r - 1, 2 * (x - r - 1))
    elif s == 3:
        return (-2 * x + r + 1, -2 * r - 2)
    elif s == 4:
        return (-x + 2 * r + 2, -2 * x)
    elif s == 5:
        return (x + r + 1, -2 * x + 2 * r + 2)