"""
QUESTION:
The sales department of Japanese Ancient Giant Corp. is visiting a hot spring resort for their recreational trip. For deepening their friendships, they are staying in one large room of a Japanese-style hotel called a ryokan.

In the ryokan, people sleep in Japanese-style beds called futons. They all have put their futons on the floor just as they like. Now they are ready for sleeping but they have one concern: they don’t like to go into their futons with their legs toward heads — this is regarded as a bad custom in Japanese tradition. However, it is not obvious whether they can follow a good custom. You are requested to write a program answering their question, as a talented programmer.

Here let's model the situation. The room is considered to be a grid on an xy-plane. As usual, x-axis points toward right and y-axis points toward up. Each futon occupies two adjacent cells. People put their pillows on either of the two cells. Their heads come to the pillows; their foots come to the other cells. If the cell of some person's foot becomes adjacent to the cell of another person's head, regardless their directions, then it is considered as a bad case. Otherwise people are all right.



Input

The input is a sequence of datasets. Each dataset is given in the following format:

n
x1 y1 dir1
...
xn yn dirn


n is the number of futons (1 ≤ n ≤ 20,000); (xi, yi) denotes the coordinates of the left-bottom corner of the i-th futon; diri is either 'x' or 'y' and denotes the direction of the i-th futon, where 'x' means the futon is put horizontally and 'y' means vertically. All coordinate values are non-negative integers not greater than 109 .

It is guaranteed that no two futons in the input overlap each other.

The input is terminated by a line with a single zero. This is not part of any dataset and thus should not be processed.

Output

For each dataset, print "Yes" in a line if it is possible to avoid a bad case, or "No" otherwise.

Example

Input

4
0 0 x
2 0 x
0 1 x
2 1 x
4
1 0 x
0 1 x
2 1 x
1 2 x
4
0 0 x
2 0 y
0 1 y
1 2 x
0


Output

Yes
No
Yes
"""

def can_avoid_bad_case(n, futons):
    from collections import defaultdict, deque

    f = defaultdict(lambda: 0)
    v = defaultdict(list)
    l = []

    for (a, b, dir) in futons:
        f[a, b] = 1
        dir = 0 if dir == 'x' else 1
        (na, nb) = (a + 1 - dir, b + dir)
        f[na, nb] = 1
        l.append((a, b, na, nb))
        l.append((na, nb, a, b))
        v[a, b].append(((na, nb), 1))
        v[na, nb].append(((a, b), 1))

    move = [(0, 1), (1, 0)]

    for (a, b, c, d) in l:
        for (dx, dy) in move:
            (na, nb) = (a + dx, b + dy)
            if f[na, nb] and (c, d) != (na, nb):
                v[a, b].append(((na, nb), 0))
                v[na, nb].append(((a, b), 0))

    bfs = defaultdict(lambda: -1)
    q = deque()

    for (a, b, c, d) in l:
        if bfs[a, b] < 0:
            q.append((a, b))
            bfs[a, b] = 0
            while q:
                (x, y) = q.popleft()
                for (node, k) in v[x, y]:
                    (nx, ny) = node
                    if k:
                        nb = 1 - bfs[x, y]
                    else:
                        nb = bfs[x, y]
                    if bfs[nx, ny] >= 0:
                        if bfs[nx, ny] != nb:
                            return 'No'
                    else:
                        bfs[nx, ny] = nb
                        q.append((nx, ny))

    return 'Yes'