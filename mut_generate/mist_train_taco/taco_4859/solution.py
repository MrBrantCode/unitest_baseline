"""
QUESTION:
Write a program which manipulates a sequence A = {a0, a1, . . . , an-1} with the following operations:

* find(s, t): report the minimum element in as, as+1, . . . ,at.
* update(i, x): change ai to x.



Note that the initial values of ai (i = 0, 1, . . . , n−1) are 231-1.

Constraints

* 1 ≤ n ≤ 100000
* 1 ≤ q ≤ 100000
* If comi is 0, then 0 ≤ xi < n, 0 ≤ yi < 231-1.
* If comi is 1, then 0 ≤ xi < n, 0 ≤ yi < n.

Input


n q
com0 x0 y0
com1 x1 y1
...
comq−1 xq−1 yq−1


In the first line, n (the number of elements in A) and q (the number of queries) are given. Then, q queries are given where com represents the type of queries. '0' denotes update(xi, yi) and '1' denotes find(xi, yi).

Output

For each find operation, print the minimum element.

Examples

Input

3 5
0 0 1
0 1 2
0 2 3
1 0 2
1 1 2


Output

1
2


Input

1 3
1 0 0
0 0 5
1 0 0


Output

2147483647
5
"""

def process_sequence_operations(n, q, queries):
    class SegTree:
        def __init__(self, N, f, ini):
            n = 1
            while n < N:
                n <<= 1
            self.n = n
            self.arr = [ini] * (2 * n - 1)
            (self.f, self.ini) = (f, ini)

        def update(self, i, val):
            i += self.n - 1
            self.arr[i] = val
            while i > 0:
                i = (i - 1) // 2
                self.arr[i] = self.f(self.arr[2 * i + 1], self.arr[2 * i + 2])

        def find(self, s, t):
            return self.__find(s, t, 0, 0, self.n)

        def __find(self, s, t, k, l, r):
            if t <= l or s >= r:
                return self.ini
            if s <= l and t >= r:
                return self.arr[k]
            vl = self.__find(s, t, 2 * k + 1, l, (l + r) // 2)
            vr = self.__find(s, t, 2 * k + 2, (l + r) // 2, r)
            return self.f(vl, vr)

    st = SegTree(n, lambda x, y: min(x, y), 2 ** 31 - 1)
    results = []

    for (com, x, y) in queries:
        if com == 0:
            st.update(x, y)
        elif com == 1:
            results.append(st.find(x, y + 1))

    return results