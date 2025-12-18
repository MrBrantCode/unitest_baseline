"""
QUESTION:
Adam and Martha are planning to leave the city after their retirement and build a house in a huge land belonging to their family. To keep everyone happy, they want to build the house at a location having distance _a*d1_ from aunt Kimberly's house, where a is some ratio and d1 is the distance of that location to uncle Bob's house. Also, the house should be at a distance _b*d2_ from uncle Jack's house where b is some ratio and d2 is the distance of the location to aunt Janet's house.

You need to help them find the location of their house.

Input Format 

The first line of input contains two integers a and b (the ratios above). In the next four lines, there are 4 pairs of integers that indicate the coordinates of Kimberly's, Bob's, Jack's, and Janet's houses, respectively.

Output Format 

You must output the coordinate of house with exactly two points after decimal point (rounded to closest one hundredth). If there is no location satisfying the above constraints, output Impossible! If there are more than one possible locations, output a location with minimum  x-coordinate and among the ones having the minimum x-coordinate, a location with minimum y-coordinate. 

Constraints  

1 < a, b <= 1000

-1000 <= all input coordinates <= 1000

Sample Input  

3 4

4 0

0 0

-2 -4

-2 -1

Sample Output  

-2.00 0.00

Explanation 

As required, the point (-2.00, 0.00) has distance 2 from Bob's house and distance 3*2=6 from Kimberly's house. It also has distance 1 from Janet's house and distance 4*1=4 from Jack's house.
"""

from fractions import Fraction
from math import sqrt

def find_house_location(a, b, kimberly, bob, jack, janet):
    (xk, yk) = kimberly
    (xb, yb) = bob
    (xc, yc) = jack
    (xn, yn) = janet
    
    a2 = a * a
    x1 = Fraction(xk - a2 * xb, 1 - a2)
    y1 = Fraction(yk - a2 * yb, 1 - a2)
    r1sq = x1 * x1 + y1 * y1 - Fraction(xk * xk + yk * yk - a2 * (xb * xb + yb * yb), 1 - a2)
    
    b2 = b * b
    x2 = Fraction(xc - b2 * xn, 1 - b2)
    y2 = Fraction(yc - b2 * yn, 1 - b2)
    r2sq = x2 * x2 + y2 * y2 - Fraction(xc * xc + yc * yc - b2 * (xn * xn + yn * yn), 1 - b2)
    
    if x1 == x2 and y1 == y2:
        if r1sq == r2sq:
            x = float(x1) - sqrt(float(r1sq))
            y = float(y1)
            return (round(x, 2), round(y, 2))
        else:
            return "Impossible!"
    else:
        dsq = (x1 - x2) ** 2 + (y1 - y2) ** 2
        vsq = r1sq - (r1sq - r2sq + dsq) ** 2 / (4 * dsq)
        if vsq < 0:
            return "Impossible!"
        else:
            v = sqrt(float(vsq / dsq))
            u = float((r1sq - r2sq) / (2 * dsq))
            dx = float(x2 - x1)
            dy = float(y2 - y1)
            (x, y) = min((u * dx - v * dy, u * dy + v * dx), (u * dx + v * dy, u * dy - v * dx))
            x += float(x2 + x1) / 2
            y += float(y2 + y1) / 2
            return (round(x, 2), round(y, 2))