"""
QUESTION:
n evenly spaced points have been marked around the edge of a circle. There is a number written at each point. You choose a positive real number k. Then you may repeatedly select a set of 2 or more points which are evenly spaced, and either increase all numbers at points in the set by k or decrease all numbers at points in the set by k. You would like to eventually end up with all numbers equal to 0. Is it possible?

A set of 2 points is considered evenly spaced if they are diametrically opposed, and a set of 3 or more points is considered evenly spaced if they form a regular polygon.


-----Input-----

The first line of input contains an integer n (3 ≤ n ≤ 100000), the number of points along the circle.

The following line contains a string s with exactly n digits, indicating the numbers initially present at each of the points, in clockwise order.


-----Output-----

Print "YES" (without quotes) if there is some sequence of operations that results in all numbers being 0, otherwise "NO" (without quotes).

You can print each letter in any case (upper or lower).


-----Examples-----
Input
30
000100000100000110000000001100

Output
YES

Input
6
314159

Output
NO



-----Note-----

If we label the points from 1 to n, then for the first test case we can set k = 1. Then we increase the numbers at points 7 and 22 by 1, then decrease the numbers at points 7, 17, and 27 by 1, then decrease the numbers at points 4, 10, 16, 22, and 28 by 1.
"""

import math

def can_all_numbers_be_zero(n: int, pts: list) -> str:
    """
    Determines if it is possible to make all numbers at evenly spaced points on a circle equal to zero.

    Parameters:
    n (int): The number of points along the circle.
    pts (list): A list of digits indicating the numbers initially present at each of the points, in clockwise order.

    Returns:
    str: "YES" if it is possible to make all numbers zero, otherwise "NO".
    """
    x, y = 0, 0
    for j in [7, 11, 13, 17, 19, 23, 29, 31, 37, 1193, 1663, 2711, 4007, 65537]:
        if math.gcd(n, j) == 1:
            for i in range(n):
                k = int(pts[i])
                x += k * math.cos(math.pi * 2 * i * j / n)
                y += k * math.sin(math.pi * 2 * i * j / n)
            if not (abs(x) < 1e-06 and abs(y) < 1e-06):
                return 'NO'
    return 'YES'