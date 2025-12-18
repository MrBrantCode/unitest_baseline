"""
QUESTION:
Create a program that outputs the surface area S of a square cone with a height of h, with a square with one side x as the base. However, assume that the line segment connecting the apex and the center of the base is orthogonal to the base. Also, x and h are positive integers less than or equal to 100.

Input

Given multiple datasets. Each dataset is given in the following format:


x
h


When both x and h are 0, it indicates the end of input.



Output

Output S (real number) on one line for each data set. The output may contain an error of 0.00001 or less.

Example

Input

6
4
7
9
0
0


Output

96.000000
184.192455
"""

from math import sqrt

def calculate_square_cone_surface_area(x: int, h: int) -> float:
    # Calculate the slant height of the cone
    sh = sqrt((x / 2) ** 2 + h ** 2)
    
    # Calculate the surface area
    S = x * x + sum([sh * x * 0.5 for _ in range(4)])
    
    return S