"""
QUESTION:
Bob is about to take a hot bath. 

There are two taps to fill the bath: a hot water tap and a cold water tap. The cold water's temperature is t1, and the hot water's temperature is t2. The cold water tap can transmit any integer number of water units per second from 0 to x1, inclusive. Similarly, the hot water tap can transmit from 0 to x2 water units per second.

If y1 water units per second flow through the first tap and y2 water units per second flow through the second tap, then the resulting bath water temperature will be:

<image>

Bob wants to open both taps so that the bath water temperature was not less than t0. However, the temperature should be as close as possible to this value. If there are several optimal variants, Bob chooses the one that lets fill the bath in the quickest way possible.

Determine how much each tap should be opened so that Bob was pleased with the result in the end.

Input

You are given five integers t1, t2, x1, x2 and t0 (1 ≤ t1 ≤ t0 ≤ t2 ≤ 106, 1 ≤ x1, x2 ≤ 106).

Output

Print two space-separated integers y1 and y2 (0 ≤ y1 ≤ x1, 0 ≤ y2 ≤ x2).

Examples

Input

10 70 100 100 25


Output

99 33

Input

300 500 1000 1000 300


Output

1000 0

Input

143 456 110 117 273


Output

76 54

Note

In the second sample the hot water tap shouldn't be opened, but the cold water tap should be opened at full capacity in order to fill the bath in the quickest way possible.
"""

import math

def optimal_tap_settings(t1, t2, x1, x2, t0):
    num1 = t2 - t0
    num2 = t0 - t1
    
    if t1 == t2:
        return (x1, x2)
    
    if num1 == 0:
        return (0, x2)
    
    if num2 == 0:
        return (x1, 0)
    
    z = num2 / num1
    maxa = 10 ** 18
    ans = (0, 0)
    
    for i in range(1, x1 + 1):
        ok = z * i
        if ok > x2:
            break
        num1 = i
        num2 = math.ceil(ok)
        if maxa == num2 / num1 - z and num2 + num1 > ans[0] + ans[1]:
            ans = (num1, num2)
        elif maxa > num2 / num1 - z:
            ans = (num1, num2)
            maxa = num2 / num1 - z
    
    if ans == (0, 0):
        ans = (0, x2)
    
    return ans