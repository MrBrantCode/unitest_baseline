"""
QUESTION:
Read problems statements in [Hindi], [Mandarin Chinese], [Russian], [Vietnamese], and [Bengali] as well.

Chefland is a big city which consists of infinite number of junctions on a 2D plane. The junctions are depicted below and they form a hexagonal grid — they satisfy the following conditions:
Two of the junctions have coordinates $(0,0)$ and $(1,0)$.
Each junction $J$ is connected by line segments with six other junctions. These junctions are the vertices of a regular hexagon with side length $1$ and their distances from $J$ are also all equal to $1$.

Chef created a robot that can traverse the junctions. Initially, it is in some junction and oriented towards another junction which is connected to it by a line segment. The robot accepts a string of instructions — decimal digits $0$ through $5$. It executes the instructions one by one and stops after executing the final instruction. When the robot executes an instruction denoted by a digit $d$, it first rotates by $60 \cdot d$ degrees counterclockwise and then moves $1$ unit forward, to the junction it is oriented towards.

Chef wants to test the robot, so he wrote a string $S$ of $N$ instructions. You should answer $Q$ queries. In each query, Chef wants to give the robot a substring of instructions $S_{L}, S_{L+1}, \ldots, S_{R}$; the robot starts in the junction $(0, 0)$ and it is oriented towards $(1, 0)$. You should find the final position (the $x$- and $y$-coordinates) of the robot.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $Q$.
The second line contains a single string $S$ with length $N$.
$Q$ lines follow. Each of these lines contains two space-separated integers $L$ and $R$ describing a query.

------  Output ------
For each query, print a single line containing two space-separated real numbers — the coordinates of the robot. Your answer will be considered correct if the absolute or relative error of each coordinate does not exceed $10^{-6}$.

Warning: Outputting more than 8 digits after floating point may result in exceeding output size limit and receiving "Runtime error" verdict.

------  Constraints  ------
$1 ≤ T ≤ 1,000$
$1 ≤ N, Q ≤ 2 \cdot 10^{5}$
$1 ≤ L ≤ R ≤ N$
$S$ contains only characters '0', '1', '2', '3', '4' and '5'
the sum of $N$ over all test cases does not exceed $10^{6}$
the sum of $Q$ over all test cases does not exceed $10^{6}$

------  Example Input ------

1
3 3
012
1 1
1 2
2 2

------  Example Output ------

1.00000000 0.00000000
1.50000000 0.86602540
0.50000000 0.86602540
"""

import math

def calculate_robot_position(N, Q, S, queries):
    sin = {}
    cos = {}
    sin[0] = 0
    sin[60] = pow(3, 0.5) / 2
    sin[120] = sin[60]
    sin[180] = 0
    sin[240] = -sin[60]
    sin[300] = -sin[60]
    cos[0] = 1
    cos[60] = 0.5
    cos[120] = -0.5
    cos[180] = -1
    cos[240] = -0.5
    cos[300] = 0.5

    Position = {}
    Angle = {}
    x = 0
    y = 0
    A = 0
    d = 60
    i = 0
    Position[i] = (0, 0)
    Angle[i] = 0

    for item in S:
        A = A + 60 * int(item)
        if A >= 360:
            A = A % 360
        i = i + 1
        Position[i] = (Position[i - 1][0] + cos[A], Position[i - 1][1] + sin[A])
        Angle[i] = A

    results = []
    for L, R in queries:
        pr = Position[R]
        p1 = Position[L - 1]
        moveinx = pr[0] - p1[0]
        moveiny = pr[1] - p1[1]
        i = Angle[L - 1]
        ci = math.cos(i * math.pi / 180)
        si = math.sin(i * math.pi / 180)
        ans1 = moveinx * ci + moveiny * si
        ans2 = -moveinx * si + moveiny * ci
        results.append((ans1, ans2))
    
    return results