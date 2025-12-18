"""
QUESTION:
You are given a permutation $p$ of $n$ integers $1$, $2$, ..., $n$ (a permutation is an array where each element from $1$ to $n$ occurs exactly once).

Let's call some subsegment $p[l, r]$ of this permutation special if $p_l + p_r = \max \limits_{i = l}^{r} p_i$. Please calculate the number of special subsegments.


-----Input-----

The first line contains one integer $n$ ($3 \le n \le 2 \cdot 10^5$).

The second line contains $n$ integers $p_1$, $p_2$, ..., $p_n$ ($1 \le p_i \le n$). All these integers are pairwise distinct.


-----Output-----

Print the number of special subsegments of the given permutation.


-----Examples-----
Input
5
3 4 1 5 2

Output
2

Input
3
1 3 2

Output
1



-----Note-----

Special subsegments in the first example are $[1, 5]$ and $[1, 3]$.

The only special subsegment in the second example is $[1, 3]$.
"""

def count_special_subsegments(n, p):
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

        def lower_bound(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.size.bit_length() - 1)
            while k:
                if x + k <= self.size and self.tree[x + k] < w:
                    w -= self.tree[x + k]
                    x += k
                k >>= 1
            return x + 1

    idx = [0] * (n + 1)
    for (i, p_val) in enumerate(p):
        idx[p_val] = i + 1

    bit = Bit(n)
    ans = 0

    for p_val in range(n, 0, -1):
        i = idx[p_val]
        k = bit.sum(i)
        r = bit.lower_bound(k + 1)
        l = bit.lower_bound(k)
        nl = i - l - 1
        nr = r - i - 1

        if nl < nr:
            for j in range(l + 1, i):
                q = p[j - 1]
                if i < idx[p_val - q] < r:
                    ans += 1
        else:
            for j in range(i + 1, r):
                q = p[j - 1]
                if l < idx[p_val - q] < i:
                    ans += 1

        bit.add(i, 1)

    return ans