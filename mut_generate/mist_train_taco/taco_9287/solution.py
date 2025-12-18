"""
QUESTION:
This problem is same as the next one, but has smaller constraints.

It was a Sunday morning when the three friends Selena, Shiro and Katie decided to have a trip to the nearby power station (do not try this at home). After arriving at the power station, the cats got impressed with a large power transmission system consisting of many chimneys, electric poles, and wires. Since they are cats, they found those things gigantic.

At the entrance of the station, there is a map describing the complicated wiring system. Selena is the best at math among three friends. He decided to draw the map on the Cartesian plane. Each pole is now a point at some coordinates $(x_i, y_i)$. Since every pole is different, all of the points representing these poles are distinct. Also, every two poles are connected with each other by wires. A wire is a straight line on the plane infinite in both directions. If there are more than two poles lying on the same line, they are connected by a single common wire.

Selena thinks, that whenever two different electric wires intersect, they may interfere with each other and cause damage. So he wonders, how many pairs are intersecting? Could you help him with this problem?


-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 50$) — the number of electric poles.

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

In the first example: [Image] 

In the second example: [Image] 

Note that the three poles $(0, 0)$, $(0, 2)$ and $(0, 4)$ are connected by a single wire.

In the third example: [Image]
"""

from fractions import Fraction

def count_intersecting_wires(n, poles):
    d2 = {}
    for i in range(n):
        x, y = poles[i]
        for j in range(i):
            item = poles[j]
            if x == item[0]:
                if 'inf' not in d2:
                    d2['inf'] = [x]
                elif x not in d2['inf']:
                    d2['inf'].append(x)
            else:
                slope = Fraction(y - item[1], x - item[0])
                c = Fraction(y, 1) - slope * Fraction(x, 1)
                if slope not in d2:
                    d2[slope] = [c]
                elif c not in d2[slope]:
                    d2[slope].append(c)
    
    z = 0
    ans = 0
    f = 0
    for k in d2:
        z += len(d2[k])
    for k in d2:
        x = len(d2[k])
        f = f + x
        ans += x * (z - f)
    
    return ans