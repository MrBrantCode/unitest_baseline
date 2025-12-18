"""
QUESTION:
The Happy Farm 5 creators decided to invent the mechanism of cow grazing. The cows in the game are very slow and they move very slowly, it can even be considered that they stand still. However, carnivores should always be chased off them. 

For that a young player Vasya decided to make the shepherd run round the cows along one and the same closed path. It is very important that the cows stayed strictly inside the area limited by the path, as otherwise some cows will sooner or later be eaten. To be absolutely sure in the cows' safety, Vasya wants the path completion time to be minimum.

The new game is launched for different devices, including mobile phones. That's why the developers decided to quit using the arithmetics with the floating decimal point and use only the arithmetics of integers. The cows and the shepherd in the game are represented as points on the plane with integer coordinates. The playing time is modeled by the turns. During every turn the shepherd can either stay where he stands or step in one of eight directions: horizontally, vertically, or diagonally. As the coordinates should always remain integer, then the length of a horizontal and vertical step is equal to 1, and the length of a diagonal step is equal to <image>. The cows do not move. You have to minimize the number of moves the shepherd needs to run round the whole herd.

Input

The first line contains an integer N which represents the number of cows in the herd (1 ≤ N ≤ 105). Each of the next N lines contains two integers Xi and Yi which represent the coordinates of one cow of (|Xi|, |Yi| ≤ 106). Several cows can stand on one point.

Output

Print the single number — the minimum number of moves in the sought path.

Examples

Input

4
1 1
5 1
5 3
1 3


Output

16

Note

Picture for the example test: The coordinate grid is painted grey, the coordinates axes are painted black, the cows are painted red and the sought route is painted green.

<image>
"""

import math

def calculate_minimum_moves(cows):
    def orientation(p0, p1, p2):
        x = (p1[1] - p0[1]) * (p2[0] - p1[0]) - (p1[0] - p0[0]) * (p2[1] - p1[1])
        if x < 0:
            return -1
        if x > 0:
            return 1
        return 0

    cows = list(set(cows))
    n = len(cows)
    
    if n == 0:
        return 0
    
    pmin = 0
    for i in range(1, n):
        if cows[i][1] < cows[pmin][1] or (cows[i][1] == cows[pmin][1] and cows[i][0] < cows[pmin][0]):
            pmin = i
    (cows[pmin], cows[0]) = (cows[0], cows[pmin])

    cows = [(p[0] - cows[0][0], p[1] - cows[0][1]) for p in cows[1:]]
    cows.sort(key=lambda p: (-p[0] / p[1] if p[1] != 0 else -1000000000000000.0, p[0] ** 2 + p[1] ** 2))
    cows = [(0, 0)] + cows

    t = [cows[0]]
    i = 1
    n = len(cows)
    while 1:
        while i < n - 1 and orientation(cows[0], cows[i], cows[i + 1]) == 0:
            i += 1
        if i >= n - 1:
            break
        t.append(cows[i])
        i += 1
    t.append(cows[-1])

    if len(t) == 1:
        return 4
    elif len(t) == 2:
        return max(abs(t[1][1] - t[0][1]), abs(t[1][0] - t[0][0])) * 2 + 4
    else:
        stack = [t[0], t[1], t[2]]
        for i in range(3, len(t)):
            while orientation(stack[-2], stack[-1], t[i]) == 1:
                stack.pop()
            stack.append(t[i])
        
        n = len(stack)
        s = 4
        for i in range(n - 1):
            s += max(abs(stack[i + 1][1] - stack[i][1]), abs(stack[i + 1][0] - stack[i][0]))
        s += max(abs(stack[0][1] - stack[n - 1][1]), abs(stack[0][0] - stack[n - 1][0]))
        return s