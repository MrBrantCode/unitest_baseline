"""
QUESTION:
JOI Park

In preparation for the Olympic Games in IOI in 20XX, the JOI Park in IOI will be developed. There are N squares in JOI Park, and the squares are numbered from 1 to N. There are M roads connecting the squares, and the roads are numbered from 1 to M. The road i (1 ≤ i ≤ M) connects the square Ai and the square Bi in both directions, and the length is Di. You can follow several paths from any square to any square.

In the maintenance plan, first select an integer X of 0 or more, and connect all the squares (including square 1) whose distance from square 1 is X or less to each other by an underpass. However, the distance between the square i and the square j is the minimum value of the sum of the lengths of the roads taken when going from the square i to the square j. In the maintenance plan, the integer C for the maintenance cost of the underpass is fixed. The cost of developing an underpass is C x X.

Next, remove all the roads connecting the plazas connected by the underpass. There is no cost to remove the road. Finally, repair all the roads that remained unremoved. The cost of repairing a road of length d is d. There is no underpass in JOI Park before the implementation of the maintenance plan. Find the minimum sum of the costs of developing the JOI Park.

Task

Given the information on the JOI Park Square and an integer for the underpass maintenance cost, create a program to find the minimum sum of the costs for the JOI Park maintenance.

input

Read the following data from standard input.

* On the first line, the integers N, M, and C are written with blanks as delimiters. This means that there are N squares, M roads, and the integer for the underpass maintenance cost is C.
* On the i-th line (1 ≤ i ≤ M) of the following M lines, the integers Ai, Bi, and Di are written separated by blanks. This means that the road i connects the square Ai and the square Bi, and the length is Di.



output

Output an integer representing the minimum sum of the costs of developing the JOI park to the standard output on one line.

Limits

All input data satisfy the following conditions.

* 2 ≤ N ≤ 100 000.
* 1 ≤ M ≤ 200 000.
* 1 ≤ C ≤ 100 000.
* 1 ≤ Ai ≤ N (1 ≤ i ≤ M).
* 1 ≤ Bi ≤ N (1 ≤ i ≤ M).
* Ai ≠ Bi (1 ≤ i ≤ M).
* (Ai, Bi) ≠ (Aj, Bj) and (Ai, Bi) ≠ (Bj, Aj) (1 ≤ i <j ≤ M).
* 1 ≤ Di ≤ 100 000 (1 ≤ i ≤ M).
* With the input data given, it is guaranteed that you can go from any square to any square by following several paths.



Input / output example

Input example 1


5 5 2
2 3 1
3 1 2
2 4 3
1 2 4
2 5 5


Output example 1


14


In this input example, when X = 3, the sum of the maintenance costs when all the squares (square 1, square 2, square 3) whose distance from square 1 is 3 or less are connected to each other by an underpass. Is 2 × 3 + 3 + 5 = 14. This is the minimum value.

Input example 2


5 4 10
one two Three
2 3 4
3 4 3
4 5 5


Output example 2


15


In this input example, the sum of maintenance costs is minimized when X = 0.

Input example 3


6 5 2
1 2 2
1 3 4
1 4 3
1 5 1
1 6 5


Output example 3


Ten


In this input example, when all the squares are connected to each other by an underpass with X = 5, the sum of the maintenance costs is minimized.

The question text and the data used for the automatic referee are the question text and the test data for scoring, which are created and published by the Japan Committee for Information Olympics.





Example

Input

5 5 2
2 3 1
3 1 2
2 4 3
1 2 4
2 5 5


Output

14
"""

from heapq import heappush, heappop

def calculate_minimum_maintenance_cost(n, m, c, roads):
    INF = 10 ** 20
    edges = [[] for _ in range(n)]
    edges_dict = {}
    d_cost = 0
    
    for (a, b, d) in roads:
        a -= 1
        b -= 1
        edges[a].append((b, d))
        edges[b].append((a, d))
        edges_dict[(a, b)] = d
        d_cost += d
    
    dist = [INF] * n
    dist[0] = 0
    que = []
    heappush(que, (0, 0))
    
    while que:
        (total, node) = heappop(que)
        for (to, d) in edges[node]:
            if dist[to] > total + d:
                dist[to] = total + d
                heappush(que, (total + d, to))
    
    removal = {}
    for (t, d) in edges_dict.items():
        max_d = max(dist[t[0]], dist[t[1]])
        if max_d in removal:
            removal[max_d] += d
        else:
            removal[max_d] = d
    
    ans = d_cost
    for (k, v) in sorted(removal.items()):
        d_cost -= v
        if d_cost + k * c < ans:
            ans = d_cost + k * c
    
    return ans