"""
QUESTION:
For a given array $a_1, a_2, a_3, ... , a_N$ of $N$ elements and an integer $K$, find the smallest sub-array size (smallest window length) where the elements in the sub-array contains all integers in range [$1, 2, ..., K$]. If there is no such sub-array, report 0.

Constraints

* $1 \leq N \leq 10^5$
* $1 \leq K \leq 10^5$
* $1 \leq a_i \leq 10^5$

Input

The input is given in the following format.

$N$ $K$
$a_1$ $a_2$ ... $a_N$

Output

Print the smallest sub-array size in a line.

Examples

Input

6 2
4 1 2 1 3 5


Output

2


Input

6 3
4 1 2 1 3 5


Output

3


Input

3 4
1 2 3


Output

0
"""

def find_smallest_subarray_size(N, K, A):
    class SegmentTree:
        def __init__(self, arr, func=min, ie=2 ** 63):
            self.h = (len(arr) - 1).bit_length()
            self.n = 2 ** self.h
            self.ie = ie
            self.func = func
            self.tree = [ie for _ in range(2 * self.n)]
            for i in range(len(arr)):
                self.tree[self.n + i] = arr[i]
            for i in range(1, self.n)[::-1]:
                self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

        def set(self, idx, x):
            idx += self.n
            self.tree[idx] = x
            while idx:
                idx >>= 1
                self.tree[idx] = self.func(self.tree[2 * idx], self.tree[2 * idx + 1])

        def query(self, lt, rt):
            lt += self.n
            rt += self.n
            vl = vr = self.ie
            while rt - lt > 0:
                if lt & 1:
                    vl = self.func(vl, self.tree[lt])
                    lt += 1
                if rt & 1:
                    rt -= 1
                    vr = self.func(self.tree[rt], vr)
                lt >>= 1
                rt >>= 1
            return self.func(vl, vr)

    res = N + 1
    st = SegmentTree([0] * K)
    rt = 0
    for lt in range(N):
        while rt < N and st.tree[1] == 0:
            if A[rt] <= K:
                st.set(A[rt] - 1, st.query(A[rt] - 1, A[rt]) + 1)
            rt += 1
        if st.tree[1] != 0:
            res = min(res, rt - lt)
        if A[lt] <= K:
            st.set(A[lt] - 1, st.query(A[lt] - 1, A[lt]) - 1)
    
    return res if res <= N else 0