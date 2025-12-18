"""
QUESTION:
Write a program which prints the central coordinate ($cx$,$cy$) and the radius $r$ of a incircle of a triangle which is constructed by three points ($x_1$, $y_1$), ($x_2$, $y_2$) and ($x_3$, $y_3$) on the plane surface.

Constraints

* $-10000 \leq x_i, y_i \leq 10000$
* The three points are not on the same straight line

Input

The input is given in the following format


$x_1$ $y_1$
$x_2$ $y_2$
$x_3$ $y_3$


All the input are integers.

Output

Print $cx$, $cy$ and $r$ separated by a single space in a line. The output values should be in a decimal fraction with an error less than 0.000001.

Examples

Input

1 -2
3 2
-2 0


Output

0.53907943898209422325 -0.26437392711448356856 1.18845545916395465278


Input

0 3
4 0
0 0


Output

1.00000000000000000000 1.00000000000000000000 1.00000000000000000000
"""

import math

def calculate_incircle(x1, y1, x2, y2, x3, y3):
    # Calculate the side lengths of the triangle
    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the radius of the incircle
    r = math.sqrt(s * (s - a) * (s - b) * (s - c)) / s
    
    # Calculate the coordinates of the incenter
    (xa, ya) = (x1 + (x2 - x1) * c / (b + c), y1 + (y2 - y1) * c / (b + c))
    (xb, yb) = (x2 + (x3 - x2) * a / (a + c), y2 + (y3 - y2) * a / (a + c))
    
    if xa - x3 != 0 and xb - x1 != 0:
        (a1, b1) = ((ya - y3) / (xa - x3), -((ya - y3) / (xa - x3)) * x3 + y3)
        (a2, b2) = ((yb - y1) / (xb - x1), -((yb - y1) / (xb - x1)) * x1 + y1)
        cx = (b2 - b1) / (a1 - a2)
        cy = a1 * cx + b1
    elif xa - x3 == 0:
        cx = x3
        (a2, b2) = ((yb - y1) / (xb - x1), -((yb - y1) / (xb - x1)) * x1 + y1)
        cy = a2 * cx + b2
    elif xb - x1 == 0:
        cx = x1
        (a1, b1) = ((ya - y3) / (xa - x3), -((ya - y3) / (xa - x3)) * x3 + y3)
        cy = a1 * cx + b1
    
    return cx, cy, r