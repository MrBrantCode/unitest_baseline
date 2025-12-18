"""
QUESTION:
It has been noted that if some ants are put in the junctions of the graphene integer lattice then they will act in the following fashion: every minute at each junction (x, y) containing at least four ants a group of four ants will be formed, and these four ants will scatter to the neighbouring junctions (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1) — one ant in each direction. No other ant movements will happen. Ants never interfere with each other.

Scientists have put a colony of n ants into the junction (0, 0) and now they wish to know how many ants will there be at some given junctions, when the movement of the ants stops.

Input

First input line contains integers n (0 ≤ n ≤ 30000) and t (1 ≤ t ≤ 50000), where n is the number of ants in the colony and t is the number of queries. Each of the next t lines contains coordinates of a query junction: integers xi, yi ( - 109 ≤ xi, yi ≤ 109). Queries may coincide.

It is guaranteed that there will be a certain moment of time when no possible movements can happen (in other words, the process will eventually end).

Output

Print t integers, one per line — the number of ants at the corresponding junctions when the movement of the ants stops.

Examples

Input

1 3
0 1
0 0
0 -1


Output

0
1
0


Input

6 5
0 -2
0 -1
0 0
0 1
0 2


Output

0
1
2
1
0

Note

In the first sample the colony consists of the one ant, so nothing happens at all.

In the second sample the colony consists of 6 ants. At the first minute 4 ants scatter from (0, 0) to the neighbouring junctions. After that the process stops.
"""

def calculate_ant_distribution(n, t, queries):
    m = 65
    r = range(m)
    p = [[0] * m for i in r]
    p[1][0] = n // 4
    p[0][0] = n % 4
    q = k = 1
    
    while q:
        k += 1
        q = 0
        for x in r[1:k]:
            for y in r[:x + 1]:
                if p[x][y] < 4:
                    continue
                q = 1
                d = p[x][y] // 4
                p[x][y] %= 4
                p[x + 1][y] += d
                if x > y:
                    if x > y + 1:
                        p[x][y + 1] += d
                        p[x - 1][y] += d
                    else:
                        p[x][x] += 2 * d
                        if y:
                            p[y][y] += 2 * d
                        else:
                            p[x][y] += d
                if y:
                    p[x][y - 1] += d if y > 1 else 2 * d
    
    results = []
    for (x, y) in queries:
        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x
        results.append(p[x][y] if x < m else 0)
    
    return results