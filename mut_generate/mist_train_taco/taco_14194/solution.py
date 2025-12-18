"""
QUESTION:
On a number line there are n balls. At time moment 0 for each ball the following data is known: its coordinate xi, speed vi (possibly, negative) and weight mi. The radius of the balls can be ignored.

The balls collide elastically, i.e. if two balls weighing m1 and m2 and with speeds v1 and v2 collide, their new speeds will be: 

<image>.

Your task is to find out, where each ball will be t seconds after.

Input

The first line contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 100) — amount of balls and duration of the process. Then follow n lines, each containing three integers: xi, vi, mi (1 ≤ |vi|, mi ≤ 100, |xi| ≤ 100) — coordinate, speed and weight of the ball with index i at time moment 0.

It is guaranteed that no two balls have the same coordinate initially. Also each collision will be a collision of not more than two balls (that is, three or more balls never collide at the same point in all times from segment [0;t]).

Output

Output n numbers — coordinates of the balls t seconds after. Output the numbers accurate to at least 4 digits after the decimal point.

Examples

Input

2 9
3 4 5
0 7 8


Output

68.538461538
44.538461538


Input

3 10
1 2 3
4 -5 6
7 -8 9


Output

-93.666666667
-74.666666667
-15.666666667
"""

def calculate_ball_positions_after_time(n, t, ball_data):
    class Ball:
        def __init__(self, x, v, m):
            self.v = v
            self.x = x
            self.m = m

        def move(self, time):
            self.x += self.v * time

        def collisionTime(self, other):
            if self.v == other.v:
                return float('inf')
            t = -(self.x - other.x) / (self.v - other.v)
            if t < 1e-09:
                return float('inf')
            return t

    def findFirst(balls):
        minTime = float('inf')
        minPairs = []
        for i in range(n):
            for j in range(i + 1, n):
                time = balls[i].collisionTime(balls[j])
                if time < minTime:
                    minTime = time
                    minPairs = [(i, j)]
                elif abs(time - minTime) < 1e-09:
                    minPairs.append((i, j))
        return (minTime, minPairs)

    def collidePair(balls, i, j):
        v1 = balls[i].v
        v2 = balls[j].v
        m1 = balls[i].m
        m2 = balls[j].m
        balls[i].v = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        balls[j].v = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

    balls = [Ball(x, v, m) for x, v, m in ball_data]
    maxTime = t

    while True:
        (time, pairs) = findFirst(balls)
        if time > maxTime:
            break
        for i in range(n):
            balls[i].move(time)
        for (i, j) in pairs:
            collidePair(balls, i, j)
        maxTime -= time

    for ball in balls:
        ball.move(maxTime)

    positions = [ball.x for ball in balls]
    return positions