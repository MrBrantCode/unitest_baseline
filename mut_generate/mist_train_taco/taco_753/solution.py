"""
QUESTION:
You are given two points $P$ and $Q$ and an opaque sphere in a three-dimensional space. The point $P$ is not moving, while $Q$ is moving in a straight line with constant velocity. You are also given a direction vector $d$ with the following meaning: the position of $Q$ at time $t$ is $Q(t) = Q(0) + d \cdot t$, where $Q(0)$ is the initial position of $Q$.
It is guaranteed that $Q$ is not visible from $P$ initially (at time $t=0$). It is also guaranteed that $P$ and $Q$ do not touch the sphere at any time.
Find the smallest positive time $t_v$ when $Q$ is visible from $P$, i.e. when the line segment connecting points $P$ and $Q$ does not intersect the sphere.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains 13 space-separated integers.
- The first three integers $P_x, P_y, P_z$ denote the coordinates of $P$.
- The next three integers $Q_x, Q_y, Q_z$ denote the initial coordinates of $Q$.
- The next three integers $d_x, d_y, d_z$ denote the components of the direction vector $d$.
- The last four integers $c_x, c_y, c_z, r$ denote the coordinates of the centre of the sphere and its radius.

-----Output-----
For each test case, print a single line containing one real number — the time $t_v$. Your answer will be considered correct if its absolute or relative error does not exceed $10^{-6}$. It is guaranteed that $t_v$ exists and does not exceed $10^9$.

-----Constraints-----
- $1 \le T \le 10^5$
- the absolute values of coordinates of all points do not exceed $2\cdot10^9$
- $1 \le r \le 10^9$

-----Subtasks-----
Subtask #1 (25 points): $P_z = Q_z = d_z = c_z = 0$
Subtask #2 (75 points): original constraints

-----Example Input-----
1
3 0 0 -10 -10 0 0 10 0 0 -3 0 3

-----Example Output-----
1.0000000000
"""

import math

def find_visibility_time(px, py, pz, qx, qy, qz, dx, dy, dz, cx, cy, cz, r):
    a = qx - px
    b = qy - py
    c = qz - pz
    k = px - cx
    l = py - cy
    m = pz - cz
    
    S1 = r ** 2 * (dx ** 2 + dy ** 2 + dz ** 2)
    S2 = (dx * l - dy * k) ** 2 + (dy * m - dz * l) ** 2 + (dz * k - dx * m) ** 2
    A = S1 - S2
    
    S1 = 2 * r ** 2 * (a * dx + b * dy + c * dz)
    S2 = 2 * ((a * l - b * k) * (dx * l - dy * k) + (b * m - c * l) * (dy * m - dz * l) + (c * k - a * m) * (dz * k - dx * m))
    B = S1 - S2
    
    S1 = r ** 2 * (a ** 2 + b ** 2 + c ** 2)
    S2 = (a * l - b * k) ** 2 + (b * m - c * l) ** 2 + (c * k - a * m) ** 2
    C = S1 - S2
    
    if A == 0:
        t = -1 * C / B
        return round(t, 10)
    else:
        t1 = (-1 * B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
        t2 = (-1 * B - math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
        
        if t1 < 0 and t2 < 0:
            return round(0, 10)
        elif t1 < 0:
            return round(t2, 10)
        elif t2 < 0:
            return round(t1, 10)
        elif t1 >= t2:
            return round(t1, 10)
        else:
            return round(t2, 10)