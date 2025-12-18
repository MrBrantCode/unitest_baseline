"""
QUESTION:
Problem

You brought a flat, holeless donut with a $ W $ horizontal $ H $ vertical $ H $ rectangle for ACPC.
Place this donut on the $ 2 $ dimension plane coordinate $ (0,0) $ with the center of the donut so that the side of length H and the $ y $ axis are parallel.


On the ACPC $ 1 $ day you ate a donut that was in the range of $ w $ vertical $ h $ centered on the coordinates ($ x $, $ y $).
If you want to eat the same amount on the $ 2 $ and $ 3 $ days, divide the donut by a straight line passing through the coordinates $ (0,0) $, and the sum of the donut areas in the area on one side of the straight line is on the other side I want it to be equal to the sum of the donut areas in the area of.


Find one slope of such a straight line.

Constraints

The input satisfies the following conditions.

* $ 1 \ lt h \ lt H \ lt 10 ^ 6 $
* $ 1 \ lt w \ lt W \ lt 10 ^ 6 $
* $ 1 \ le y \ le (h / 2 + H-1)-H / 2 $
* $ 1 \ le x \ le (w / 2 + W-1)-W / 2 $
* $ W $, $ H $, $ w $, $ h $ are even numbers

Input

The input is given in the following format.


$ W $ $ H $ $ w $ $ h $ $ x $ $ y $


Output

Output the slope of a straight line in one line. If the absolute error or relative error is $ 10 ^ {-6} $ or less, the answer is correct.

Examples

Input

6000 5000 20 10 400 300


Output

0.75


Input

10 10 8 8 8 8


Output

1
"""

def calculate_slope(W, H, w, h, x, y):
    a = min(W // 2, x + w // 2) + max(-W // 2, x - w // 2)
    b = min(H // 2, y + h // 2) + max(-H // 2, y - h // 2)
    return b / a