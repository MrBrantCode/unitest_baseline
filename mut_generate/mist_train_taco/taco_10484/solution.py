"""
QUESTION:
E: Jam

problem

There are N cities in a country, numbered 1, \ 2, \ ..., \ N. These cities are connected in both directions by M roads, and the i-th road allows you to travel between the cities u_i and v_i in time t_i. Also, any two cities can be reached by using several roads.

Bread is sold in each town, and the deliciousness of bread sold in town i is P_i.

In addition, there are K flavors of jam in this country, and in town i you can buy delicious J_i jams at taste c_i.

Homu-chan, who lives in Town 1, decided to go out to buy bread and jam one by one. Homu-chan travels through several cities, buys bread and jam, and returns to city 1. More precisely, go to city u to buy bread, select city v to buy jam, and return to city 1. At this time, u = v, u = 1, and v = 1 can be used.

The happiness of Homu-chan after shopping is "the total of the deliciousness of the bread and jam I bought"-"the time it took to move". For each of the K types of jam, calculate the maximum possible happiness when going to buy jam and bread of that taste.

Input format


NMK
P_1 P_2 ... P_N
c_1 c_2 ... c_N
J_1 J_2 ... J_N
u_1 v_1 t_1
u_2 v_2 t_2
::
u_M v_M t_M


Constraint

* 1 \ leq N \ leq 10 ^ 5
* 1 \ leq M \ leq 2 \ times 10 ^ 5
* 1 \ leq K \ leq N
* 1 \ leq P_i, J_i \ leq 10 ^ 9
* 1 \ leq c_i \ leq K
* 1 \ leq u_i, v_i \ leq N
* 1 \ leq t_i \ leq 10 ^ 9
* For all i \ (1 \ leq i \ leq K), there exists j \ (1 \ leq j \ leq N) such that c_j = i.
* Given graphs are concatenated graphs that do not include multiple edges or self-loops.
* All inputs are given as integers



Output format

Please output K line. On line i, print the maximum happiness when you go to buy bread and taste i jam.

Input example 1


4 4 3
3 6 1 6
1 1 2 3
6 1 5 5
1 2 1
2 3 1
1 3 1
1 4 1


Output example 1


Ten
8
9


* When buying taste 1 jam
* If you buy jam in city 1, move to city 2, buy bread, and come back to city 1, your happiness will be 6 + 6-2 = 10, which is optimal.
* When buying taste 2 jam
* If you move to City 2 to buy bread, move to City 3 to buy jam, and return to City 1, your happiness will be 6 + 5-3 = 8.
* When buying taste 3 jam
* If you go to City 4 and buy both bread and jam and come back to City 1, your happiness will be 6 + 5-2 = 9.



Input example 2


2 1 2
1 1
1 2
1 1
1 2 1000000000


Output example 2


2
-1999999998


* Homu-chan seems to be dissatisfied because the distance is too far compared to the deliciousness of bread and jam.



Input example 3


6 8 3
31 41 59 26 53 58
1 2 3 1 2 3
27 18 28 18 28 46
one two Three
2 3 7
2 4 8
3 6 9
3 5 3
4 5 3
1 5 15
4 6 7


Output example 3


66
61
68






Example

Input

4 4 3
3 6 1 6
1 1 2 3
6 1 5 5
1 2 1
2 3 1
1 3 1
1 4 1


Output

10
8
9
"""

import sys
from heapq import heappop as hpp, heappush as hp

def calculate_max_happiness(N, M, K, P, C, J, roads):
    def dijkstra(N, s, Edge):
        inf = 10 ** 18
        dist = [inf] * N
        Q = [(0, s)]
        decided = set()
        for _ in range(N):
            while True:
                (dn, vn) = hpp(Q)
                if vn not in decided:
                    decided.add(vn)
                    dist[vn] = dn
                    break
            for (vf, df) in Edge[vn]:
                if vf not in decided:
                    hp(Q, (dn + df, vf))
        return dist

    Edge1 = [[] for _ in range(N)]
    for (u, v, t) in roads:
        u -= 1
        v -= 1
        Edge1[u].append((v, t))
        Edge1[v].append((u, t))

    dist = dijkstra(N, 0, Edge1)

    Edge2 = [[] for _ in range(3 * N)]
    for (u, v, t) in roads:
        u -= 1
        v -= 1
        Edge2[u].append((v, t))
        Edge2[v].append((u, t))
        Edge2[N + u].append((N + v, t))
        Edge2[N + v].append((N + u, t))

    inf = 10 ** 17
    for i in range(N):
        Edge2[i].append((N + i, inf - P[i]))
        Edge2[N + i].append((2 * N + i, inf - J[i] + dist[i]))

    dist2 = dijkstra(3 * N, 0, Edge2)

    Ans = [-10 ** 20] * K
    for i in range(N):
        Ans[C[i] - 1] = max(Ans[C[i] - 1], 2 * inf - dist2[2 * N + i])

    return Ans