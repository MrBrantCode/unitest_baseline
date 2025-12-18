"""
QUESTION:
You are given a string `s` and an array of pairs of indices in the string `pairs` where `pairs[i] = [a, b]` indicates 2 indices (0-indexed) of the string. You can swap the characters at any pair of indices in the given `pairs` only once. Write a function `largestString(s, pairs)` that returns the lexicographically largest string that `s` can be changed to after using the swaps. The function should work under the constraints that `1 <= s.length <= 10^5`, `0 <= pairs.length <= 10^5`, `0 <= pairs[i][0], pairs[i][1] < s.length`, and `s` only contains lower case English letters.
"""

from collections import defaultdict

class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        
def largestString(s, pairs):
    dsu = DSU(len(s))
    for x, y in pairs:
        dsu.union(x, y)
        
    group = defaultdict(list)
    for i in range(len(s)):
        group[dsu.find(i)].append(s[i])
    for _, v in group.items():
        v.sort(reverse=True)
    
    ans = []
    for i in range(len(s)):
        ans.append(group[dsu.find(i)].pop())
    return "".join(ans)