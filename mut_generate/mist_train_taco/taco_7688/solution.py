"""
QUESTION:
Snuke has a string s. From this string, Anuke, Bnuke, and Cnuke obtained strings a, b, and c, respectively, as follows:

* Choose a non-empty (contiguous) substring of s (possibly s itself). Then, replace some characters (possibly all or none) in it with `?`s.



For example, if s is `mississippi`, we can choose the substring `ssissip` and replace its 1-st and 3-rd characters with `?` to obtain `?s?ssip`.

You are given the strings a, b, and c. Find the minimum possible length of s.

Constraints

* 1 \leq |a|, |b|, |c| \leq 2000
* a, b, and c consists of lowercase English letters and `?`s.

Input

Input is given from Standard Input in the following format:


a
b
c


Output

Print the minimum possible length of s.

Examples

Input

a?c
der
cod


Output

7


Input

atcoder
atcoder
???????


Output

7
"""

def find_minimum_length_of_s(a: str, b: str, c: str) -> int:
    def F(a, b):
        A = len(a)
        r = [all([len(set([a[i + j], b[j], '?'])) < 3 for j in range(min(A - i, len(b)))]) for i in range(A)]
        return r + [1]

    def Z(X):
        (i, j, k) = X
        (U, V, W) = (M[i][j], M[j][k], M[i][k])
        (A, B, C) = map(len, [S[i] for i in X])
        q = A + B + C
        for l in range(A + 1):
            if U[l]:
                for r in range(l, A + B + 1):
                    if (B < r - l or V[r - l]) * W[min(A, r)]:
                        q = min(q, max(A, l + B, r + C))
        return q

    S = [a, b, c]
    T = range(3)
    M = [[F(S[i], S[j]) for j in T] for i in T]
    from itertools import permutations
    return min([Z(i) for i in permutations(T)])