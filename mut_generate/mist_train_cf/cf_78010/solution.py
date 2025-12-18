"""
QUESTION:
Write a function `smallestEquivalentString(A, B, S)` that returns the lexicographically smallest equivalent string of `S` by using the equivalency information from `A` and `B`. 

`A` and `B` are strings of the same length consisting of lowercase English letters from 'a' to 'z'. The lengths of `A`, `B`, and `S` are between 1 and 1000. 

The function should not exceed O(n^2) time complexity.
"""

def smallestEquivalentString(s1, s2, S):
    parent = list(range(26))

    def find(i):  
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):  
        pi, pj = find(i), find(j)
        if pi != pj:
            min_p = min(pi, pj)
            parent[pi] = min_p
            parent[pj] = min_p

    for a, b in zip(s1, s2):
        union(ord(a) - ord('a'), ord(b) - ord('a'))

    return ''.join(chr(find(ord(c) - ord('a')) + ord('a')) for c in S)