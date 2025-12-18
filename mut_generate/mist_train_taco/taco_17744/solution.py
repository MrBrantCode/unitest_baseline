"""
QUESTION:
Let x be a string of length at least 1.
We will call x a good string, if for any string y and any integer k (k \geq 2), the string obtained by concatenating k copies of y is different from x.
For example, a, bbc and cdcdc are good strings, while aa, bbbb and cdcdcd are not.
Let w be a string of length at least 1.
For a sequence F=(\,f_1,\,f_2,\,...,\,f_m) consisting of m elements,
we will call F a good representation of w, if the following conditions are both satisfied:
 - For any i \, (1 \leq i \leq m), f_i is a good string.
 - The string obtained by concatenating f_1,\,f_2,\,...,\,f_m in this order, is w.
For example, when w=aabb, there are five good representations of w:
 - (aabb)
 - (a,abb)
 - (aab,b)
 - (a,ab,b)
 - (a,a,b,b)
Among the good representations of w, the ones with the smallest number of elements are called the best representations of w.
For example, there are only one best representation of w=aabb: (aabb).
You are given a string w. Find the following:
 - the number of elements of a best representation of w
 - the number of the best representations of w, modulo 1000000007 \, (=10^9+7)
(It is guaranteed that a good representation of w always exists.)

-----Constraints-----
 - 1 \leq |w| \leq 500000 \, (=5 \times 10^5)
 - w consists of lowercase letters (a-z).

-----Partial Score-----
 - 400 points will be awarded for passing the test set satisfying 1 \leq |w| \leq 4000.

-----Input-----
The input is given from Standard Input in the following format:
w

-----Output-----
Print 2 lines.
 - In the first line, print the number of elements of a best representation of w.
 - In the second line, print the number of the best representations of w, modulo 1000000007.

-----Sample Input-----
aab

-----Sample Output-----
1
1
"""

def find_best_representation(w: str) -> tuple[int, int]:
    MOD = 1000000007
    n = len(w)
    t = -1

    def Z(s: list[str]) -> list[int]:
        m = len(s)
        z = [0] * m
        c = 0
        f = [1] * m
        for i in range(1, m):
            if i + z[i - c] < c + z[c]:
                z[i] = z[i - c]
            else:
                j = max(0, c + z[c] - i)
                while i + j < n and s[j] == s[i + j]:
                    j += 1
                z[i] = j
                c = i
        for p in range(1, m):
            for k in range(2, z[p] // p + 2):
                f[k * p - 1] = 0
        return f

    for j in range(1, n // 2 + 1):
        if n % j == 0 and w[:n - j] == w[j:]:
            t = j
            break

    if t == -1:
        return 1, 1
    elif t == 1:
        return n, 1
    else:
        zl = Z(list(w))
        zr = Z(list(reversed(w)))
        cnt = 0
        for i in range(0, n - 1):
            if zl[i] and zr[n - 2 - i]:
                cnt += 1
        return 2, cnt % MOD