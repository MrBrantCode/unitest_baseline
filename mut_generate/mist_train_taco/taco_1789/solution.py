"""
QUESTION:
Problem

Find the area of ​​a regular N / K polygon inscribed in a circle with a radius of 1.

However, a regular N / K polygon is defined as "the outermost figure that takes N points on the circumference at equal intervals and connects each point every K-1".

For example, a 5/2 polygon can be drawn as follows. First, take five points at equal intervals on the circumference of radius 1.

Sample Input 2 diagram


Next, connect each point every other 2-1 = 1.

Sample Input 2 diagram


The outermost figure is a regular 5/2 square.

Sample Input 2 diagram

Constraints

The input satisfies the following constraints.

* 5 ≤ N ≤ 106
* 1 <K <N / 2
* N and K are integers that are relatively prime

Input

The input is given in the following format.


N K


Two integers N and K are given on one line.

Output

Output the area of ​​a regular N / K polygon inscribed in a circle with a radius of 1 on one line. An error of 10-5 or less is acceptable.

Examples

Input

5 2


Output

1.12256994


Input

20 3


Output

2.93114293


Input

7 3


Output

1.08395920


Input

100000 3


Output

3.14159265
"""

import math

def calculate_inscribed_polygon_area(N: int, K: int) -> float:
    PI = 3.141592653589793
    return N * math.sin(PI / N) * math.cos(K * PI / N) / math.cos((K - 1) * PI / N)