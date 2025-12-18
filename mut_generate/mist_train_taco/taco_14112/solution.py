"""
QUESTION:
Jim likes to play with laser beams. 

Jim stays at point $(0,0)$. 

There is a mirror at point $(X_m,Y_m)$ and a wall between points $(X_1,Y_1)$ and $(X_2,Y_2)$.

Jim wants to find out if he can point the laser beam on the mirror.

Input Format 

First line contains the number of test cases, ${T}$. 

Each subsequent line contains one test case: space separated integers that denote endpoints of the wall $X_1,Y_1$, $X_2,Y_2$ and position of the mirror $X_m,Y_m$.  

Output Format 

The answer for each test case: Display YES if Jim can point the laser beam to the mirror, otherwise display NO .  

Constraints 

$1\leq T\leq100$ 

$0≤|X_1|,|Y_1|,|X_2|,|Y_2|,|X_m|,|Y_m|≤10^6$ 

Mirror doesn't have common points with wall. 

Wall doesn't pass through the point $(0,0)$.  

Sample Input

5
1 2 2 1 2 2
-1 1 1 1 1 -1
1 1 2 2 3 3
2 2 3 3 1 1
0 1 1 1 0 2

Sample Output

NO
YES
NO
YES
NO
"""

def can_point_laser_to_mirror(X1, Y1, X2, Y2, Xm, Ym):
    """
    Determines if Jim can point the laser beam from (0,0) to the mirror at (Xm, Ym) without hitting the wall defined by (X1, Y1) and (X2, Y2).

    Parameters:
    X1, Y1 (int): Coordinates of the first endpoint of the wall.
    X2, Y2 (int): Coordinates of the second endpoint of the wall.
    Xm, Ym (int): Coordinates of the mirror.

    Returns:
    str: "YES" if Jim can point the laser beam to the mirror, otherwise "NO".
    """
    
    def det(a, b, c, d, e, f):
        return (a - e) * (d - f) - (b - f) * (c - e)
    
    if det(X1, Y1, X2, Y2, Xm, Ym) == 0 and det(X1, Y1, X2, Y2, 0, 0) == 0:
        return 'YES' if (0 - X1) * (Xm - X1) >= 0 and (0 - Y1) * (Ym - Y1) >= 0 else 'NO'
    elif det(X1, Y1, X2, Y2, Xm, Ym) * det(X1, Y1, X2, Y2, 0, 0) <= 0 and det(0, 0, Xm, Ym, X1, Y1) * det(0, 0, Xm, Ym, X2, Y2) <= 0:
        return 'NO'
    else:
        return 'YES'