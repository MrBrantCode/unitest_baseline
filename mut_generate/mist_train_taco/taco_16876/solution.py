"""
QUESTION:
There are N computers and N sockets in a one-dimensional world. The coordinate of the i-th computer is a_i, and the coordinate of the i-th socket is b_i. It is guaranteed that these 2N coordinates are pairwise distinct.

Snuke wants to connect each computer to a socket using a cable. Each socket can be connected to only one computer.

In how many ways can he minimize the total length of the cables? Compute the answer modulo 10^9+7.

Constraints

* 1 ≤ N ≤ 10^5
* 0 ≤ a_i, b_i ≤ 10^9
* The coordinates are integers.
* The coordinates are pairwise distinct.

Input

The input is given from Standard Input in the following format:


N
a_1
:
a_N
b_1
:
b_N


Output

Print the number of ways to minimize the total length of the cables, modulo 10^9+7.

Examples

Input

2
0
10
20
30


Output

2


Input

3
3
10
8
7
12
5


Output

1
"""

def count_min_cable_connections(N, a, b):
    mod = 10 ** 9 + 7
    
    # Combine and sort the coordinates with a marker to distinguish between computers and sockets
    E = sorted(((e, 2 * (i < N) - 1) for i, e in enumerate(a + b)))
    
    res = 1
    cnt = 0
    
    for _, delta in E:
        if cnt * delta < 0:
            res *= abs(cnt)
            res %= mod
        cnt += delta
    
    return res