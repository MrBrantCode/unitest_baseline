"""
QUESTION:
Given a string s of length n where s[i] is either 'I' or 'D', reconstruct a permutation perm of n + 1 integers in the range [0, n] such that perm[i] < perm[i + 1] when s[i] == 'I' and perm[i] > perm[i + 1] when s[i] == 'D'. Return the reconstructed permutation perm and the number of possible permutations that can be formed from the given string s.

Restrictions: 1 <= s.length <= 10^5.
"""

def diStringMatch(s):
    lo, hi = 0, len(s)
    ans = []
    for x in s:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1
    return (ans + [lo], hi + 1)