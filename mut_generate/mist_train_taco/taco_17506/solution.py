"""
QUESTION:
Hannibal is on a mission. He has to shoot a criminal. Hannibal was on the point (0, 0) and the criminal is on the point (Xc, Yc). But there is a wall between the point (X1, Y1) and (X2, Y2). 

You have to tell whether Hannibal can shoot criminal or not.

INPUT:

First line contains the total number of test cases T. For each test case, a single line contains space separated integers denoting X1, Y1, X2, Y2, Xc, Yc.

OUTPUT:

For each test case display YES, if Hannibal can shoot the criminal. Otherwise, display NO.

Constraints:

1 ≤ T ≤ 100

1 ≤ X, Y ≤ 1000000

SAMPLE INPUT
2
1 1 2 2 3 3
2 2 3 3 1 1

SAMPLE OUTPUT
NO
YES
"""

def can_hannibal_shoot(X1, Y1, X2, Y2, Xc, Yc):
    o1 = Yc * (X2 - Xc) - Xc * (Y2 - Yc)
    o2 = Yc * (X1 - Xc) - Xc * (Y1 - Yc)
    o3 = (Y2 - Y1) * X1 - Y1 * (X2 - X1)
    o4 = (Y2 - Y1) * (X1 - Xc) - (Y1 - Yc) * (X2 - X1)
    
    if o1 * o2 < 0 and o3 * o4 < 0:
        return "NO"
    elif o1 == 0 and X2 <= Xc and Y2 <= Yc and o2 == 0 and X1 <= Xc and Y1 <= Yc:
        return "NO"
    else:
        return "YES"