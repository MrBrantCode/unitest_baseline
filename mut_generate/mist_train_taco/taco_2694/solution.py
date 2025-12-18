"""
QUESTION:
Read problems statements in [Hindi], [Mandarin Chinese], [Russian], [Vietnamese], and [Bengali] as well.

[Flappy Bird] is on a screen with height $H$ pixels (a 2D plane where the $y$-axis corresponds to the vertical direction). There are $N$ vertical obstacles in the room (numbered $1$ through $N$); for each valid $i$, the coordinates of the *endpoint* of the $i$-th obstacle are $(x_{i}, a_{i})$. There are two types of obstacles: 
Type 0: A line segment between the points $(x_{i}, 0)$ and $(x_{i}, a_{i})$, i.e. upwards from the floor.
Type 1: A line segment between the points $(x_{i}, H)$ and $(x_{i}, a_{i})$, i.e. downwards from the ceiling.

For each obstacle, you need to find the number of endpoints of other obstacles (not including itself) that are visible from its endpoint. Two endpoints are visible from each other if the line segment joining them does not intersect or touch any other obstacle. Note that each obstacle has exactly one endpoint.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $H$ and $N$.
The following $N$ lines describe the obstacles. For each valid $i$, the $i$-th of these lines contains three space-separated integers $t_{i}$, $x_{i}$ and $a_{i}$, where $t_{i}$ is the type of the $i$-th obstacle.

------  Output ------
For each test case, print a single line containing $N$ space-separated integers. For each valid $i$, the $i$-th of these integers should be the number of endpoints visible from the $i$-th endpoint.

------  Constraints  ------
$1 ≤ T ≤ 200$
$1 ≤ H ≤ 10^{9}$
$1 ≤ N ≤ 2,000$
$t_{i} \in \{0, 1\}$ for each valid $i$
$1 ≤ x_{i} ≤ 10^{9}$ for each valid $i$
$1 ≤ a_{i} ≤ H-1$ for each valid $i$
no two obstacles touch or intersect
the sum of $N$ over all test cases does not exceed $20,000$

----- Sample Input 1 ------ 
1

10 4

0 2 5

1 5 6

1 8 8

0 11 2
----- Sample Output 1 ------ 
2 3 2 3
----- explanation 1 ------ 
Example case 1:
"""

def count_visible_endpoints(H, N, obstacles):
    r = []
    for i in range(N):
        tt, x, a = obstacles[i]
        r.append([tt, x, a, i])
    r.sort(key=lambda x: x[1])
    fr = [0 for i in range(N)]
    
    for i in range(N):
        slope1 = float('inf')
        slope2 = -float('inf')
        x, y = r[i][1], r[i][2]
        typ = r[i][0]
        c = 0
        
        for j in range(i + 1, N):
            try:
                cur = (y - r[j][2]) / (x - r[j][1])
            except ZeroDivisionError:
                c += 1
                fr[r[j][3]] += 1
                continue
            
            if typ == 0:
                if r[j][0] == 1:
                    if slope1 > cur and cur > slope2:
                        c += 1
                        fr[r[j][3]] += 1
                    slope1 = min(cur, slope1)
                else:
                    if slope2 < cur and cur < slope1:
                        c += 1
                        fr[r[j][3]] += 1
                    slope2 = max(cur, slope2)
            else:
                if r[j][0] == 1:
                    if slope1 > cur and cur > slope2:
                        c += 1
                        fr[r[j][3]] += 1
                    slope1 = min(cur, slope1)
                else:
                    if slope2 < cur and cur < slope1:
                        c += 1
                        fr[r[j][3]] += 1
                    slope2 = max(cur, slope2)
            
            if slope2 >= slope1:
                break
        
        fr[r[i][3]] += c
    
    return fr