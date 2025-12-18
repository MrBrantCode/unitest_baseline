"""
QUESTION:
There are N integers, A_1, A_2, ..., A_N, written on the blackboard.
You will choose one of them and replace it with an integer of your choice between 1 and 10^9 (inclusive), possibly the same as the integer originally written.
Find the maximum possible greatest common divisor of the N integers on the blackboard after your move.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq N \leq 10^5
 - 1 \leq A_i \leq 10^9

-----Output-----
Input is given from Standard Input in the following format:
N
A_1 A_2 ... A_N

-----Output-----
Print the maximum possible greatest common divisor of the N integers on the blackboard after your move.

-----Sample Input-----
3
7 6 8

-----Sample Output-----
2

If we replace 7 with 4, the greatest common divisor of the three integers on the blackboard will be 2, which is the maximum possible value.
"""

from math import gcd

def max_possible_gcd(N, A):
    def segfunc(x, y):
        return gcd(x, y)
    
    ide_ele = 0
    
    class SegTree:
        def __init__(self, init_val, segfunc, ide_ele):
            n = len(init_val)
            self.segfunc = segfunc
            self.ide_ele = ide_ele
            self.num = 1 << (n - 1).bit_length()
            self.tree = [ide_ele] * 2 * self.num
            for i in range(n):
                self.tree[self.num + i] = init_val[i]
            for i in range(self.num - 1, 0, -1):
                self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

        def update(self, k, x):
            k += self.num
            self.tree[k] = x
            while k > 1:
                self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
                k >>= 1

        def query(self, l, r):
            res = self.ide_ele
            l += self.num
            r += self.num
            while l < r:
                if l & 1:
                    res = self.segfunc(res, self.tree[l])
                    l += 1
                if r & 1:
                    res = self.segfunc(res, self.tree[r - 1])
                l >>= 1
                r >>= 1
            return res

    seg = SegTree(A, segfunc, ide_ele)
    ans = 1
    for i in range(N):
        seg.update(i, 0)
        ans = max(ans, seg.query(0, N))
        seg.update(i, A[i])
    
    return ans