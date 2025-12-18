"""
QUESTION:
We will define the median of a sequence b of length M, as follows:
 - Let b' be the sequence obtained by sorting b in non-decreasing order. Then, the value of the (M / 2 + 1)-th element of b' is the median of b. Here, / is integer division, rounding down.
For example, the median of (10, 30, 20) is 20; the median of (10, 30, 20, 40) is 30; the median of (10, 10, 10, 20, 30) is 10.
Snuke comes up with the following problem.
You are given a sequence a of length N.
For each pair (l, r) (1 \leq l \leq r \leq N), let m_{l, r} be the median of the contiguous subsequence (a_l, a_{l + 1}, ..., a_r) of a.
We will list m_{l, r} for all pairs (l, r) to create a new sequence m.
Find the median of m.

-----Constraints-----
 - 1 \leq N \leq 10^5
 - a_i is an integer.
 - 1 \leq a_i \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 a_2 ... a_N

-----Output-----
Print the median of m.

-----Sample Input-----
3
10 30 20

-----Sample Output-----
30

The median of each contiguous subsequence of a is as follows:
 - The median of (10) is 10.
 - The median of (30) is 30.
 - The median of (20) is 20.
 - The median of (10, 30) is 30.
 - The median of (30, 20) is 30.
 - The median of (10, 30, 20) is 20.
Thus, m = (10, 30, 20, 30, 30, 20) and the median of m is 30.
"""

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

def med(x, a, n):
    cum = [0] * (n + 1)
    for i in range(n):
        if a[i] >= x:
            cum[i + 1] = cum[i] + 1
        else:
            cum[i + 1] = cum[i] - 1
    m = min(cum)
    for i in range(n + 1):
        cum[i] -= m - 1
    zb = Bit(max(cum))
    ret = 0
    for j in range(n + 1):
        ret += zb.sum(cum[j])
        zb.add(cum[j], 1)
    return ret

def find_median_of_medians(a, n):
    b = sorted(a)
    l = 0
    r = n
    while r - l > 1:
        mid = (l + r + 1) // 2
        if 2 * med(b[mid], a, n) >= n * (n + 1) // 2:
            l = mid
        else:
            r = mid
    return b[l]