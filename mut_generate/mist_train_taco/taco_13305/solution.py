"""
QUESTION:
There are N squares in a row. The squares are numbered 1, 2, ..., N from left to right.

You have two pieces, initially placed on square A and B, respectively. You will be asked to process Q queries of the following kind, in the order received:

* Given an integer x_i, move one of the two pieces of your choice to square x_i.



Here, it takes you one second to move a piece one square. That is, the time it takes to move a piece from square X to Y is |X-Y| seconds.

Your objective is to process all the queries in the shortest possible time.

You may only move the pieces in response to queries, and you may not move both pieces at the same time. Also, it is not allowed to rearrange the order in which queries are given. It is, however, allowed to have both pieces in the same square at the same time.

Constraints

* 1 ≤ N, Q ≤ 200,000
* 1 ≤ A, B ≤ N
* 1 ≤ x_i ≤ N

Input

Input is given from Standard Input in the following format:


N Q A B
x_1 x_2 ... x_Q


Output

Let the shortest possible time to process all the queries be X seconds. Print X.

Examples

Input

8 3 1 8
3 5 1


Output

7


Input

9 2 1 9
5 1


Output

4


Input

9 2 1 9
5 9


Output

4


Input

11 16 8 1
1 1 5 1 11 4 5 2 5 3 3 3 5 5 6 7


Output

21
"""

import sys

INF = 10 ** 12

class Rmin:
    def __init__(self, size):
        self.n = 1 << size.bit_length()
        self.node = [INF] * (2 * self.n - 1)

    def Access(self, x):
        return self.node[x + self.n - 1]

    def Update(self, x, val):
        x += self.n - 1
        self.node[x] = val
        while x > 0:
            x = x - 1 >> 1
            self.node[x] = min(self.node[(x << 1) + 1], self.node[(x << 1) + 2])
        return

    def Get(self, l, r):
        (L, R) = (l + self.n, r + self.n)
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.node[R - 1])
            if L & 1:
                s = min(s, self.node[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return s

def calculate_minimum_time(N, Q, A, B, queries):
    dp_l = Rmin(N + 1)
    dp_r = Rmin(N + 1)
    dp_l.Update(B, -B)
    dp_r.Update(B, B)
    total_diff = 0
    x = A
    for y in queries:
        diff = abs(y - x)
        l_min = dp_l.Get(1, y)
        r_min = dp_r.Get(y, N + 1)
        res = min(l_min + y, r_min - y)
        dp_l.Update(x, res - diff - x)
        dp_r.Update(x, res - diff + x)
        total_diff += diff
        x = y
    N = dp_l.n
    return total_diff + min((l + r >> 1 for (l, r) in zip(dp_l.node[N:], dp_r.node[N:])))