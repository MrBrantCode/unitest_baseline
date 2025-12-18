"""
QUESTION:
A robot is initially at $(0,0)$ on the cartesian plane. It can move in 4 directions - up, down, left, right denoted by letter u, d, l, r respectively. More formally:
- if the position of robot is $(x,y)$ then u makes it $(x,y+1)$
- if the position of robot is $(x,y)$ then l makes it $(x-1,y)$
- if the position of robot is $(x,y)$ then d makes it $(x,y-1)$
- if the position of robot is $(x,y)$ then r makes it $(x+1,y)$
The robot is performing a counter-clockwise spiral movement such that his movement can be represented by the following sequence of moves -
ulddrruuulllddddrrrruuuuu… and so on.
A single move takes 1 sec. You have to find out the position of the robot on the cartesian plane at $t$ second.

-----Input:-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $t$.

-----Output:-----
For each test case, print two space-separated integers, $(x,y)$ — the position of the robot.

-----Constraints-----
- $1 \leq T \leq 10^6$
- $1 \leq t \leq 10^{18}$

-----Sample Input:-----
5
1
2
3
50
12233443

-----Sample Output:-----
0 1
-1 1
-1 0
2 4
-1749 812
"""

def find_robot_position(t: int) -> tuple:
    p = int(t ** 0.5)
    if p * (p + 1) < t:
        p += 1
    
    (x, y) = (0, 0)
    q = 0
    flag = True
    
    if p * (p + 1) == t:
        q = p
    else:
        q = p - 1
        flag = False
    
    if q % 2:
        x -= (q + 1) // 2
        y += (q + 1) // 2
    else:
        x += q // 2
        y -= q // 2
    
    if flag:
        return (x, y)
    else:
        l = q * (q + 1)
        t_new = p * (p + 1)
        diff = t_new - l
        
        if x < 0:
            if t - l >= diff // 2:
                y *= -1
                l += diff // 2
                x += t - l
            else:
                y -= t - l
        elif t - l >= diff // 2:
            y *= -1
            y += 1
            l += diff // 2
            x -= t - l
        else:
            y += t - l
        
        return (x, y)