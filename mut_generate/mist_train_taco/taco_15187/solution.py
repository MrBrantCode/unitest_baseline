"""
QUESTION:
Vasya takes part in the orienteering competition. There are n checkpoints located along the line at coordinates x_1, x_2, ..., x_{n}. Vasya starts at the point with coordinate a. His goal is to visit at least n - 1 checkpoint in order to finish the competition. Participant are allowed to visit checkpoints in arbitrary order.

Vasya wants to pick such checkpoints and the order of visiting them that the total distance travelled is minimized. He asks you to calculate this minimum possible value.


-----Input-----

The first line of the input contains two integers n and a (1 ≤ n ≤ 100 000,  - 1 000 000 ≤ a ≤ 1 000 000) — the number of checkpoints and Vasya's starting position respectively.

The second line contains n integers x_1, x_2, ..., x_{n} ( - 1 000 000 ≤ x_{i} ≤ 1 000 000) — coordinates of the checkpoints.


-----Output-----

Print one integer — the minimum distance Vasya has to travel in order to visit at least n - 1 checkpoint.


-----Examples-----
Input
3 10
1 7 12

Output
7

Input
2 0
11 -10

Output
10

Input
5 0
0 0 1000 0 0

Output
0



-----Note-----

In the first sample Vasya has to visit at least two checkpoints. The optimal way to achieve this is the walk to the third checkpoints (distance is 12 - 10 = 2) and then proceed to the second one (distance is 12 - 7 = 5). The total distance is equal to 2 + 5 = 7.

In the second sample it's enough to visit only one checkpoint so Vasya should just walk to the point  - 10.
"""

def calculate_minimum_distance(n, a, checkpoints):
    checkpoints.sort()
    
    if n == 1:
        return 0
    elif a >= checkpoints[n - 1]:
        return a - checkpoints[1]
    elif a <= checkpoints[0]:
        return checkpoints[n - 2] - a
    else:
        gauche = min(abs(a - checkpoints[0]), abs(checkpoints[n - 2] - a)) + checkpoints[n - 2] - checkpoints[0]
        droite = min(abs(a - checkpoints[1]), abs(checkpoints[n - 1] - a)) + checkpoints[n - 1] - checkpoints[1]
        return min(gauche, droite)