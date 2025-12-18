"""
QUESTION:
One day, Snuke was given a permutation of length N, a_1, a_2, ..., a_N, from his friend.

Find the following:

<image>

Constraints

* 1 ≦ N ≦ 200,000
* (a_1, a_2, ..., a_N) is a permutation of (1, 2, ..., N).

Input

The input is given from Standard Input in the following format:


N
a_1 a_2 ... a_N


Output

Print the answer.

Note that the answer may not fit into a 32-bit integer.

Examples

Input

3
2 1 3


Output

9


Input

4
1 3 2 4


Output

19


Input

8
5 4 8 1 2 6 7 3


Output

85
"""

def calculate_permutation_score(N, A):
    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

    B = [[A[i], i] for i in range(N)]
    B.sort()
    L = Bit(N)
    R = Bit(N)
    ans = 0

    for i in range(N):
        l = -1
        r = N + 1
        m = (l + r) // 2
        while r - l > 1:
            if L.sum(m) < L.sum(B[i][1] + 1):
                l = m
            else:
                r = m
            m = (l + r) // 2
        L.add(B[i][1] + 1, 1)
        LL = l

        rr = N - 1 - B[i][1]
        l = -1
        r = N + 1
        m = (l + r) // 2
        while r - l > 1:
            if R.sum(m) < R.sum(rr + 1):
                l = m
            else:
                r = m
            m = (l + r) // 2
        R.add(N - 1 - B[i][1] + 1, 1)
        RR = l

        ans += B[i][0] * (B[i][1] - LL) * (N - 1 - RR - B[i][1])

    return ans