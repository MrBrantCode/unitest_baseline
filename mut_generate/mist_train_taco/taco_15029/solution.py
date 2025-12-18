"""
QUESTION:
The hobbits Frodo and Sam are carrying the One Ring to Mordor. In order not to be spotted by orcs, they decided to go through the mountains.

The mountain relief can be represented as a polyline with n points (x_i, y_i), numbered from 1 to n (x_i < x_{i + 1} for 1 ≤ i ≤ n - 1). Hobbits start their journey at the point (x_1, y_1) and should reach the point (x_n, y_n) to complete their mission.

The problem is that there is a tower with the Eye of Sauron, which watches them. The tower is located at the point (x_n, y_n) and has the height H, so the Eye is located at the point (x_n, y_n + H). In order to complete the mission successfully, the hobbits have to wear cloaks all the time when the Sauron Eye can see them, i. e. when there is a direct line from the Eye to the hobbits which is not intersected by the relief.

The hobbits are low, so their height can be considered negligibly small, but still positive, so when a direct line from the Sauron Eye to the hobbits only touches the relief, the Eye can see them.

<image> The Sauron Eye can't see hobbits when they are in the left position, but can see them when they are in the right position.

The hobbits do not like to wear cloaks, so they wear them only when they can be spotted by the Eye. Your task is to calculate the total distance the hobbits have to walk while wearing cloaks.

Input

The first line of the input contains two integers n and H (2 ≤ n ≤ 2 ⋅ 10^5; 1 ≤ H ≤ 10^4) — the number of vertices in polyline and the tower height.

The next n lines contain two integers x_i, y_i each (0 ≤ x_i ≤ 4 ⋅ 10^5; 0 ≤ y_i ≤ 10^4) — the coordinates of the polyline vertices. It is guaranteed that x_i < x_{i + 1} for 1 ≤ i ≤ n - 1.

Output

Print one real number — the total distance the hobbits have to walk while wearing cloaks. Your answer will be considered correct if its absolute or relative error does not exceed 10^{-6} — formally, if your answer is a, and the jury's answer is b, your answer will be accepted if (|a - b|)/(max(1, b)) ≤ 10^{-6}.

Examples

Input


6 10
10 40
20 10
25 30
30 15
50 15
65 30


Output


70.4034587602


Input


9 5
0 0
5 10
15 10
20 0
25 11
30 0
35 10
50 10
60 5


Output


27.2787986124


Input


2 10000
0 10000
400000 0


Output


400124.9804748512
"""

def calculate_cloaked_distance(n, H, points):
    def dot(a, b):
        return a[0] * b[0] + a[1] * b[1]

    def sub(a, b):
        return (a[0] - b[0], a[1] - b[1])

    def norm(a):
        return (a[0] ** 2 + a[1] ** 2) ** 0.5

    eye = (points[-1][0], points[-1][1] + H)
    peak = points[-1]
    out = 0

    for i in range(n - 2, -1, -1):
        p1 = points[i]
        p2 = points[i + 1]
        vecP = sub(peak, eye)
        vecR = (vecP[1], -vecP[0])
        vecP1 = sub(p1, eye)
        vecP2 = sub(p2, eye)
        h1 = dot(vecP1, vecR)
        h2 = dot(vecP2, vecR)

        if h2 >= 0:
            if h1 >= 0:
                out += norm(sub(p1, p2))
                peak = p1
        elif h1 >= 0:
            out += norm(sub(p1, p2)) * (h1 / (h1 - h2))
            peak = p1

    return out