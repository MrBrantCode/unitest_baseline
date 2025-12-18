"""
QUESTION:
Limak can repeatedly remove one of the first two characters of a string, for example abcxyx \rightarrow acxyx \rightarrow cxyx \rightarrow cyx.

You are given N different strings S_1, S_2, \ldots, S_N. Among N \cdot (N-1) / 2 pairs (S_i, S_j), in how many pairs could Limak obtain one string from the other?

Constraints

* 2 \leq N \leq 200\,000
* S_i consists of lowercase English letters `a`-`z`.
* S_i \neq S_j
* 1 \leq |S_i|
* |S_1| + |S_2| + \ldots + |S_N| \leq 10^6

Input

Input is given from Standard Input in the following format.


N
S_1
S_2
\vdots
S_N


Output

Print the number of unordered pairs (S_i, S_j) where i \neq j and Limak can obtain one string from the other.

Examples

Input

3
abcxyx
cyx
abc


Output

1


Input

6
b
a
abc
c
d
ab


Output

5
"""

from collections import defaultdict

class RollingHash:
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1] * (len(s) + 1)
        l = len(s)
        self.h = h = [0] * (l + 1)
        v = 0
        for i in range(l):
            h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

def count_transformable_pairs(N, Slist):
    Slist.sort(key=len)
    dic = defaultdict(lambda: defaultdict(int))
    ans = 0
    for S in Slist:
        alp = set()
        l = len(S)
        RH = RollingHash(S, 37, 10 ** 18 + 9)
        for i in range(len(S)):
            alp.add(S[i])
            alpdic = dic[RH.get(i + 1, l)]
            for X in alpdic.keys():
                if X in alp:
                    ans += alpdic[X]
        dic[RH.get(1, l)][S[0]] += 1
    return ans