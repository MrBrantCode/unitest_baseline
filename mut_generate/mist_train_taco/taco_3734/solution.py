"""
QUESTION:
This problem is same as the previous one, but has larger constraints.

It was a Sunday morning when the three friends Selena, Shiro and Katie decided to have a trip to the nearby power station (do not try this at home). After arriving at the power station, the cats got impressed with a large power transmission system consisting of many chimneys, electric poles, and wires. Since they are cats, they found those things gigantic.

At the entrance of the station, there is a map describing the complicated wiring system. Selena is the best at math among three friends. He decided to draw the map on the Cartesian plane. Each pole is now a point at some coordinates $(x_i, y_i)$. Since every pole is different, all of the points representing these poles are distinct. Also, every two poles are connected with each other by wires. A wire is a straight line on the plane infinite in both directions. If there are more than two poles lying on the same line, they are connected by a single common wire.

Selena thinks, that whenever two different electric wires intersect, they may interfere with each other and cause damage. So he wonders, how many pairs are intersecting? Could you help him with this problem?


-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 1000$) — the number of electric poles.

Each of the following $n$ lines contains two integers $x_i$, $y_i$ ($-10^4 \le x_i, y_i \le 10^4$) — the coordinates of the poles.

It is guaranteed that all of these $n$ points are distinct.


-----Output-----

Print a single integer — the number of pairs of wires that are intersecting.


-----Examples-----
Input
4
0 0
1 1
0 3
1 2

Output
14

Input
4
0 0
0 2
0 4
2 0

Output
6

Input
3
-1 -1
1 0
3 1

Output
0



-----Note-----

In the first example:

 [Image] 

In the second example:

 [Image] 

Note that the three poles $(0, 0)$, $(0, 2)$ and $(0, 4)$ are connected by a single wire.

In the third example:

 [Image]
"""

from math import gcd

def count_intersecting_wires(n, poles):
    ks = {}
    ct = 0
    res = 0
    ls = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            dy = poles[j][1] - poles[i][1]
            dx = poles[j][0] - poles[i][0]
            if dx < 0:
                dx *= -1
                dy *= -1
            elif dx == 0:
                dy = abs(dy)
            g = gcd(abs(dx), abs(dy))
            k = (dx // g, dy // g)
            (x, y) = (poles[i][0], poles[i][1])
            if dx == 0:
                a = (poles[i][0], 0)
            else:
                cl = abs(x) // k[0]
                if x >= 0:
                    x -= cl * k[0]
                    y -= cl * k[1]
                else:
                    x += cl * k[0]
                    y += cl * k[1]
                    while x < 0:
                        x += k[0]
                        y += k[1]
                a = (x, y)
            if (k, a) in ls:
                continue
            else:
                ls.add((k, a))
            ct += 1
            if k not in ks:
                ks[k] = 1
            else:
                ks[k] += 1
            res += ct - ks[k]
    
    return res