"""
QUESTION:
Iahub got lost in a very big desert. The desert can be represented as a n × n square matrix, where each cell is a zone of the desert. The cell (i, j) represents the cell at row i and column j (1 ≤ i, j ≤ n). Iahub can go from one cell (i, j) only down or right, that is to cells (i + 1, j) or (i, j + 1). 

Also, there are m cells that are occupied by volcanoes, which Iahub cannot enter. 

Iahub is initially at cell (1, 1) and he needs to travel to cell (n, n). Knowing that Iahub needs 1 second to travel from one cell to another, find the minimum time in which he can arrive in cell (n, n).


-----Input-----

The first line contains two integers n (1 ≤ n ≤ 10^9) and m (1 ≤ m ≤ 10^5). Each of the next m lines contains a pair of integers, x and y (1 ≤ x, y ≤ n), representing the coordinates of the volcanoes.

Consider matrix rows are numbered from 1 to n from top to bottom, and matrix columns are numbered from 1 to n from left to right. There is no volcano in cell (1, 1). No two volcanoes occupy the same location. 


-----Output-----

Print one integer, the minimum time in which Iahub can arrive at cell (n, n). If no solution exists (there is no path to the final cell), print -1.


-----Examples-----
Input
4 2
1 3
1 4

Output
6

Input
7 8
1 6
2 6
3 5
3 6
4 3
5 1
5 2
5 3

Output
12

Input
2 2
1 2
2 1

Output
-1



-----Note-----

Consider the first sample. A possible road is: (1, 1)  →  (1, 2)  →  (2, 2)  →  (2, 3)  →  (3, 3)  →  (3, 4)  →  (4, 4).
"""

from collections import defaultdict

def minimum_time_to_reach_end(n, m, volcanoes):
    def f(u, v):
        s, l = [], len(v)
        i = j = 0
        for i in range(len(u)):
            while j < l and v[j][1] <= u[i][0]:
                j += 1
                if j == l:
                    return s
            if u[i][1] <= v[j][0]:
                continue
            if u[i][0] >= v[j][0]:
                s.append(u[i])
            else:
                s.append((v[j][0], u[i][1]))
        return s

    p = defaultdict(list)
    for x, y in volcanoes:
        p[x].append(y)

    for x in p:
        if len(p[x]) > 1:
            p[x].sort()
        t, i = [], 1
        for j in p[x]:
            if i != j:
                t.append((i, j))
            i = j + 1
        if i != n + 1:
            t.append((i, n + 1))
        p[x] = t

    k, s = 1, [(1, 2)]
    for x in sorted(p.keys()):
        if x == k:
            s = f(p[x], s)
        else:
            s = f(p[x], [(s[0][0], n + 1)])
        if not s:
            break
        k = x + 1

    if s and k == n + 1 and (s[-1][1] != k):
        s = []

    return 2 * (n - 1) if s else -1